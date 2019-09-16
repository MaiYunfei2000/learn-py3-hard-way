# 参考：https://blog.csdn.net/christianashannon/article/details/78867204

import numpy as np

print("\n这是一个生成随机整数序列的小程序。\n")
filename = input("""
请输入写入对象的文件名。
如果不需要写入对象则输入0。
>>> """) # 或者干脆略过输入环节，把input直接变成文件名
start = int(input("请输入起始值："))
stop = int(input("请输入终止值："))
quantity = stop - start + 1
print(quantity)

array = np.arange(quantity)
array = array + start
np.random.shuffle(array)
print(array)

if filename == "0":
    exit(0)

target = open(filename, 'w+')
print(f"即将开始生成从{start}至{stop}的随机数列并写入目标文档。\n按 ENTER 开始。\n若要结束程序请按 CTRL-C 。")
input(">>> ")

array = f'{array}'

target.write(array)

target.close()