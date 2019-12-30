##### 5.数据结构
#### 5.1 列表的更多特性
# https://docs.python.org/zh-cn/3/tutorial/datastructures.html#more-on-lists

### 5.1.3. 列表推导式
# https://docs.python.org/zh-cn/3/tutorial/datastructures.html#list-comprehensions

# 创建一个平方数的列表
# 原始：
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# 使用列表推导式：
squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares = [x**2 for x in range(10)]
print(squares)

# 更有意思的

a = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(a == combs)

# more

vec = [-4, -2, 0, 2, 4]
b = [x*2 for x in vec]
print('\nb', b)
c = [x for x in vec if x >= 0]
print('\nc', c)
d = [abs(x) for x in vec]
print('\nd', d)

freshfruit = ['banana', 'loganberry', 'passion fruit']
e = [weapon.strip() for weapon in freshfruit]
print('\ne', e)

ee = []
for weapon in freshfruit:
    ee.append(weapon.strip())
print(ee == e)

# create a list of 2-tuples like (number, square)
# the tuple must be parenthesized, otherwise an error is raised
f = [(x, x**2) for x in range(6)]
print('\nf', f)

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
g = [num for elem in vec for num in elem]
print('\ng', g)

gg = []
for elem in vec:
    for num in elem:
        gg.append(num)
print(gg == g)

from math import pi
h = [str(round(pi, i)) for i in range(1, 6)]
print('\nh', h)

hh = []
# namely, [1, 2, 3, 4, 5]
for i in range(1, 6):
    hh.append(str(round(pi, i)))

print(hh == h)

### 5.1.4. 嵌套的列表推导式
# 就是套娃……把组块拆出来就好……

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(matrix)
print(list(zip(matrix)))
print(list(zip(*matrix)))