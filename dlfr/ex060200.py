##### 6.2 理解循环神经网络

## RNN的输入是一个张量序列（❓所谓张量序列，就是「数列」的张量版吗？），shape=(timesteps, input_features)。
## 它对timestep进行遍历（什么是「遍历」❓“沿着某条搜索路线，依次对树（或图）中每个节点均做一次访问”；“是二叉树最重要的运算之一”——「访问」和「二叉树」是什么意思？？？），在每个timestep，它考虑t时刻的当前状态与t时刻的输入（形状为(input_features,)，对二者计算得到t时刻的输出。
    # 哦也就是说，在第n次信息加工过程中（n≥2），RNN的某节点/层在产生一个输出时，同时要考虑（同时要计算）本次（第n次）来到此节点/层的输入数据***与***上次（第n-1次）的(输入？输出？)数据。that is，对两者计算得到此次输出。随后咧，本次（n）输入?输出?会作为下一次（n+1）信息加工的数据之一。无限重复下去……
    # 哦，在6-19解决了，是以本次**输出**作为下次状态
# 那对于第一个timestep该怎么办呢？
    ## 它的上一个timestep的输出没有定义，因此它没有「当前状态」。处理方法是以全零向量作为「初始状态」(initial state)

"""
### 6-19 RNN伪代码
    
## t时刻的状态
state_t = 0
## 对序列元素进行遍历
for input_t in input_sequence:
    output_t = f(input_t, state_t)
    ## 前一次的输出变成下一次迭代的状态
    state_t = output_t

### 6-20 更详细的RNN伪代码

state_t = 0
for input_t in input_sequence:
    # 把6-19中的抽象f换成了更具体的activation函数
    ## 在这个激活函数例子里，参数包括两个矩阵W、U和一个偏置向量b
    output_t = activation(dor(W, input_t) + dot(U, state_t) + b)
    state_t = output_t
"""
    
### 6-21 简单RNN的NumPy实现
import numpy as np

## 输入序列的时间步数
timesteps = 100
## 输入特征空间的维度
input_features = 32
## 输出特征空间的维度
output_features = 64
# 🚧「特征空间」是什么意思？？？？？？与4.3.2的「特征工程」有关吗？还是指线性代数里的「特征空间」（“特征空间是相同特征值的特征向量与同维度的零向量的集合”——Wikipedia）？？？？？呼——嘶——头大。似乎是个机器学习术语，不是线代的。

## 输入数据：随机噪声，仅作为示例
    # np.random.random(shape)：返回一个张量，形状为shape，元素为[0.0, 1.0)区间内的浮点数。
    # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.random.html
inputs = np.random.random((timesteps, input_features))

## 初始状态：全零向量
    # 生成一个形状为(output_features,)的零张量
state_t = np.zeros((output_features,))

## 创建随机的权重矩阵
W = np.random.random((output_features, input_features)) # (64, 32)
U = np.random.random((output_features, output_features)) # (64, 64)
b = np.random.random((output_features,)) # (64,)
# 🚧 W, U, b 具体代表什么与什么之间的连接权重呢？
# 参见图 6-10 的中间的矩形里的内容。

successive_outputs = []
## input_t是shape=(input_features,)的向量
# 对样本轴(axis 0)进行遍历
"""
举例：
>>> a = np.array([[1,2],[3,4]])
>>> a
array([[1, 2],
       [3, 4]])
>>> for i in a:
...     print(i)
...     print("hey")
...
[1 2]
hey
[3 4]
hey
"""
for input_t in inputs:
    ## 由「输入」和「当前状态」(前一个输出)计算得到当前输出
    # output_t = （W与input_t点积 + U与state_t点积 + b）的双曲正切函数
        # （双曲正切函数为此例的激活函数）
        # https://docs.scipy.org/doc/numpy/reference/generated/numpy.tanh.html
    output_t = np.tanh(np.dot(W, input_t) + np.dot(U, state_t) + b)
    
    ## 将这个输出保存到一个列表中
    successive_outputs.append(output_t)
    # 输出的形状是什么？
        # axis 0的：append的次数，即for循环遍历的次数，即inputs在axis 0上的维数，即timesteps
        # axis 1的：output_t的维数，即input_t的维数，即inputs的axis 1的维数，即input_features
    
    ## 更新网络的状态，用于下一个timestep
    state_t = output_t

## 最终输出是一个shape=(timesteps, output_features)的二维张量
    # numpy.stack(arrays, axis=0, out=None)：Join a sequence of arrays along a new axis. 沿着一个新轴加入一个数组
    # The axis parameter specifies the index of the new axis in the dimensions of the result. For example, if axis=0 it will be the first dimension and if axis=-1 it will be the last dimension.
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.stack.html
    # 感觉就是把一个元素都为1D array的list变成一个2D array呢，然后究竟依哪个轴来堆叠出新array则视参数而定
final_output_sequence = np.stack(successive_outputs, axis=0)



# 随便玩玩
print("Successfully loaded.")
while True:
    exec(input(">>> "))