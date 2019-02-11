# 通过此练习，我学习了通过 “变量名 = 值” 来建立一个变量并赋值，用变量运算，以及输出变量。

cars = 100 # 将值100赋给变量cars。
space_in_a_car = 4 # 去掉“.0”，average_passengers_per_car的输出值仍有小数；而carpool_capacity的输出值变为整数。
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.") # 逗号和引号后无论有无空格，输出的变量和值之间都会有空格。以及必须要有这个逗号。逗号前多加空格也不会有变化。但其他内容如数字、字母则不行。

# 知道为什么作者一直在说，在代码**上一行**作注释，而不是在本行代码后面吗？因为程序出错时，你的长长的注释也会出现在出错行，这样在终端里会显示不是一行字，这样你通过“^”标记寻找出错点就会很麻烦。

# 巩固练习：如果提示“'某某' is not define”，意思是之前并没有建立这个变量。
# SK：检查代码要倒着读。