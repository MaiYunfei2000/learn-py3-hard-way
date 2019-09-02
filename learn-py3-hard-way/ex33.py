# i的初始值为0
i = 0
# 建立空表格numbers
numbers = []

# 当i小于6时，进行以下循环：
while i < 6:
    print(f"At the top i is {i}")
    # 将当前的i值添加至列表末尾
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

# 将表格numbers中的元素一个个赋给num，一次次执行此语句
for num in numbers:
    print(num)