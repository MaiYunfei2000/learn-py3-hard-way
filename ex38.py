ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# 将字符串ten_things的每个单词拆分成一个个单独组块，变为表格，赋给变量stuff
stuff = ten_things.split(' ')
# 建立表格more_stuff，并输入一个个内容
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# 当stuff的元素数不等于10时
while len(stuff) != 10:
    # 取走表格more_stuff的最后一个元素作为字符串赋给变量next_one
    next_one = more_stuff.pop()
    # 打印字符串"Adding: "和变量next_one
    print("Adding: ", next_one)
    # 将变量next_one中的字符串赋给表格stuff，作为其最后一个元素
    stuff.append(next_one)
    # 打印："There are {表格stuff的元素数} items now."
    print(f"There are {len(stuff)} items now.")

# 打印字符串"There we go: "和表格stuff
print("There we go: ", stuff)

print("Let's do some things with stuff.")

# 打印表格stuff的第二个元素
print(stuff[1])
# 打印表格stuff的最后一个元素
print(stuff[-1])
# 所以pop是什么意思？
# 删除列表中给定位置的元素并返回它。如果没有给定位置，`a.pop()` 将会删除并返回列表中的最后一个元素。（ 方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。你会在 Python 参考库中经常看到这种表示方法)。
# https://docs.python.org/zh-cn/3/tutorial/datastructures.html?highlight=pop
print(stuff.pop())

# 什么意思？？？？记得去搜官方文档。
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!