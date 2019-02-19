# 定义函数cheese_and_crackers，它有两个参数：cheese_count和boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# 我们可以直接把值赋给函数的参数。
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# 或者，我们可以使用脚本中的变量。
print("OR, We can use variables from our script:")
## amount_of_cheese = 10
cheese_count = 10
amount_of_crackers = 50

## cheese_and_crackers(amount_of_cheese, amount_of_crackers)
cheese_and_crackers(cheese_count, amount_of_crackers)

# 我们甚至还可以在里面做数学运算。
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# 以及，还可以把上述两种用在一起。
print("And we can combine the two, variables and math:")
# 运行函数，参数cheese_count的值为变量amount_of_cheese与100的和，参数boxes_of_crackers的值为变量amout_of_crackers与1000的和。
## cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
cheese_and_crackers(cheese_count + 100, amount_of_crackers + 1000)

# 你看，函数定义里的参变量和脚本中的变量的名字重复了没所谓。

# 巩固练习3：自己编写至少一个函数出来，然后用10种不同的方式运行这个函数。

from sys import argv

filename, argument = argv

def function(x):
    print(f"你可真是{x}哦。")

function(argument)

function(input("> 请用形容一下你自己："))

# 我……