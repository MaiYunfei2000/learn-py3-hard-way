# 3.5.1

name = "Python语言程序设计"
print(name[0], name[7], name[11], name[2:-4], name[:6], name[6:], name[:], sep='\n')
'''依次为：
第1个：P
第8个：言
第12个：计
第3至倒数第4个（不包含倒数第4个）：thon语言
从头至第7个（不包含第7个）：Python
从第7个至结尾：语言程序设计
全部：Python语言程序设计
'''

# 3.5.2

# break: 不如从https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=str#text-sequence-type-str或https://docs.python.org/3/library/stdtypes.html?highlight=str#text-sequence-type-str开始，联系完所有的代码，然后再回课本康康

print('\nstr.capitalize()\n')
# Return a copy of the string with its first character capitalized and the rest lowercased.

a = 'apple'
print(a.capitalize())
print('apple'.capitalize())
# print(capitalize(a)) is wrong usage

print('\nstr.casefold()\n')
# Return a casefolded copy of the string.

b = 'China'
c = 'ΑΒΓΔ'
print(b.casefold(), c.casefold())

print('\nstr.center(width[, fillchar])\n')
# Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).

test = 'test aaa bbb ccc'
print(test.center(15,"c"))
# 🚧怎么捣鼓都没高明白干啥用的……

print('\nstr.count(sub[, start[, end]])\n')
# Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

t = 't'
print(test.count('t'))
print(test.count('test'))
print(test.count('test', 0, 4))
print(test.count('test', 4))
# 哦，要有end的话前面必须有start

print('\nstr.encode(encoding="utf-8", errors="strict")\n')

print(test.encode())# 输出了“b'test aaa bbb ccc'”是什么意思？
print('b'.encode())
# 🚧没搞懂

print('\nstr.endswith(suffix[, start[, end]])\n')
# Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position.
print(test.endswith('c'))
print(test.endswith('ccc'))
print(test.endswith('ccb'))
print(test.endswith('t', 4))
print(test.endswith('t', 0, 4))

print('\nstr.expandtabs(tabsize=8)\n')

d = 'test\ttesttest\ttesttesttest\t'
e = 'test\rtesttest\rtesttesttest\r'

print(d)
print(d.expandtabs(4))
print(d.expandtabs(8))
print(d.expandtabs(16))
print(d.expandtabs())
print(d.expandtabs(4))
'''打印结果都是：
test	testtest	testtesttest
test    testtest    testtesttest
test    testtest        testtesttest
test            testtest        testtesttest
'''
# 🚧没搞懂

print('\nstr.find(sub[, start[, end]])\n')
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

print(test.find('ccc')) # 返回的是13（而第一个c是第14个字符）
print(test.find('c', 13)) # 返回13
print(test.find('c', 14)) # 返回14
print(test.find('test')) # 返回0即首位

# 暂停
# 190923 1620 进度条：下一步：https://docs.python.org/3/library/stdtypes.html?highlight=str#str.format