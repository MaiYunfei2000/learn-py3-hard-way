# 仍不会注释这一行……
from sys import argv

# 解包参数，依次赋值给两个变量。
script, filename = argv

# 打印：我们将擦除{相应文件名}。
print(f"We're going to erase {filename}.")
# 所以，按下了^C，到底发生了什么呢？是什么设定了会发生这样的事情？
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# 以filename的变量值为名，以写入模式访问对应文件，赋给变量target。
# r为只读(read)模式，w为写入(write)模式，a为追加(append)模式。不输入参数默认为r。
# 「追加」是个什么意思？
## target = open(filename, 'w')
# 下一行为巩固练习2的typeB，若启用，则禁用上一行代码；反之。
target = open(filename, 'r+') # r+或w+都行。

print("Truncating the file. Goodbye!")
# 清除target对应文件的内容。
target.truncate()

print("Now I'm going to ask you for three lines.")

# 将输入的字符串赋给变量line1。
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# 将变量line1的值写入变量target对应的文件。
## target.write(line1)
# 将换行写入变量target对应的文件。
## target.write("\n")
## target.write(line2)
## target.write("\n")
## target.write(line3)
## target.write("\n")

## print("And finally, we close it.")
# 关闭变量target对应的文件。
## target.close()
# 以下，巩固练习3。运作以下代码则需让上面八行代码（不包括注释）失效；反之。
# 前面那六行通过write写入的数据会被下一行代码的写入覆盖掉，所以即便不禁用那六行代码也不影响结果。
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print() # 空一行。

# 以上，巩固练习3；以下，巩固练习2。
# 运作巩固练习2的部分需要将前面的“target.close()”失效。
# 以只读模式（重新）访问文件。
## target = open(filename)
print("现在来看看修改过后的文件内容吧~")
print(target.read())
print("然后把文件关闭~这是一个很重要很重要很重要的习惯！")
target.close()
# 必须要养成关闭文件的习惯。现在只是个小小文件，还没有什么问题。以后文件一大，可能会使程序崩溃或是发生泄漏。
# 额，如果没有巩固练习2的第一行代码，会提示“io.UnsupportedOperation: not readable”。
# 还有一种解决方法：使用'r+'、'w+'可以把文件用同时读写的方式打开。

# 巩固练习4未能解决。

# 发现一个问题。清除文件内容后，仍会留下一行空行。然后写入文件会新建一行然后放上内容。这就使得文件结尾总是会有一行空行。