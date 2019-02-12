# 通过此练习巩固了习题6，并新学了重复生成字符串、合并打印多个赋值为字符串的变量。

# Why this file can't add Chinese annotation?
# For example, If I place some CN characters in line 1, it will said:
# SyntaxError: Non-ASCII character '\xe4' in file ex7.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
# 哦我明白了，在命令行里测试时，只打了“python”没打“3.6”。
# 那我的电脑里还有一个比较旧的Python？是的，18年7月按照阳老师博客配置电脑时，用brew cask install安装了python，那里的貌似是第2版

print("Mary had a little lamb.")
# 目前看来，.format就像是f-string的另一个版本。
# 「格式化」到底是什么意思呢？
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.") # "还有玛丽去的每一个地方。"?
print("." * 10) # What'd that do? 重复生成字符串。

# 好蠢啊恍恍惚惚……
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# Yummy，真香！

# watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# 若移除“, end=' '”，Cheese和Burger会在不同行。若移除单引号里的空格，那么Cheese和Burger之间没有空格间隔开来。说明，此代码的作用是不让print跳行显示结果，并用制定的字符串来链接两行print的内容。

# 打印变量end7和end8和end9……和end12。
print(end7 + end8 + end9 + end10 + end11 + end12)