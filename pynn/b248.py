# 2.4.8 完整的神经网络代码
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

        output_errors = targets - final_outputs

        # 反向传播至隐藏层的误差
        hidden_errors = numpy.dot(self.who.T, output_errors)
 
        # 更新隐藏层至输出层的权重
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        
        # 更新输入层至隐藏层的权重
        self.wih += self.lr * numpy.dot((hidden_error * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
        pass
        
    # 查询函数
    def query(self, inputs_list):
        
        # 输入层
        # 输入信号
        inputs = numpy.array(inputs_list, ndmin=2).T

        # 隐藏层
        # 前馈至隐藏层的输入信号
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 隐藏层输出的信号矩阵（即前馈至输出层的输入信号矩阵）
        hidden_outputs = self.activation_function(hidden_inputs)函数的值域 得到 隐藏层输出的信号矩阵（即前馈至输出层的输入信号矩阵）

        # 输出层
        # 前馈至输出层的输入信号矩阵
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 最终输出的信号
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputst

        pass

input_nodes = 3
hidden_nodes = 3
output_nodes = 3

learning_rate = 0.5

n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)