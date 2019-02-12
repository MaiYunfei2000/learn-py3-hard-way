# 此练习新学了在一个字符串中让文字换行，以及打印多行的字符串。

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
# \n 能让字符串换行。注意是 \n 不是 n\ 也不是/n 哦！！！
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

# 打印多行字符串。从 """ 后开始就生效了，如果 """ 后面不填字符，则会空出一行。
print("""
There's something going on here.
Withe the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")