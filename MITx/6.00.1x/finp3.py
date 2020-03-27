# Write a Python function that takes in a string and prints out a version of this string that does not contain any vowels, according to the specification below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

##################################################

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string = []
    for char in s:
        if char not in vowels:
            string.append(char)
    print(''.join(string))

##################################################

s = "This is great!"
# should be "Ths s grt!"
print_without_vowels(s)

s = "a"
# should be ""
print_without_vowels(s)