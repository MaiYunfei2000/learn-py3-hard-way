# 此练习中，学会了：
# 在终端中键入“echo "xxx" > xxx.xxx”来将字符串输入（覆盖）进某个文档。
# 在终端中键入“cat xxx.xxx”来查看某文件的内容。

# ...?
from sys import argv
# ...?
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# 以只读模式打开from_file对应名字的文件，赋给变量in_file。
## in_file = open(from_file)
# 读取in_file的内容，赋给变量indata。
## indata = in_file.read()
indata = open(from_file).read() # 

# 打印“输入的文件的字符长度为{嵌入：indata的字符长度}bytes。”
print(f"The input file is {len(indata)} bytes long")

# 打印“作为输出对象的文件存在吗？ {嵌入：函数：判断(变量to_file对应的文件)是否存在并返回是或否}
print(f"Does the output file exist? {exists(to_file)}")
# 巩固练习1：如果不想它询问，而是直接操作文件，则注释这两行代码。
## print("Ready, hit RETURN to continue, CTRL-C to abort.")
## input("> ")

# 以写入模式打开变量to_file对应名字的文件，赋给变量out_file。
out_file = open(to_file, 'w')
# 将变量indata写入变量out_file对应的文件。
out_file.write(indata)

# 关闭out_file和in_file对应的文件。
out_file.close()
## in_file.close()
open(from_file).close()

print("Alright, all done.")

# 巩固练习2、4未能解决。巩固练习5划水。