# 2.5
# 详细的代码解释请翻阅前面的单元

import numpy
import matplotlib.pyplot

# 打开该路径的文件，以只读模式；将数据赋给变量data_file
data_file = open("makeyourownneuralnetwork-master/mnist_dataset/mnist_train_100.csv", 'r')

# “从输入流读取所有行并将其作为一个行列表返回。”[codecs --- 编解码器注册和相关基类 — Python 3.7.5 文档](https://docs.python.org/zh-cn/3/library/codecs.html?highlight=readlines#codecs.StreamReader.readlines)
data_list = data_file.readlines()

# 关闭文件是个好习惯~
data_file.close()

# 将data_list的第0行（即第1行）用逗号将字符串分割成一条list，赋给all_values
all_values = data_list[0].split(',')
# [1:]采用列表all_values中第一个元素以外的所有值
# numpy.asfarray()将文本字符串转化为实数，更多见[numpy.asfarray — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.asfarray.html)
# reshape((28,28))列表每28个元素“折返一次”（也许是转到第二行开头的意思），形成28*28的方阵
# 将这个方阵形式的数组赋给image_array
image_array = numpy.asfarray(all_values[1:]).reshape(28,28)

# 使用imshow()函数绘制出image_array
# cmap='Greys'：选择灰度调色板
matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
matplotlib.pyplot.show()
# 然后就将csv数据还原成位图显示出来了

print('\n再试一试？直到你感到无聊并按下CTRL-C\n')

while True:
    
    i = int(input('想读取第几行？请输入：'))
    
    all_values = data_list[i].split(',')
    image_array = numpy.asfarray(all_values[1:]).reshape(28,28)
    matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
    matplotlib.pyplot.show()

'''
import numpy
import scipy.special

class neuralNetwork:
    
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
    
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.lr = learningrate

        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        self.activation_function = lambda x: scipy.special.expit(x)
        
        pass
    
    def train(self, inputs_list, targets_list):
        
        targets = numpy.array(targets_list, ndmin=2).T

        output_errors = targets - final_outputs

        hidden_errors = numpy.dot(self.who.T, output_errors)
 
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        
        self.wih += self.lr * numpy.dot((hidden_error * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
        pass
        
    def query(self, inputs_list):
        
        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputst

        pass

input_nodes = 3
hidden_nodes = 3
output_nodes = 3

learning_rate = 0.5

n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
'''