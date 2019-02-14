# 此练习中，新学了如何读取文件并将其内容赋给变量。

# 仍然不知道这行代码该怎么注释……
# 实际上完全可以不靠argv来读取文件。只要用到open()就可以了。
from sys import argv

# 将argv解包，将参数依次赋值给script和filename两个变量。
script, filename = argv

# 以变量filename被赋予的值为名称读取文件，然后把读取到的文件赋给变量txt（？）。
txt = open(filename)

# 打印嵌入变量filename的内容。
print(f"Here's your file {filename}:")
# 打印从变量txt读取到的内容。
print(txt.read())

# 就算说是again，也完全可以输入其它文件名。包括py、md等等，效果自己看。
print("Type the filename again:")
# 输入字符串，赋值给变量file_again（？）。
file_again = input("> ")

# 以变量filename被赋予的值为名称读取文件，把文件赋给变量txt_again（？）。
txt_again = open(file_again)

# 打印从变量txt_again读取到的内容。
print(txt_again.read())

# 这个练习其实都不是很会注释诶……
# 尚未弄清楚open()和.read()的机制。

# 拓展阅读：http://www.runoob.com/python3/python3-file-methods.html