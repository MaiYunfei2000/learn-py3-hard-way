# 继续深入练习.format。就当前的理解，此函数的功能是按照相应格式给{}赋值。

formatter = "{} {} {} {}"

# 取代码 formatter = "{} {} {} {}" 定义的字符串，并给format依次传递4个参数。
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# 嵌套中的嵌套！
print(formatter.format(
formatter, formatter, formatter, 
# 就算让参变量跳行，也不会跳行。
formatter))
# 字符串同理。
print(formatter.format(
    "Try you",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
    "我才不_(:з」∠)_"
))

# MYF的自由发挥时间↓
print()
print("那么我还可以试试：")
x = 5
x = x * x
print(formatter.format(formatter.format(1, 2, 3, 4), formatter, 3, x))
