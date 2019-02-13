#此练习巩固上个练习中学到的argv。并学会了用更机智轻松的方法设置提示语。

from sys import argv

script, user_name = argv

# 将字符串“> ”赋值给变量prompt。这样的好处就是后续不需要重复输入提示语了，（然而这里很蠢的是，作者使用的字符串比变量名还短四个字符……）以及要改提示语的话只用改此处变量的赋值，而不用在后面一个一个改。
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")