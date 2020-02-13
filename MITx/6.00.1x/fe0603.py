# Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# We want to write some simple procedures that work on dictionaries to return information.

# This time, write a procedure, called "biggest", which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

# Example usage:
"""
>>> biggest(animals)
'd'
"""
# If there are no values in the dictionary, "biggest" should return "None".

##########

import copy

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    num_list = []
    dict_copy = aDict.copy()
    for i in dict_copy:
        dict_copy[i] = len(dict_copy[i])
        num_list.append(dict_copy[i])
    maxnum = max(num_list)
    for j in dict_copy:
        if maxnum == dict_copy[j]:
            return j

##########

print(biggest(animals))