"""
You are given the following definitions:

- A run of monotonically increasing numbers means that a number at position
  k+1 in the sequence is greater than or equal to the number at position k 
  in the sequence.
- A run of monotonically decreasing numbers means that a number at position
  k+1 in the sequence is less than or equal to the number at position k in
  the sequence.

Implement a function that meets the specifications below.
"""

"""
- If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically
  increasing numbers in L is [3, 4, 5, 7, 7] and the longest run of 
  monotonically decreasing numbers in L is [10, 4, 3]. Your function should 
  return the value 26 because the longest run of monotonically increasing 
  integers is longer than the longest run of monotonically decreasing numbers.
- If L = [5, 4, 10] then the longest run of monotonically increasing numbers
  in L is [4, 10] and the longest run of monotonically decreasing numbers in
  L is [5, 4]. Your function should return the value 9 because the longest 
  run of monotonically decreasing integers occurs before the longest run of 
  monotonically increasing numbers.
"""

##################################################

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    storage = []
    def is_mono_incre(ls):
        """
        Assumes ls is a sublist of list L.
        Determine if ls is monotonically increasing.
        Returns True if so, False otherwise.
        """
        for i in range(len(ls)-1):
            if ls[i] > ls[i+1]:
                return False
        return True
    def is_mono_decre(ls):
        """
        Assumes ls is a sublist of list L.
        Determine if ls is monotonically increasing.
        Returns True if so, False otherwise.
        """
        for i in range(len(ls)-1):
            if ls[i] < ls[i+1]:
                return False
        return True
    def is_mono(ls):
        """
        Assumes ls is a sublist of list L.
        Determine if ls is monotonically increasing or monotonically decreasing.
        Returns True if so, False otherwise.
        """
        if is_mono_decre(ls) or is_mono_incre(ls):
            return True
        else:
            return False
    
    if is_mono(L):
        return sum(L)
    for length in list(range(2,len(L)+1))[::-1]:
        for i in range(len(L)-length+1):
            temp_list = L[i:i+length]
            #print("temp_list:", temp_list)
            if is_mono(temp_list):
                #print("length:", length, "; temp_list is mono: ", temp_list)
                storage.append(temp_list)
    return sum(storage[0])

##################################################

L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] 
# should return 26
print(longest_run(L))

L = [5, 4, 10]
# should return 9, see instruction
print(longest_run(L))

# kuso！练了一年Python了，对于索引的应用还是很生疏！！！！！！

# should be 65
print(longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

# should be -6
print(longest_run([1, 2, 3, 2, -1, -10]))
