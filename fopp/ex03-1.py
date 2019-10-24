# 3.1 数字类型

# 3.1.2 整数类型

## 整数类型的四种进制表示

print(0b101, 0B101) # 二进制
print(0o711, 0O711) # 八进制
print(0xABC, 0X66CCFF) # 十六进制

# 可是打印出来就变成二进制了？？

## 幂运算（不限于整数）

print(pow(2, 3)) # 2 raised to the power of 3

# 3.1.3 浮点数类型

print(3) # 这是整数
print(3.0) # 这是浮点数

# 标准库decimal提供了更精确的的数字类Decimal，可进行更高精度的运算   detailed: TB p.64

# 3.1.4 复数类型

print(1+2j) # 复数(1,2) 加j则代表此数为虚数，并且加j的部分为虚部

# About numeric types, more detailed information: [内置类型 — Python 3.8.0 文档](https://docs.python.org/zh-cn/3/library/stdtypes.html#numeric-types-int-float-complex)