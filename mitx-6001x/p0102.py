# [Problem 2 | Problem Set 1 | 6.00.1x Courseware | edX](https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/fc8f42302c644118adfcfa720f9f403e/ca19e125470846f2a36ad1225410e39a/?child=first)

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs 
in s. For example, if s = 'azcbobobegghakl', then your program should 
print:

Number of times bob occurs is: 2
"""

s = 'bobbsbobobbobbbooboboobobobbobbobobokfb'

##########

num = 0

for i in range(len(s)):
    if s[i:i+3] == "bob":
        num += 1

print("Number of times bob occurs is: " + str(num))