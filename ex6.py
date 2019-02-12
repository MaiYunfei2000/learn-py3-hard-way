# 在此练习中进一步巩固了ex5所学的f-string。新接触了.format函数。并学习了用print语句跟踪变量。

# 变量types_of_people赋值为10。
types_of_people = 10
x = f"There are {types_of_people} types of people."

# 赋予给变量的值可以是字符串。
# 变量binary赋值为“binary”。
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
# 删去下一行代码的井号和空格，则下一行代码变成调试(debug)代码。其含义是用print语句追踪变量y。
# print(">>> after assigning y", y)

# 打印变量x。
print(x)
# 删去下一行代码的井号和空格，则下一行代码变成调试代码。
# print(">>> bofore printing y", y)
print(y)

# 嵌套中的嵌套。
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "False"
# 如果破坏掉print(joke_evaluation.format(hilarious))，那么这一行代码就会失效。
joke_evaluation = "Isn't that joke so fuuny?! {}"

# 打印变量joke_evaluation，把变量hilarious的值赋给花括号。
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# 加号可以使两个值为字符串的变量连在一起。但是，“为什么”（巩固练习4）？我答不出来。
print(w + e)

# 答巩固练习4：有6处吧？？textmate直接帮我把嵌套的变量上色了。

# 作注释要简短一行搞定。

# 不要盯着代码看，仿佛想一下就会弄明白某段代码的作用一样。要动手破坏和调试代码。