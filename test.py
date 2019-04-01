# /Users/maiyunfei/Library/Mobile\ Documents/N39PJFAFEV\~com\~metaclassy\~byword/Documents/maiyunfei2000.com/file.maiyunfei2000.com/StudyIngredients/STAT/filp-coins/output.txt

# 这里有个字符“	”很有用

# 初始化
import random
i = 0
m = 0

print("这是一个模拟抛硬币的小程序。")
filename = input("请输入输出对象的文件名：") # 或者干脆略过输入环节，把input直接变成文件名
num = int(input("请输入抛硬币的次数："))
# ⚠️必须取整。input()返回的数据类型是str，不能直接和整数进行比较。不然会报错：TypeError: '<' not supported between instances of 'int' and 'str'

target = open(filename, 'w+')

print(f"即将开始生成{num}个随机数并写入目标文档，按 ENTER 开始。若要结束程序请按 CTRL-C 。")
input(">>> ")

while i < num:
    i = i + 1
    ran = random.randrange(2) # 返回[0,2)区间内的随机整数，赋给变量ran
    
    if ran == 1:
        m = m + 1
        
    p = round(m / i, 6) # 将 m/i 的值取6位小数赋给变量p
    print(f"{i}	{ran}	{m}	{p}")
    target.write(f"{i}	{ran}	{m}	{p}\n")

print(
"""
------------------------------------------------
完成。
请将文本文档中的数据复制到EXCEL表格中进一步分析。
------------------------------------------------
说明：
第一列是数据的累计个数，
第二列是随机生成的数字 0 或 1，
第三列是数字 1 的累计个数，
第四列是此时数字 1 所占全部数字的比值。
------------------------------------------------
""")

target.close()