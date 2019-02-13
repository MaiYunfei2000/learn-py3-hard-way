# 此练习中新学了函数：input()。

# 打印“How old are you?”，不跳行，用空格连上下一行的内容。
print("How old are you?", end=' ')
# 让用户输入一个值，并将这个值赋给变量age。
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")