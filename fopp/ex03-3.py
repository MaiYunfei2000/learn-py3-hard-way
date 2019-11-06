# 3.3 math库的使用
# 教材69页开始

import math

def p(item):
    print(item)

# 数学常数

print(f"""
{math.pi}, # 圆周率
{math.e}, # 自然对数
{math.inf}, # 无穷
{math.nan}, # 非浮点数标记，NaN(Not a Number)
""")

# 数值表示函数

x = 3
y = 2
z = -1
p(math.fabs(z)) # 绝对值
p(math.fmod(x, y)) # x与y的模（x除以y的余数）
p(math.fsum([math.pi, math.e])) # 浮点数精确求和
p(math.ceil(math.e)) # 向上取整
p(math.floor(math.e)) # 向下取整
p(math.factorial(x)) # 阶乘
p(math.gcd(8, 12)) # 最大公约数
# p(math.frepx(x)) AttributeError: module 'math' has no attribute 'frepx'
p(math.ldexp(x, y)) # 运算：x*(2的y次方)
p(math.modf(math.pi)) # 返回小数和整数部分
p(math.trunc(math.pi)) # 返回整数部分
p(math.copysign(y, z)) # 用z的正负号替换y的正负号
p(math.isclose(x, y)) # 比较a和b的相似性
p(math.isfinite(math.pi)) # 是否为有限小数
p(math.isinf(-1)) # 是否为无穷大
p(math.isinf(math.inf))
p(math.isnan(math.nan)) # 是否为NaN

# 幂对数函数

# 三角运算函数

# 高等特殊函数
