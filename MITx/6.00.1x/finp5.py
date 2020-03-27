"""
You are given a dictionary aDict that maps integer keys to integer values. 
Write a Python function that returns a list of keys in aDict that map to 
dictionary values that appear exactly once in aDict.

- This function takes in a dictionary and returns a list.
- Return the list of keys in increasing order.
- If aDict does not contain any values appearing exactly once, return an empty list.
- If aDict is empty, return an empty list.

For example:
If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
If aDict = {1: 1, 2: 1, 3: 1} then your function should return []
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    output = []
    def isUnique(key):
        """
        key: a certain key of aDict
        returns: True if the value of the key is unique, False otherwise.
        """
        for traversalKey in aDict:
            if traversalKey != key and aDict[traversalKey] == aDict[key]:
                return False
        return True
    
    if aDict == {}:
        return []
    for key in aDict:
        #print(f"key: {key}; isUnique: {isUnique(key)}") # debug!!!
        if isUnique(key):
            output.append(key)
    return sorted(output)

##################################################

aDict = {3: 2, 6: 0, 7: 0, 8: 4, 10: 0, 1: 1}
# should return [1, 3, 8]
print("print(uniqueValues(aDict)):", uniqueValues(aDict))

aDict = {1: 1, 2: 1, 3: 1}
# should return []
print("print(uniqueValues(aDict)):", uniqueValues(aDict))