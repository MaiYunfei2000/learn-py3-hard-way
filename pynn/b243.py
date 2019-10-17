# 2.4.3 权重——网络的核心

import numpy

# 生成3*3的随机数组，每个值都是0~1的随机值
s = numpy.random.rand(3, 3) - 0.5

# 更多关于numpy.random的内容详见官方文档

# 这一块是即兴自由发挥
'''
r = s

# 对于0至2的整数i，循环：
for i in range(3):
    
    for j in range(3):
        
        # 单元(i,j)的数值取5位小数
        r[i,j] = round(r[i,j], 5)

print(s)
'''

# 载入2.4.2的代码

class neuralNetwork:
    
    def __init__(self,
    inputnodes, hiddennodes, outputnodes,
    learningrate):
    
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.lr = learningrate
        
        
        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc
        
        # 生成随机数组，数组的尺寸为变量self.hnodes和self.inodes所对应的值，分别为行、列
        # 数组每个数值减去0.5后赋给变量self.wih
        self.wih = numpy.random.rand(self.hnodes, self.inodes) - 0.5
        # 生成随机数组，数组的大小为变量self.onodes和self.hnodes所对应的值
        self.who = numpy.random.rand(self.onodes, self.hnodes) - 0.5
        # wih means the weight of input and hidden layer and who means that of hidden and output layer? (myf)
        
        # 或者也可以这样↓

        # 2.4.4 可选项：较复杂的权重
        
        # 函数numpy.random.normal(μ,σ,c)也是生成随机数组，只不过数值从正态分布中随机抽取x（横轴数值），如果是标准正态分布的话，你会发现更容易取到0.x~1.x的数值
        # 第一个参数为样本均值即正态分布的对称轴；第二个参数为样本标准差即正态分布大小的“标尺”；第三个为数组的尺寸（行，列），这个与前面的numpy.random.rand()一样
        # pow(self.hnodes, -0.5)为self.hnodes的数值的取-0.5次幂，也就是传入链接书目的开方
        self.wih = numpy.random.normal(0, pow(self.hnodes, -0.5),
            (self.hnodes, self.inodes))
        # 为什么是0.0而不是0？0也没问题
        self.who = numpy.random.normal(0, pow(self.onodes, -0.5),
            (self.onodes, self.hnodes))
        
        pass
        
    def train():
        pass
        
    def query():
        
        pass

input_nodes = 3
hidden_nodes = 3
output_nodes = 3

learning_rate = 0.5

n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)