# many practice about "string"

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

print('\n★ str.isspace()\n')
# Return true if there are only whitespace characters in the string and there is at least one character, false otherwise.
# A character is whitespace if in the Unicode character database (see unicodedata), either its general category is Zs (“Separator, space”), or its bidirectional class is one of WS, B, or S.

print(''.isspace())
print('maiyunfei2000 '.isspace())
print(' '.isspace())

print('\nstr.istitle()\n')
# Return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return false otherwise.

print('maiyunfei'.istitle())
print('2000'.istitle())
print('maiyunfei2000'.istitle())
print(' '.istitle())
print(''.istitle())
print('TEXT'.istitle())

# 🚧没搞懂

print('\n★ str.isupper()\n')

print('TEXT'.isupper())
print('Text'.isupper())
print('text'.isupper())
print(c.isupper())

print('\n★ str.join(iterable)\n')
# Return a string which is the concatenation of the strings in iterable. A TypeError will be raised if there are any non-string values in iterable, including bytes objects. The separator between elements is the string providing this method.

# 🚧没搞懂 以及iterable是什么意思？/代表什么？

print('\n★ ★ ★ str.ljust(width[, fillchar])\n')
# Return the string left justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).

print('maiyunfei2000'.ljust(0))
print('maiyunfei2000'.ljust(13)) # len('maiyunfei') = 13
print('maiyunfei2000'.ljust(14))
print('maiyunfei2000'.ljust(100))

# 🚧没搞懂

print('\n★ str.lower()\n')
# Return a copy of the string with all the cased characters converted to lowercase.

b = 'China'
c = 'ΑΒΓΔ'
print(b.casefold(), c.casefold())
print(b.lower(), c.lower())
# 🚧所以casefold()和lower()到底有什么区别？

print('\n★ str.lstrip([chars])\n')
# Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped:
'''
>>> '   spacious   '.lstrip()
'spacious   '
>>> 'www.example.com'.lstrip('cmowz.')
'example.com'
'''

print('maiyunfei'.lstrip('mai'))
print('maiyunfeimaiyunfei'.lstrip('mai'))
print('0 maiyunfei'.lstrip())
print('   0 maiyunfei'.lstrip())

print('\n★ str.maketrans(x[, y[, z]]')
# This static method returns a translation table usable for str.translate().
# If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters (strings of length 1) to Unicode ordinals, strings (of arbitrary lengths) or None. Character keys will then be converted to ordinals.
# If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

# 🚧没搞懂

print('\n★ str.partition(sep)\n')
# Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.

print('mai★yunfei'.partition('★'))
print('★maiyunfei'.partition('★'))

print('\n★ str.replace(old, new[, count])\n')
# Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

print('maiyunyun'.replace('yun', 'fei'))
print('maiyunyun'.replace('yun', 'fei', 1))
print('maiyunyun'.replace('yun', 'fei', 2))
print('maiyunyun'.replace('yun', 'fei', 3))
print('233a233a233a233a233'.replace('a', 'bbq', 3))

print('\n★ str.rfind([, start[, end]])\n')
# Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

print('maiyunfei'.rfind('mai'))
print('maiyunfeimai'.rfind('mai'))
print('maiyunfei'.rfind('fei'))
print('maiyunfei'.rfind('cai'))

print('\n★ str.rindex(sub[, start[, end]])\n')
# Like rfind() but raises ValueError when the substring sub is not found.

# 跳过

print('\n★ str.rjust(width[, fillchar])\n')
# Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s). 

# 🚧 不懂，略过

print('\n★ str.rpartition(sep)\n')
# Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.

print('mai★yunfei'.rpartition('★'))
print('★maiyunfei'.rpartition('★'))
print('maiyunfei'.rpartition('x'))

print('\n★ rsplit(sep=None, maxsplit=-1)\n')
# Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a separator. Except for splitting from the right, rsplit() behaves like split() which is described in detail below.

print('maiyunfei2000'.rsplit(sep='i'))
print('maiyunfei2000'.rsplit(sep=None))
print('maiyunfei2000'.rsplit(sep='i', maxsplit=-1))
print('maiyunfei2000'.rsplit(sep='i', maxsplit=-2))
print('maiyunfei2000'.rsplit(sep='i', maxsplit=1))

print('\n★ str.rstrip([chars])\n')
# Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:
'''
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'
'''

print('maiyunfei2000'.rstrip('mai'))
print('maiyunfei2000'.rstrip('fei'))
print('maiyunfei2000'.rstrip('2000'))
# 与lstrip()相反，是摘取后面露出来的字符串
print('maiyunfei2000'.rstrip('i'))

print('\n★ str.split(sep=None, maxsplit=-1)\n')
# Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
# If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].
# For example:
'''
>>> '1,2,3'.split(',')
['1', '2', '3']
>>> '1,2,3'.split(',', maxsplit=1)
['1', '2,3']
>>> '1,2,,3,'.split(',')
['1', '2', '', '3', '']
'''
# If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].
# For example:
'''
>>> '1 2 3'.split()
['1', '2', '3']
>>> '1 2 3'.split(maxsplit=1)
['1', '2 3']
>>> '   1   2   3   '.split()
['1', '2', '3']
'''

print('\n★ str.splitlines([keepends])\n')
# Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.

print("↓ print('asfasf\nasdfsadf\rdasfadf\r\nsafsdf')")
print('asfasf\nasdfsadf\rdasfadf\r\nsafsdf')
print('asfasf\nasdfsadf\rdasfadf\r\nsafsdf'.splitlines())
print('asfasf\nasdfsadf\rdasfadf\r\nsafsdf'.splitlines(keepends = True))
# 不明白keepends是什么，哦，“keep ends”——分割后保留末尾字符——的意思
# 与split的比较详见https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=str#str.split

print('\n★ str.startswith(prefix[, start[, end]])\n')
# Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.

print('maiyunfei'.startswith('mai'))
print('maiyunfei'.startswith('yun'))
print('maiyunfei'.startswith('fei', 5))
print('maiyunfei'.startswith('fei', 6))
print('maiyunfei'.startswith('fei', 6, 7))
print('maiyunfei'.startswith('fei', 6, 8))
print('maiyunfei'.startswith('fei', 6, 9))

# next: https://docs.python.org/3/library/stdtypes.html?highlight=str#str.strip