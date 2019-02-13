# 此练习巩固ex11所学。并新学了在input函数的括号里键入字符串来达成提示别人应输入什么东西的效果。

print("input numbers only, or it will error. \n")
# 效果等同于：
# print("How old are you?", end=' ')
# age = input()
# 也就是用一行代码实现了两行代码的功能。
age = input("How old are you? ")
# 提示用户输入身高并取整，然后赋值给变量height。
height = int(input("How tall are you? (cm) "))
weight = input("How much do you weigh? (kg) ")

print(f"So, you're {age} old, {height} cm tall and {weight} kg heavy.")