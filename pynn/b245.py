# 2.4.5 查询网络
# 2.4.6 迄今为止的代码

# 本节编写query()函数

import numpy
# 从SciPy Python库里调用一些特殊的函数，例如本书内容所需的S抑制函数(sigmoid(x))
# scipy.special for the sigmoid function expit()
import scipy.special

class neuralNetwork:
    
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
    
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.lr = learningrate

        self.wih = numpy.random.normal(0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        # activation function is the sigmoid function
        # [scipy.special.expit — SciPy v0.14.0 Reference Guide](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.special.expit.html)
        # [4. More Control Flow Tools — Python 3.8.0 documentation](https://docs.python.org/3/tutorial/controlflow.html)
        self.activation_function = lambda x: scipy.special.expit(x)
        # lambda也是一种创建函数的方式，只不过相较def()没有名字，等等，因此创建起来较方便快捷；有些程序员喜欢称其为匿名函数，不过这里分配了一个名字“self.activation_function”（注意，名字后无括号，否则会报错：SyntaxError: can't assign to function call）
        # 这个函数接受x，返回scipy.special.expit(x)，是不是更加有数学函数的感觉了？
        # 之后要使用sigmoid函数，调用self.activation_function()即可（注意，这里有括号了！）
        # 此代码的效果等同于
        """
        def self.activation_function(x):
            return scipy.special.expit(x)
        """
        # 使用方式与lambda函数相同
        
        pass
        
    def train():
        pass
        
    def query(self, inputs_list):
        
        # convert inputs list to 2d array（将输入转换为二维矩阵）
        # numpy.array()的功能是创建一个矩阵
        # 其中inputs_list作为参数从函数query()中获取（但是什么个东西？）；ndmin是可选参数，指定矩阵具有的最小维数
        inputs = numpy.array(inputs_list, ndmin=2).T
        # 末尾的".T"啥意思？哦，转置。如果没有这个，则这个input为行向量而非列向量
        # more detailed information: [numpy.array — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)
        
        # calculate signals into hidden layer
        # numpy.dot(A, B): 做矩阵乘法，输出矩阵A与矩阵B的点积即A·B
        # 注意先后顺序
        hidden_inputs = numpy.dot(self.wih, inputs)
        # more detailed information: [numpy.dot — NumPy v1.17rc1 Manual](https://numpy.org/doc/1.17/reference/generated/numpy.dot.html?highlight=numpy%20dot#numpy.dot)
        
        # calculate the signals emerging from hidden layer (计算隐藏层中出现的信号)
        # 也就是矩阵内每个数值都生成sigmoid函数，得到一个新矩阵
        hidden_outputs = self.activation_function(hidden_inputs)
        # 这个就是隐藏层节点的输出信号（相对于输出层来说则是输入信号了）
        
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        # 自己额外加的一条测试代码
        print(final_outputs)
        
        pass

input_nodes = 3
hidden_nodes = 3
output_nodes = 3

learning_rate = 0.5

# set n to an instance of neuralNetwork
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)



# from n get the query function, call it with an array [1, 0.5, -1.5]
n.query([1, 0.5, -1.5])