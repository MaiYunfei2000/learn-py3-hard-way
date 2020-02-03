##### 2.3 神经网络的“齿轮”：张量运算

import numpy as np

#### 2.3.1 逐元素运算

## 逐元素relu运算

def naive_relu(x):
    """
    x is a 2D tensor
    """
    # assert 是什么意思？
    # [7. 简单语句 — Python 3.8.1 文档](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#the-assert-statement)
    # 只理解了如果这条式子为False则会引起AssertionError
        # 看来就是用来自定义报错内容的
    assert len(x.shape) == 2
    
    # 创建x的浅拷贝
    ## 避免覆盖输入的张量
    # 那为什么不是赋给别的变量名如y，而是还是给了x？这和x = x有什么区别？
        # 噢噢，学到了。这里赋给的x是函数内的局部变量。
        # 如果删去.copy()，就直接对全局变量下手了
        # ⚠️那为什么在无copy()的情况下把局部变量名改为y就行不通呢？后面的操作不都是在对y操作吗？为什么x还是会受到影响？
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            # 2D张量中(i,j)元素
            x[i, j] = max(x[i, j], 0)
    return x

# test
x = np.array([[-5, 78, -2, 34, 0],
              [-6, 79, 3, 35, 1],
              [-7, 80, 4, 36, 2]])

print("x:\n", x, end='\n\n')

y = naive_relu(x)
print("x, y:", x, y, sep='\n\n')

# relu运算在出现负数元素时才会有效果。所谓relu也许就是把负数会变成0的运算吧？
# 原来「逐元素」(element-wise)运算的意思就是字面意思啊——逐个元素地运算

print(y[1, 1])
# 突然理解为什么Python以0为起点了
    # 位于[0,0]位置上的元素就像是位于坐标原点上的一个东西一样
    # 位于[c,0]位置上的元素就像是位于第一个轴任意位置上的东西一样
    # 三维张量的情况也很好理解，想想立体几何就是了


## 逐元素加法运算
## 同样的方法可实现乘法

def naive_add(x, y):
    # x的shape的长度必须为2，即x必须是2D向量
    assert len(x.shape) == 2
    # x与y的形状必须相等
    assert x.shape == y.shape
    
    x = x.copy()
    for i in range(x.shape[0]):
        # 才发现，原来.shape其实就是推广至2维及更高维情况的len()，虽然前者是属性，后者是方法
        for j in range(x.shape[0]):
            # x的某个元素与y的相同位置的元素相加，赋给x的这个位置上的元素
            x[i, j] += y[i, j]
    return x

z = naive_add(x, y)
print("\nz:\n", z, end='\n')



#### 2.3.2 广播

"""
广播(broadcast)：使较小的张量变形，以匹配较大的张量。

广播有以下两步：

- 向较小向量添加轴（称作「广播轴」），使其ndim与较大张量的ndim相同
- 使较小向量沿着新轴重复，使其shape与较大张量的shape相同

"""

def naive_add_matrix_and_vector(x, y):
    """x is-a 2D tensor; 
       y is-a vector (1D tensor);
       the second(1st) axis of x is the same as the first(0th) axis of y"""
    # x必须为2D张量
    assert len(x.shape) == 2
    # y必须为1D张量
    assert len(y.shape) == 1
    # x的第二个轴（横轴）的长度必须与y的第一个轴的长度相同
        # 也就是矩阵x的行的长度（/列数/元素个数）必须等于向量的长度（元素个数）
    assert x.shape[1] == y.shape[0]
    
    x = x.copy()
    # 对于x的第一个轴（纵轴）上的元素的索引：
    for i in range(x.shape[0]):
        # 对于x的第二个轴（横轴）上的元素的索引
        for j in range(x.shape[1]):
            x[i, j] += y[j]
    return x

x = np.array([[-5, 78, -2, 34, 0],
              [-6, 79, 3, 35, 1],
              [-7, 80, 4, 36, 2]])

y = np.array([10,
              100,
              1000,
              100,
              10])
z = naive_add_matrix_and_vector(x, y)
print("\nz:\n", z, end='\n')

# 生成shape为(64, 3, 32, 10)的元素为0~1随机数的张量
x = np.random.random((64, 3, 32, 10))
# [numpy.random.random — NumPy v1.14 Manual](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.random.html)
# 前一个random指的是模块，后一个random指的是方法
y = np.random.random((32, 10))

z = np.maximum(x, y)
print(x, y, z, sep='\n', end='\n') 

# ……我自己搞个例子好了

x = np.array([[-5, 78, -2, 34, 0],
              [-6, 79, 3, 35, 1],
              [-7, 80, 4, 36, 2]])
y = np.array([10,
              100,
              1000,
              100,
              10])
# 逐元素取较大值，如果两张量shape不相同则广播后再比较
# [numpy.maximum — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.maximum.html)
z = np.maximum(x, y)
print(x, y, z, sep='\n', end='\n')



#### 2.3.3 张量点积

# 类比矩阵点积（只适用于1D和2D张量），略过。更高维的情况实操时再说。

#### 2.3.4 张量变形

x = np.array([[0., 1.,
               2., 3.,
               4., 5.]])
# 看起来可以理解为先降维为线性（一维），再将元素按这个一维顺序一次次排成更高维的样子。
# 对于二维的情况，例如这里，有个形象的类比：
    # 想象一下串着珠子的长度可任意变化的绳子，每个珠子上刻有一个数字，且相互间隔也可以变化
    # 可以随便摆弄绳子的形状。有一个顺序始终不变。纯文字不好描述，直接脑补吧。
print(x.shape)
x = x.reshape((6, 1))
print(x.shape)
x = x.reshape((2, 3))
print(x.shape)

# 剩余的可参见线性代数的「转置」和「线性变换」，此略。

#### 2.3.5 张量运算的几何解释

# 略，参见国外线性代数教材。

#### 2.3.6 深度学习的几何解释

# 略。