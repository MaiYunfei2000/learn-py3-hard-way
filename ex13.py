# 此练习中新接触了argv这个参数变量（argument variable）。并把argv解包，依次赋值给四个变量。
# sys是一种模块（module），但目前没能搞明白它到底是个什么东西。这行代码整行都搞不明白。
from sys import argv
# read this WYSS section for how to run this
script, first, second, third = argv

print('The script is called:', script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# 在变量的值为字符串的情况下：
# 用加号连接，打印出来的多个变量是连在一起的。
print(first + second + third)
# 用逗号连接，打印出来的多个变量之间有空格。
print(first, second, third)