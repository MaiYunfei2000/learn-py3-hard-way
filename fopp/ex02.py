# 练习教材中第二章的实例

print('\n\n实例2.1 温度转换：\n\n')

tempstr = input("请输入带有符号的温度值（符号在后）：")
if tempstr[-1] in ['F', 'f']:
    # [内置函数 — Python 3.7.4 文档](https://docs.python.org/zh-cn/3/library/functions.html?highlight=eval#eval)
    # eval函数的作用是将字符串作为代码来执行
    # 哦，这里读取到了数字，它自然就作为数值而存在了
    # 将华氏度转化为摄氏度的算法
    # tempstr[0:-1]的意义是字符串tempstr的从开头第一个（即第[0]个）字符到最后一个字符（[-1]）的区间
    C = (eval(tempstr[0:-1]) - 32)/1.8
    # {}里.2f的意义是取小数点后两位数
    print("转换后的温度是{:.2f}C".format(C))
elif tempstr[-1] in ['C', 'c']:
    F = 1.8*eval(tempstr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")

print('\n\n\n\n')