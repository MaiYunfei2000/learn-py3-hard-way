# 此练习巩固ex11所学。并新学了在input函数的括号里键入字符串来达成提示别人应输入什么东西的效果。
print("How old are you?", input())
# 效果等同于：
# print("How old are you?", end=' ')
# age = input()
# 也就是用一行代码实现了两行代码的功能。
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")