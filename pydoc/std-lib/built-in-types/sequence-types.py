##### Sequence Types -- list, tuple, range
##### 序列类型：列表，元组，range对象

##### https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

#### common sequence operations(https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

# This table lists the sequence operations sorted in ascending priority. In the table, s and t are sequences of the same type, n, i, j and k are integers and x is an arbitrary object that meets any type and value restrictions imposed by s.

# The in and not in operations have the same priorities as the comparison operations. The + (concatenation) and * (repetition) operations have the same priority as the corresponding numeric operations. 

x = 0
y = 'b'
s = [0, 2, 4, 2, 'a', 'c', 'fff']
n = 3

# x in s: True if an item of s is equal to x, else False

print(x in s, y in s)

# x not in s: False if an item of s is equal to x, else True

print(x not in s, y not in s)

# s * n or n * s: equivalent to adding s to itself n times

print(s * n, n * s)

# s[i]: *i*th item of s, origin 0

print(s[0], s[5])

# s[i:j]: slice of s from i to j

print(s[1:4])

# s[i:j:k]: slice of s from i to j with step k

print(s[0:5:1])
print(s[0:5:2])

# len(s): length of s

print(len(s))

t = [0, 2, 4, 999, 888]

# min(s): smallest item of s

print(min(t))
# 所有元素必须为数

# max(s): largest item of s

print(max(t))

# s.index(x[, i[, j]]): index of the first occurrence of x in s(at or after index i and before index j)

print(s.index(2))
print(s.index(2, 2))
print(s.index(2, 3))
print(s.index('c', 3, 6)) # 如果找不到的话不会返回False而是直接报错，e.g. ValueError: 4 is not in list

# s.count(x): total number of occurences of x in s

print(s.count(2))
print(s.count('fff'))

# notes: 
# 1.While the in and not in operations are used only for simple containment testing in the general case, some specialised sequences (such as str, bytes and bytearray) also use them for subsequence testing:
print("gg" in "eggs")
# 2.Values of n less than 0 are treated as 0 (which yields an empty sequence of the same type as s). Note that items in the sequence s are not copied; they are referenced multiple times. This often haunts new Python programmers; consider:
lists = [[]] * 3
print(lists)
print(lists[0])
lists[0].append(3)
print(lists)
lists.append(222)
print(lists)
lists[0].append(999)
print(lists)

#### Mutable Sequence Types 可变序列类型

# https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types

# The operations in the following table are defined on mutable sequence types. The collections.abc.MutableSequence ABC is provided to make it easier to correctly implement these operations on custom sequence types.
# In the table s is an instance of a mutable sequence type, t is any iterable object and x is an arbitrary object that meets any type and value restrictions imposed by s (for example, bytearray only accepts integers that meet the value restriction 0 <= x <= 255).

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 2
j = 7
x = 233
t = [22, 33, 44, 55, 66]

print("\nprint s: \n", s)
print(len(s))

# item i of s is replaced by x
s[i] = x
print(s)
print(len(s))

# slice of s from i to j is replaced by the contents of the iterable t
s[i:j] = t # 如果列表t多加了一个数，接下来一坨代码执行后会发生什么？
print(s)
print(len(s))

# same as s[i:j] = []
del s[i:j]
print(s)
print(len(s))

#

#

# try more
'''
string = 'abcdeeffffgh'
string[5] = 'x'
print(string)

报错：TypeError: 'str' object does not support item assignment
'''