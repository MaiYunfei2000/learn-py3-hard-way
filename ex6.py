types_of_people = 10
x = f"There are {types_of_people} types of people."

# 赋予给变量的值可以是字符串。
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# 嵌套中的嵌套。
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "False"
# 这个空的“{}”是什么鬼？
# 如果破坏掉print(joke_evaluation.format(hilarious))，那么这一行代码就会失效。
joke_evaluation = "Isn't that joke so fuuny?! {}"
# 吐槽：BTW，我看不懂这个冷笑话……还是说，这里我连"joke"都理解错了。

# 此行代码的作用目前还是搞不懂。
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# 加号可以使两个值为字符串的变量连在一起。但是，“为什么”（巩固练习4）？我答不出来。
print(w + e)

# 答巩固练习4：有6处吧？？textmate直接帮我把嵌套的变量上色了。