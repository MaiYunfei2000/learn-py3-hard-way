# 此练习中新学了自定义函数。函数可以理解为被命名的代码段，可以接收参数。类比open(xxx, 'x')。
# 定义一个函数：
#   def 函数名字(参数)
#       想实现的功能，嵌有参数。

# this one is like your scripts with argv
# 定义函数print_two()
def print_two(*args):
    # 参数args解包为两个参数。（是这样理解吗？）
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
# 定义函数print_none()
def print_none():
    # 这个函数的功能是：打印“I got nothin'.”
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# 巩固练习

# 定义函数时的注意事项：
#   1.函数定义以def开始
#   2.函数名只由字符和下划线组成
#   3.函数名后紧跟着括号
#   4.括号里若包含多个参数，以逗号隔开
#   5.参数名称不可重复
#   6.紧跟着参数的是括号和冒号
#   7.紧跟着函数定义的代码使用**4个空格（或tab）**的缩进，不可多不可少
#   8.函数结束的位置取消缩进

# 调用/使用/运行函数时的注意事项
#   1.调用函数时使用函数名
#   2.函数名紧跟着左括号
#   3.括号内放入想要的值，并以逗号隔开
#   4.函数调用以右括号结尾