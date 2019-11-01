##### numeric-types （数字类型）

# https://docs.python.org/zh-cn/3/library/stdtypes.html#numeric-types-int-float-complex

#### int

#### float

#### complex

# Complex numbers have a real and imaginary part, which are each a floating point number. To extract these parts from a complex number z, use z.real and z.imag. (The standard library includes the additional numeric types fractions.Fraction, for rationals, and decimal.Decimal, for floating-point numbers with user-definable precision.)

complexa = (1+2j)

print(f'虚数{complexa}的实部为{complexa.real}，虚部为{complexa.imag}')

# ------------------------------------

# 001 The constructors int(), float(), and complex() can be used to produce numbers of a specific type.

a = '12'
print(int(a)) # 转换为整数
print(float(int(a))) # 转换为浮点数
print(complex(float(int(a)))) # 转换为复数

# 002 operations

print(2 // 3)
print(3 // 2) # x // y: floored quotient of x and y
print(3 % 2) # x % y: remainder of x / y
print(abs(-1)) # abs(x): absolute value or magnitude of x. see more: [abs()](https://docs.python.org/3/library/functions.html#abs)
print(complex(1,2)) # complex(re, im): a complex number with real part re, imaginary part im. im defaults to zero. see more: [complex()](https://docs.python.org/3/library/functions.html#complex)
print(complex(1,2).conjugate())# c.conjugate(): conjugate of the complex number c（求复数c的共轭复数）
print(divmod(3,2)) # divmod(x, y): the pair (x // y, x % y). see more: [divmod()](https://docs.python.org/3/library/functions.html#divmod)
print(pow(2,3)) # pow(x, y): x to the power y. see more: [pow()](https://docs.python.org/3/library/functions.html#pow)
print(2 ** 3) # x ** y: x to the power y

# 003

# All numbers.Real(https://docs.python.org/3/library/numbers.html#numbers.Real) types (int and float) also include the following operations:

# math.trunc(x): x truncated to Integral https://docs.python.org/3/library/math.html#math.trunc
import math

print(math.trunc(5.4))
print(math.trunc(5.5))
print(math.trunc(5.6))
print()
# round(x[, n]): x rounded to n digits, rounding half to even. If n is omitted, it defaults to 0. https://docs.python.org/3/library/functions.html#round
print(round(5.4))
print(round(5.5))
print(round(5.6))
print(round(5.55, 1))
print(round(5.55, -1))
print(round(5.55, -2))
print()
# math.floor(x): the greatest Integral <= x https://docs.python.org/3/library/math.html#math.floor
print(math.floor(5.5))
print()
# math.ceil(x): the least Integral >= x https://docs.python.org/3/library/math.html#math.ceil
print(math.ceil(5.5))
print()

# For additional numeric operations see the math(https://docs.python.org/3/library/math.html#module-math) and cmath(https://docs.python.org/3/library/cmath.html#module-cmath) modules.

# 004 Bitwise Operations on Integer Types（整数类型的按位运算） https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types

## [位操作 - Wikipedia](https://zh.wikipedia.org/wiki/%E4%BD%8D%E6%93%8D%E4%BD%9C)大概理解这个就好了，先跳过，以后再回来

# 005 https://docs.python.org/3/library/stdtypes.html#additional-methods-on-integer-types

# 跳过

# 006 Additional Methods on Float https://docs.python.org/3/library/stdtypes.html#additional-methods-on-float

print("\nfloat.as_integer_ratio()\n")
# Return a pair of integers whose ratio is exactly equal to the original float and with a positive denominator. Raises OverflowError on infinities and a ValueError on NaNs.

print(2.2.as_integer_ratio())
print(0.04.as_integer_ratio())
print(0.5.as_integer_ratio())
print(6.0.as_integer_ratio())
# 这里必须是浮点数6.0而非6，否则会报SyntaxError

print("\nfloat.is_integer()\n")
# Return True if the float instance is finite with integral value, and False otherwise:

print(-2.0.is_integer()) # 为什么输出了-1？
print((-2.0).is_integer())
print(3.2.is_integer())

print("\nfloat.hex()\n")
# https://docs.python.org/3/library/stdtypes.html#float.hex