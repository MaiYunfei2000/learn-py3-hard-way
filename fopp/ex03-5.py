# many kinds of practice about "string"

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

print('\n★ str.capitalize()\n')
# Return a copy of the string with its first character capitalized and the rest lowercased.

a = 'apple'
print(a.capitalize())
print('apple'.capitalize())
# print(capitalize(a)) is wrong usage

print('\n★ str.casefold()\n')
# Return a casefolded copy of the string.

b = 'China'
c = 'ΑΒΓΔ'
print(b.casefold(), c.casefold())

print('\n★ str.center(width[, fillchar])\n')
# Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).

test = 'test aaa bbb ccc'
print(test.center(15,"c"))
# 🚧怎么捣鼓都没高明白干啥用的……

print('\n★ str.count(sub[, start[, end]])\n')
# Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

t = 't'
print(test.count('t'))
print(test.count('test'))
print(test.count('test', 0, 4))
print(test.count('test', 4))
# 哦，要有end的话前面必须有start

print('\n★ str.encode(encoding="utf-8", errors="strict")\n')

print(test.encode())# 输出了“b'test aaa bbb ccc'”是什么意思？
print('b'.encode())
# 🚧没搞懂

print('\n★ str.endswith(suffix[, start[, end]])\n')
# Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position.
print(test.endswith('c'))
print(test.endswith('ccc'))
print(test.endswith('ccb'))
print(test.endswith('t', 4))
print(test.endswith('t', 0, 4))

print('\n★ str.expandtabs(tabsize=8)\n')

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

print('\n★ str.find(sub[, start[, end]])\n')
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

print(test.find('ccc')) # 返回的是13（而第一个c是第14个字符）
print(test.find('c', 13)) # 返回13
print(test.find('c', 14)) # 返回14
print(test.find('test')) # 返回0即首位

print('\n★ str.format(*args, **kwargs)\n')
# Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.

a = 1
b = 2
print('The sum of 1 + 2 is {}'.format(a+b))
print('The sum of {} + {} is {}'.format(a, b, a+b))

print('\n★ str.format_map(mapping)\n')
# Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict. This is useful if for example mapping is a dict subclass:

class Default(dict):
    def __missing__(self, key):
        return key

print('{name} was born in {country}'.format_map(Default(name='Guido')))

# 🚧没搞懂

print('\n★ str.index(sub[, start[, end]])\n')
# Like find(), but raise ValueError when the substring is not found.

print(test.find('test'))
print(test.index('test'))
print(test.find('tet'))
# print(test.index('tet'))

print('\n★ str.isalnum()\n')
# Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise. A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().

print('maiyunfei'.isalnum())
print('2000'.isalnum())
print('maiyunfei2000'.isalnum())
print('maiyunfei008!'.isalnum())
print(''.isalnum())

print('\n★ isalpha()\n')
# Return true if all characters in the string are alphabetic and there is at least one character, false otherwise. Alphabetic characters are those characters defined in the Unicode character database as “Letter”, i.e., those with general category property being one of “Lm”, “Lt”, “Lu”, “Ll”, or “Lo”. Note that this is different from the “Alphabetic” property defined in the Unicode Standard.

print('maiyunfei'.isalpha())
print('2000'.isalpha())
print('maiyunfei2000'.isalpha())
print('maiyunfei008!'.isalpha())
print(''.isalpha())

print('\n★ str.isascii()\n')
# Return true if the string is empty or all characters in the string are ASCII, false otherwise. ASCII characters have code points in the range U+0000-U+007F.

# print('maiyunfei'.isascii()) 
# print('2000'.isascii())
# print('maiyunfei2000'.isascii())
# print('maiyunfei008!'.isascii())
# print('★'.isascii())
# print('✨'.isascii())
# print(''.isascii())
# AttributeError: 'str' object has no attribute 'isascii'

# 没搞懂🚧

# next https://docs.python.org/3/library/stdtypes.html?highlight=str#str.isdecimal

print('\n★ str.isdecimal()\n')
# Return true if all characters in the string are decimal characters and there is at least one character, false otherwise. Decimal characters are those that can be used to form numbers in base 10, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Formally a decimal character is a character in the Unicode General Category “Nd”.

print('2000'.isdecimal())
print('2000.0'.isdecimal())
print('2000.1'.isdecimal())
print('maiyunfei2000'.isdecimal())
print(''.isdecimal())

print('\n★ str.isdigit()\n')
# Return true if all characters in the string are digits and there is at least one character, false otherwise. Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits. This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.

print('2000'.isdigit())
print('66ccff'.isdigit())
print('2000.0'.isdigit())
print('2000.1'.isdigit())
print('maiyunfei2000'.isdigit())
print(''.isdigit())

print('\n★ str.isidentifier()\n')
# Return true if the string is a valid identifier according to the language definition, section Identifiers and keywords.

# 🚧跳过

print('\n★ str.islower()\n')
# Return true if all cased characters in the string are lowercase and there is at least one cased character, false otherwise.

print(''.islower())
print('2000'.islower())
print('maiyunfei2000'.islower())
print('maiyunfei'.islower())
print('Maiyunfei'.islower())

print('\n★ str.isnumeric()\n')
# Return true if all characters in the string are numeric characters, and there is at least one character, false otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH. Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.

print(''.isnumeric())
print('ONE FIFTH'.isnumeric())
print('U+2155'.isnumeric())
print('1/5'.isnumeric())
print('0.2'.isnumeric())
print('2333'.isnumeric())
print('maiyunfei2000'.isnumeric())

print('\n★ str.isprintable()\n')
# Return true if all characters in the string are printable or the string is empty, false otherwise. Nonprintable characters are those characters defined in the Unicode character database as “Other” or “Separator”, excepting the ASCII space (0x20) which is considered printable. (Note that printable characters in this context are those which should not be escaped when repr() is invoked on a string. It has no bearing on the handling of strings written to sys.stdout or sys.stderr.)

# 🚧跳过