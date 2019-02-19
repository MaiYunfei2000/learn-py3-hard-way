# 此练习

from sys import argv

script, input_file = argv

# 定义函数print_all()。
def print_all(f):
    # 读取f的文件
    print(f.read())

# 定义函数rewind()。
def rewind(f):
    # 把f变量对应的文件的读取倒回第0行？
    f.seek(0)

# 定义函数print_a_line()
def print_a_line(line_count, f):
    # 打印变量line_count和读取的文本的一行，并把“磁头”移到下一行。
    ## print(line_count, f.readline())
    # 如果你不想每打印一行，就多空一行的话：
    print(line_count, f.readline(), end="")

# 以只读模式打开input_file对应的文件，赋给current_file。
current_file = open(input_file)

print("First let's print the whole file:\n")

# 以current_file为参数运行函数print_all。
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# 以current_file为参数运行函数rewind。
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# x = x + y 等效于 x += y 。
current_line += 1
print_a_line(current_line , current_file)