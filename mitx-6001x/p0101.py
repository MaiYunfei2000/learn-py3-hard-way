# [Problem 1 | Problem Set 1 | 6.00.1x Courseware | edX](https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/fc8f42302c644118adfcfa720f9f403e/ca19e125470846f2a36ad1225410e39a/?child=first)

s = 'azcbobobeGGhakl'

##########

s_lower = s.casefold()
vowels_list = ['a', 'e', 'i', 'o', 'u']
vowels_num = 0

for character in s_lower:
    if character in vowels_list:
        vowels_num += 1

print("Number of vowels: " + str(vowels_num))