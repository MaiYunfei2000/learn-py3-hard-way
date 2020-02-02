##### 2.2 神经网络的数据表示
#### 2.2.1 标量（0D张量）

import numpy as np

# 创建一个数组x。这个数组只有“12”一个元素。
    # 更多细节参见：[numpy.array — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)
x = np.array(12)

print(x)

## 打印数组x/张量x的ndim属性。
## 即其「轴」(axis)的个数，又称为「阶」(rank)。
print(x.ndim)
print(x.shape)



#### 2.2.2 向量（1D张量）

x = np.array([12, 3, 6, 14, 7])
print(x)
print(x.ndim)

"""
- 这个向量有5个元素，因此是「5D向量」，但切勿与「5D张量」搞混！

    - 前者只有一个轴，沿着轴有5个维度；
    - 而后者有五个轴，沿着每个轴可能有任意维度。

    - （所以维度到底是个什么嘛= =）

    - 对于后者的情况，更准确的说法是「5阶张量」，
      只是「5维张量」这种模糊的写法更为常见。
"""



#### 2.2.3 矩阵（2D张量）

## 向量组成的数组叫作矩阵（matrix）或二维张量。
## 矩阵有两个轴，通常叫「行」和「列」。
## [5, 78, 2, 34, 0]是x的第一行；[5, 6, 7]是x的第一列
x = np.array([[5, 78, 2, 34, 0],
              [6, 79, 3, 35, 1],
              [7, 80, 4, 36, 2]])
# 这里三个向量之间的","的就像MATLAB的";"一样。
# 不过Python里的矩阵确实稍微没有MATLAB直观些，还是更容易看作一个套娃的列表。

print(x)
print(x.ndim)
print(x.shape)



#### 2.2.4 3D张量与更高维张量

## 将多个矩阵组合(taowa)成一个新的数组，可以得到一个3D向量。
## 可以直观地理解为数字组成的立方体。
# 🚧🚜要是有更直观的显示方式就好了

x = np.array([[[5, 78, 2, 34, 0],
               [6, 79, 3, 35, 1],
               [7, 80, 4, 36, 2]],
              [[5, 78, 2, 34, 0],
               [6, 79, 3, 35, 1],
               [7, 80, 4, 36, 2]],
              [[5, 78, 2, 34, 0],
               [6, 79, 3, 35, 1],
               [7, 80, 4, 36, 2]]])
print(x)
print('\n', x.ndim, sep='')
print(x.shape)

## 若将多个 3D数组/3D张量 合成为一个数组/张量（套娃+1），则可创建一个4D张量



#### 2.2.5 关键属性

"""
张量由以下三个关键属性来定义：

- 轴的个数 / 阶。在numpy中叫ndim。
- 形状。在numpy中叫shape。
- 数据类型。常见有float32, uint8, float64。详见：
        [Data type objects (dtype) — NumPy v1.19.dev0 Manual]
        (https://numpy.org/devdocs/reference/arrays.dtypes.html#specifying-and-constructing-data-types)
        [Data types — NumPy v1.19.dev0 Manual]
        (https://numpy.org/devdocs/user/basics.types.html?highlight=uint)
"""

from keras.datasets import mnist

(train_images, train_label), (test_images, test_label) = mnist.load_data()
print(train_images.ndim)
print(train_images.shape)
print(train_images.dtype)

print('\n', train_images[0])
print('\n', train_images[0][0])

"""
这里的train_images是一个8位整数组成的3D张量。更确切地说，是
60000个矩阵组成的数组，每个矩阵由28*28个整数组成。
每个元素的取值范围都是0~255。
也就是说，每个矩阵是一个28*28像素的方形灰度图像。
"""

digit = train_images[4]

import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()



#### 2.2.6 在NumPy中操作张量

## 「张量切片」(tensor slicing)

my_slice = train_images[10:100]
print("my_slice.shape", my_slice.shape)
## 等于上面的例子。
## 显示出了每个轴上的索引；“:”等同于选择整个轴
# 也就是跟MATLAB一样喽
my_slice = train_images[10:100, :, :]
print("my_slice.shape", my_slice.shape)
## 也等同于前面的例子
my_slice = train_images[10:100, 0:28, 0:28]
print("my_slice.shape", my_slice.shape)

## 又或者，可以在所有图像的右下角选出14*14像素的区域。
my_slice = train_images[:, 14:, 14:]
print("my_slice.shape", my_slice.shape)

## 也可以使用负数索引。负数代表与此轴终点的相应位置。
    ## 试着打印[1, 2, 3, 4, 5, 6, 7, 8, 9][2:-2]就明白了。
## 在图像的中心选出14*14像素的区域。
my_slice = train_images[:, 14:, 14:]
print("my_slice.shape", my_slice.shape)