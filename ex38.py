ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# 将字符串ten_things的每个单词拆分成一个个单独组块，变为 列表，赋给变量stuff
stuff = ten_things.split(' ')
# 建立 列表more_stuff，并输入一个个内容
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# 当stuff的元素数不等于10时
while len(stuff) != 10:
    # 取走 列表more_stuff的最后一个元素作为字符串赋给变量next_one
    next_one = more_stuff.pop()
    # 打印字符串"Adding: "和变量next_one
    print("Adding: ", next_one)
    # 将变量next_one中的字符串赋给 列表stuff，作为其最后一个元素
    stuff.append(next_one)
    # 打印："There are { 列表stuff的元素数} items now."
    print(f"There are {len(stuff)} items now.")

# 打印字符串"There we go: "和 列表stuff
print("There we go: ", stuff)

print("Let's do some things with stuff.")

# 打印 列表stuff的第二个元素
print(stuff[1])
# 打印 列表stuff的最后一个元素
print(stuff[-1])
# 打印 列表stuff的第一个元素
print(stuff[0])
# 所以pop是什么意思？
# list.pop([i])：删除列表中给定位置的元素并返回它。如果没有给定位置，`a.pop()` 将会删除并返回列表中的最后一个元素。（ 方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。你会在 Python 参考库中经常看到这种表示方法)。
# https://docs.python.org/zh-cn/3/tutorial/datastructures.html?highlight=pop
print(stuff.pop())

# join什么意思？？？？记得去搜官方文档。

# 用“ ”作为列表stuff里每一个元素之间的分隔，把这样处理后的字符串打印出来
print(' '.join(stuff)) 
print("# what? cool!")
# 用“#”作为列表中第**四**个元素和第**六**个元素之间的分隔，打印出第四个元素、用于分隔元素的字符串、第六个元素连在一起形成的字符串⚠️我猜错了！为什么3是Telephone（第四个元素）而5是Light（第五个元素）却不是第六个元素？难不成这是一个区间，先闭后开？
print('#'.join(stuff[3:5])) 
print("# super stellar!")
# str.join(iterable)：返回一个由 iterable 中的字符串拼接而成的字符串。 如果 iterable 中存在任何非字符串值包括 bytes 对象则会引发 TypeError。 调用该方法的字符串将作为元素之间的分隔。
# https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=join#str.join

print("那么我来自由发挥一下\n")
print("先来个更符合我们常识的“列表”")
print('\n'.join(stuff), "\n")

print("再来一个！")
print('###'.join(stuff[3:6]))

print("\nNice! 原来如此！")