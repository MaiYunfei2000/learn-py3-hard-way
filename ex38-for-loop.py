# 附加练习：使用for循环代替原本的代码的while循环

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# ✨用for循环可以实现完全相同的输出结果，只是要多加一行代码，把stuff的长度赋给一个变量——for循环只能用变量不可以用函数，否则会提示 SyntaxError: can't assign to function call

a = len(stuff)

# for a in range(0,10): # 会怎么样？详见附录。
for a in range(6,10): # 会怎么样？
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff[0])
print(stuff.pop())

print(' '.join(stuff)) 
print("# what? cool!")
print('#'.join(stuff[3:5])) 
print("# super stellar!")
# https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=join#str.join

print("那么我来自由发挥一下\n")
print("先来个更符合我们常识的“列表”")
print('\n'.join(stuff), "\n")

print("再来一个！")
print('###'.join(stuff[3:6]))

print("\nNice! 原来如此！")

# 附录 乱来的后果如下⬇️：它从0开始加到10，那么原有列表的元素数量不够了然后就GG了

"""
Adding:  Boy
There are 7 items now.
Adding:  Girl
There are 8 items now.
Adding:  Banana
There are 9 items now.
Adding:  Corn
There are 10 items now.
Adding:  Frisbee
There are 11 items now.
Adding:  Song
There are 12 items now.
Adding:  Night
There are 13 items now.
Adding:  Day
There are 14 items now.
Traceback (most recent call last):
  File "ex38-for-loop.py", line 16, in <module>
    next_one = more_stuff.pop()
IndexError: pop from empty list
Ms-MacBook-Pro:trail-learn-py maiyunfei$
"""