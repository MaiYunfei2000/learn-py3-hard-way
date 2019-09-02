# 此热身是为了练习创建模块

# 调用模块 ex40mystuff
import ex40mystuff

# 创建字典mystuff。里面有一个叫作'apple'的**键**(key)，并赋值为"I AM APPLES!"。
mystuff = {'apple': "I AM APPLES!"}
# 打印字典mystuff里的键apple的值
print(mystuff['apple'])

# 运行模块ex40mystuff的函数apple()
ex40mystuff.apple()
# 打印模块ex40mystuff的变量tangerine
print(ex40mystuff.tangerine)

print("\n比较一下字典和模块：\n")

ex40mystuff['apple'] # get apple from dict
ex40mystuff.apple() # get apple from the module
ex40mystuff.tangerine # same thing, it's just a variable

# 吐槽：其实就是可以调用外部文件的代码，然后取了个“模块”的名字——叫着方便？= =