"""
Here is the code for a function applyToEach:
"""
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

"""
Assume that
"""
testList = [1, -4, 8, -9]
    
# For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using "applyToEach", so that after evaluation "testList" has the indicated value. You may need to write a simple procedure in each question to help with this process.

"""
Example:

>>> print(testList)
[5, -20, 40, -45]

----------

def timesFive(a):
    return a * 5

applyToEach(testList, timesFive)
"""


### 1
"""
>>> print(testList)
[1, 4, 8, 9]
"""
#----------
applyToEach(testList, abs)



### 2
"""
>>> print(testList)
[2, -3, 9, -8]
"""
#----------
def addsOne(a):
    return a + 1

applyToEach(testList, addsOne)



### 3
"""
>>> print testList
[1, 16, 64, 81]
"""
def square(a):
    return a ** 2

applyToEach(testList, square)