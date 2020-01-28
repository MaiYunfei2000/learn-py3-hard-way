### 3.6.2 format()方法的格式控制(p.86)
# more: https://docs.python.org/zh-cn/3/library/string.html#format-string-syntax

s = "PYTHON"
print("{0:30}".format(s)) # 默认左对齐
print("{0:>30}".format(s)) # 右对齐
print("{0:>35}".format(s)) # 逼死强迫症
print("{0:^30}".format(s)) # 居中
print("{0:*^30}".format(s)) # 居中并使用“*”填充
print("{0:-^30}".format(s)) # 居中并使用“-”填充
# 并不能用别的任意字符填充

print()

print("{0:-^30}".format(1234567890))
print("{0:-^30,}".format(1234567890))
print("{0:-^30,}".format(12345.67890))
print("{0:.2f}".format(12345.67890)) # 注意此行的2f和下一行的3f
print("{0:H^20.3f}".format(12345.67890))
print("{0:.4}".format("PYTHON"))

print()

print("{0:b}, {0:c}, {0:d}, {0:o}, {0:x}, {0:X}".format(425))
# b：整数的二进制形式；c：整数对应的Unicode字符；d：整数的十进制方式；o：整数的八进制方式；x整数的小写十六进制方式；X：整数的大写十六进制方式

print("{0:e}, {0:E}, {0:f}, {0:%}".format(3.14))
# e：浮点数对应的小写字母e的指数形式；浮点数对应的大写字母E的指数形式；浮点数的标准浮点形式；浮点数的百分形式

print("{0:.2e}, {0:.2E}, {0:.2f}, {0:.2%}".format(3.14))
# .2：控制精度，设置小数部分宽度为2