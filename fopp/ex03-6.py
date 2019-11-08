### 3.6.2 format()方法的格式控制(p.86)

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

# p.88