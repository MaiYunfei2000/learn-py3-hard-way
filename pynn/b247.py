# 2.4.7 训练网络
# 详细的代码解释请翻阅前面的单元

import numpy
import scipy.special

class neuralNetwork:
    
    # 初始化函数
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
    
        # 设定输入层节点数
        self.inodes = inputnodes
        # 设定隐藏层节点数
        self.hnodes = hiddennodes
        # 设定输出层节点数
        self.onodes = outputnodes

        # 设定学习率
        self.lr = learningrate

        # 设定原始的权重矩阵：输入层至隐藏层
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        # 设定原始的权重矩阵：隐藏层至输出层
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        # 权重随机抽样自对称轴0标准差为节点数-0.5次幂的正态分布
        
        # 设定sigmoid函数
        self.activation_function = lambda x: scipy.special.expit(x)
        
        pass
    
    # 训练函数
    def train(self, inputs_list, targets_list):
        
        targets = numpy.array(targets_list, ndmin=2).T
        
        # error is the (target - actual)
        output_errors = targets - final_outputs
        
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        # 矩阵点乘：反向传播至隐藏层的误差矩阵 = 隐藏层至输出层的权重矩阵的转置 · 来自输出层的误差矩阵（列向量）
        hidden_errors = numpy.dot(self.who.T, output_errors)
        
        # update the weights for the links between the hidden and output layers（更新隐藏层至输出层的权重矩阵）
        # 原始函数：△w(j,k) = α * E(k) * sigmoid(O(k)) * (1 - sigmoid(O(k)) * O(j).T # 括号内容是下标符号的内容
        # 新的who矩阵 = 旧的who矩阵 + 等式右边的一大串内容
            # 学习率 * 矩阵点乘【（反向传播至隐藏层的误差矩阵 * 前馈至输出层的输入信号矩阵 * (1 - 前馈至输出层的输入信号矩阵)）* 隐藏层输出的信号矩阵】 
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        # transpose也是取矩阵的转置，可为什么不用.T呢？
        # more detailed information: [numpy.transpose — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.transpose.html)
        
        # update the weights for the links between the input and hidden layers(更新输入层至隐藏层的权重矩阵）
        self.wih += self.lr * numpy.dot((hidden_error * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        # 注意最后一个变量是inputs即输入信号矩阵
        
        pass
        
    # 查询函数
    def query(self, inputs_list):
        
        # 输入层
        inputs = numpy.array(inputs_list, ndmin=2).T
        # 生成输入信号矩阵：将输入信号的列表转化为矩阵再取其转置

        # 隐藏层
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 矩阵点乘：前馈至隐藏层的输入信号矩阵 = 输入层至隐藏层的权重矩阵 · 外部输入信号矩阵（列向量）
        hidden_outputs = self.activation_function(hidden_inputs)
        # 线性变换：将 前馈至隐藏层的输入信号矩阵 映射至 sigmoid函数的值域 得到 隐藏层输出的信号矩阵（即前馈至输出层的输入信号矩阵）

        # 输出层
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 矩阵点乘：前馈至输出层的输入信号矩阵 = 隐藏层至输出层的权重矩阵 · 隐藏层输出的信号矩阵
        final_outputs = self.activation_function(final_inputs)
        # 线性变换，得到sigmoid(x)

        pass

input_nodes = 3
hidden_nodes = 3
output_nodes = 3

learning_rate = 0.5

n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)