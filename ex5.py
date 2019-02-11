# 此练习教我学会了创建嵌入变量内容的**字符串**。原来所谓的**字符串**就是用双引号(")括起来的一些文本，例如："Hello world!"。

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are ususally {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
# 如果字符串开头没有"f"，那么嵌入的变量不会被打印，只会显出括号和变量名。例如：
# If I add {my_age}, {my_height}, and {my_weight} I get {total}.
# 如果有"f"，那么变量就会显示出来。例如：
# If I add 35, 74, and 180 I get 289.

# 为什么要安排巩固练习1？此练习的作用是什么？是假定初学者会漏改一些变量名从而使程序出错，训练他们的细心吗？或是告诉我们，变量名要选好不要轻易改，否则程序一大就是无限的灾难？

# 这可以起空一行的作用。
print()

# 以下是巩固练习2的内容。

# 单位转换。
# 相乘运算必须要有乘法运算符，不能像数学列式运算一样省去乘号。
height_cm = 2.54 * height
# 函数"round()"的作用是给数值四舍五入成整数。
weight_kg = round(0.45 * weight)

print("What if convert inches and lbs to centimeters and kilograms?")

# 为什么如果把height_cm这行代码放到此行的下一行，变量{height_cm}是蓝色的？并且怎么修改变量名都是这种情况，以及Python会提示“SyntaxError: invalid syntax”。然后挪到上方就没事了。

print(f"He's {height_cm} cm and {weight_kg} kg.")

# 这次终于漏输右括号而翻车了吧，哈哈哈。检查时要一个字一个字地从后往前扫，不仅仅是提示错误的那一行，更要继续往上一行去找。
# AC：if 提示print语法错误 then 查看括号是否齐全 假如有前后多行print连在一起，还得检查前面print的右括号是否漏打了。