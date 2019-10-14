# 此练习巩固ex9的内容，并新学了使用反斜杠转义特定字符。

# ↓此处为自由发挥。
# 反斜杠“\”可以将难录入的字符放到字符串里。
# 例如这个代码：
# x = "A man called "Mai Yunfei" is coding."
# 显然这段代码会出错，因为把Mai Yunfei括起来的括号被认为是字符串的边界了。
# 那么你可以这样：
x = "A man called \"Mai Yunfei\" is coding."
print(x)
# 反斜杠将双引号「转义」了。这是一个「转义序列」(escape sequence)
# ↑以上。

# \t 能将后面的字符串缩进。也就是起到平时在输入文本时按“Tab”键的效果。

# 翻译：我被缩进了。
tabby_cat = "\tI'm tabbed in."
# 翻译：I'm split on a line.→我被分成两半了。
persian_cat = "I'm split\non a line."
# 前一个反斜杠转义了后一个反斜杠，使其无效。
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# 以下是Python支持的所有转义序列：
# \\ 反斜杠“\”
# \' 单引号
# \" 双引号
# \a ASCII响铃符（BEL）
# \b ASCII退格符（BS）
# \N{name} Unicode数据库中的字符名，其中name是它的名字，仅Unicode适用
# \r ASCII回车符（CR）
# \t ASCII水平制表符（TAB）
# \uxxxx 值为16位十六进制值xxxx的字符
# \Uxxxxxxxx 值为32位十六进制值xxxxxxxx的字符
# \v ASCII垂直制表符（VT）
# \ooo 值为八进制值ooo的字符
# \xhh 职位十六进制值hh的字符