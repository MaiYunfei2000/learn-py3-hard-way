# [Problem 3 | Problem Set 1 | 6.00.1x Courseware | edX](https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/fc8f42302c644118adfcfa720f9f403e/ca19e125470846f2a36ad1225410e39a/?child=first)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

##### 思路1：最短为2个字符，最长为整个字符串，暴力拎出一个个单词，判断是否完全按顺序。从2至i不断变大即可。

s = 'rlhkdzgipromy' # gipr
s = 'suvynfmooabtdnplsunim' # suvy
s = 'zyxwvutsrqponmlkjihgfedcba' # z
#s = 'abcdefghijklmnopq'

#s = "azcbobobegghaklabcfhhhhhhh"
# 15个，第一遍，每个子串长度为2，其中最长的为abcfhhhhhhh 

##########

print("\n### Version 1 ###\n")

alphabet_list = ("""a b c d e f g h i j k l m n o p q r s t u v w x y z
                 """.split())
alphabet_dict = dict(zip(alphabet_list, list(range(1, 27))))

def is_alphabetical_order(string):
    true_num = 0
    
    for char_index in range(len(string)):
        
        if ((char_index == (len(string)-1) or 
                alphabet_dict[string[char_index]] <= 
                alphabet_dict[string[char_index+1]])):
            true_num += 1
        else:
            return False
    
    return True

longest_substr = []

for len_substr in range(1, len(s)+1): 
    
    longest_this_loop = []   
    
    for word_index in range(len(s)-len_substr):
        
        substring = s[word_index:(word_index+len_substr)]
        if is_alphabetical_order(substring):
            longest_this_loop.append(substring)
        
    if longest_this_loop != []:
        longest_substr = longest_this_loop

substring = s[0:len(s)]
if is_alphabetical_order(substring):
    longest_substr = []
    longest_substr.append(substring)

print("Longest substring in alphabetical order is:", longest_substr[0])

### Without dict

print("\n### Version 2.0 ###\n")

# i means "index"
def is_alphabetical_order(string):
    for i in range(len(string)):
        if (len(string) != 1 and ((i == 0 and string[0] > string[1]) or 
                (i != 0 and string[i-1] > string[i]))):
            return False
    return True

longest_substr = []
for len_substr in range(1, len(s)+1):
    longest_this_loop = []
    
    if len_substr == len(s) and is_alphabetical_order(s):
        longest_this_loop = [s]
    
    for word_index in range(len(s) - len_substr):
        substring = s[word_index:word_index+len_substr]
    
        if is_alphabetical_order(substring):
            longest_this_loop.append(substring)
    
    if longest_this_loop != []:
        longest_substr = longest_this_loop

print("Longest substring in alphabetical order is:", longest_substr[0])



print("\n### Version 2.1 ###\n")

