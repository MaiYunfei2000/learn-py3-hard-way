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

def stdtest(a):
    print(a)
    print(type(a))
    print('✨')

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

s = list(range(25))
i = 2
j = 7
k = 2
n = 3
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

print(t)
u = t
print("\nu: \n", u)
del u[3:5]
print("\nt: \n", t) # 为什么t也被删了两个？
print("\nu: \n", u)

# the elements of s[i:j:k] are replaced by those of t
# s[i:j:k]与t必须有相同个数的元素，否则会报错：ValueError: attempt to assign sequence of size 5 to extended slice of size 3
s[i:j:k] = u
print(s)

# removes the elements of s[i:j:k] from the list

del s[i:j:k]
print(s)

# appends x to the end of the sequence (same as s[len(s):len(s)] = [x])

s.append(x)

# removes all items from s (same as del s[:])

s.clear()

# creates a shallow copy (浅拷贝) of s (same as s[:])
# 搜索之后没能一下子明白「浅拷贝」是什么意思，先放着

s = list(range(25))
print("\ns: \n", s)
c = s.copy()
print("\nc: \n", c)

# extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t)

s.extend(t)
print(s)
# also:
s += t
print(s)

# updates s with its contents repeated n times

s *= n
print(s)

# inserts x into s at the index given by i (same as s[i:i] = [x])
s.insert(i, x)
print(s)
#s.insert([i:3], [233, 332]) 额果然这样做是不行的呀
#print(s)

# retrieves the item at i and also removes it from s
m = s.pop(i)
print(m)
print(s)

x = 44
# remove the first item from s where s[i] is equal to x
s.remove(x)
print(s)

# reverses the items of s in place
s.reverse()
print(s)

'''
Notes:

1. t must have the same length as the slice it is replacing.

2. The optional argument i defaults to -1, so that by default the last item is removed and returned.

3. remove() raises ValueError when x is not found in s.

4. The reverse() method modifies the sequence in place for economy of space when reversing a large sequence. To remind users that it operates by side effect, it does not return the reversed sequence.

5. clear() and copy() are included for consistency with the interfaces of mutable containers that don’t support slicing operations (such as dict and set). copy() is not part of the collections.abc.MutableSequence ABC, but most concrete mutable sequence classes provide it.

New in version 3.3: clear() and copy() methods.

6. The value n is an integer, or an object implementing __index__(). Zero and negative values of n clear the sequence. Items in the sequence are not copied; they are referenced multiple times, as explained for s * n under Common Sequence Operations.
'''

# try more
'''
string = 'abcdeeffffgh'
string[5] = 'x'
print(string)

报错：TypeError: 'str' object does not support item assignment
'''

#### Lists
# https://docs.python.org/3/library/stdtypes.html#lists

# Lists are mutable sequences, typically used to store collections of homogeneous items (where the precise degree of similarity will vary by application).

# class list([iterable])
"""
Lists may be constructed in several ways:

Using a pair of square brackets to denote the empty list: []

Using square brackets, separating items with commas: [a], [a, b, c]

Using a list comprehension: [x for x in iterable]

Using the type constructor: list() or list(iterable)
"""

example1 = []
print(example1)
example2 = ['a', 'b', 'c']
print(example2)
a,b,c = 1,2,3
# Using a list comprehension (使用列表推导式)
example3 = ['x' for a in [a, b, c]]
example33 = [[a,b] for a in [a, b, c]] # 没明白
print(example3)
print(example33)
print([[b,a] for a in [a, b, c]])
print([[a,b] for c in [a, b, c]]) # 还是没明白……
example4 = list(range(10))
print(example4)
example5 = list('maiyunfei2000')
print(example5)
# example5 = list(iterable?)

#### Tuple (元组)
# https://docs.python.org/3/library/stdtypes.html#tuples
# https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tuples-and-sequences

"""
class tuple([iterable])

Tuples may be constructed in a number of ways:

- Using a pair of parentheses to denote the empty tuple: ()
- Using a trailing comma for a singleton tuple: a, or (a,)
- Separating items with commas: a, b, c or (a, b, c)
- Using the tuple() built-in: tuple() or tuple(iterable)
"""

# 最大的区别就是元组里的元素自元组生成后不可改变

d = ()
stdtest(d)
e = ('a',)
stdtest(e)
f = ('233', '22', '33')
stdtest(f)
g = tuple(['233', '22', '33'])
stdtest(g)

#### Range
# https://docs.python.org/3/library/stdtypes.html#ranges