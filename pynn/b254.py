# 2.5.4 一些改进：调整学习率

## 将神经网络的学习率由0.5多次摸索后调整为0.2

# 2.5.5 一些改进：多次运行

## 让神经网络不只是训练1个「世代」(epoch)，从1改为2，然后发现5是个不错的点

# 2.5.6 改变神经网络的形状

## 调整节点数以继续优化：把隐藏层节点数由100调整为200

# 2.5.8 最终结果

import numpy, scipy.special, matplotlib.pyplot

class neuralNetwork:
    
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
    
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.lr = learningrate

        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        self.activation_function = lambda x: scipy.special.expit(x)
    
    def train(self, inputs_list, targets_list):
        
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        # the same as targets list
        targets = numpy.array(targets_list, ndmin=2).T
        
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calculate the signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        #print("training...final_outputs\n: ", final_outputs) # 调试用

        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        
        print("training...output_errors: \n", output_errors) # 调试
        
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)
 
        # update the weights fo rthe links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        
        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
    def query(self, inputs_list):
        
        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputs

input_nodes = 784
hidden_nodes = 200
output_nodes = 10

learning_rate = 0.2

# create an instance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# load the mnist training data CSV file into a list
training_data_file = open("makeyourownneuralnetwork-master/mnist_dataset/mnist_train.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# train the neural network

# epoch is the number of times the training data set is used for training
epochs = 5

for e in range(epochs):

    # go through all records in the training data set
    for record in training_data_list:
        # split the record by the ',' commas
        all_values = record.split(',')
        # scale and shift the inputs
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        # create the target output values (all 0.01, except the desired label which is 0.99)
        targets = numpy.zeros(output_nodes) + 0.01
        # all_values[0] is the target label for this record
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)

# load the mnist test data CSV file into a list

test_data_file = open("makeyourownneuralnetwork-master/mnist_dataset/mnist_test.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# test the neural network

# scorecard for how well the records in the test data set
scorecard = []

# go through all the records in the test data set
for record in test_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    # correct answer is first value
    correct_label = int(all_values[0])
    print("correct label:		", correct_label)
    # scale and shift the inputs
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # query the network
    outputs = n.query(inputs)
    # the index of the highest value corresponds to the label
    label = numpy.argmax(outputs)
    print("network's answer:	", label, '\n')

    if (label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)

# calculate the performance score, the fraction of correct answers
scorecard_array = numpy.asarray(scorecard) 
print("performance = ", scorecard_array.sum() / scorecard_array.size)

# 来理一理计算机大概要做多少运算：
# 训练60000次，每次训练中有：生成输入矩阵的转置，生成输出矩阵的转置，矩阵点乘得到隐藏层输入信号矩阵，sigmoid函数运算得到隐藏层输出的信号矩阵，点乘得到传至输出层的信号矩阵，sigmoid函数运算得到此次最终输出的信号，减法运算得到此次运算的误差，随后开始回馈——点乘得到返回至隐藏层的误差矩阵，更新权重，再更新权重。这样涉及到运算的代码行数就有10。然后训练60000次就要跑600000行算术代码。
# 然后训练5个世代，要跑3billion行运算代码……
# 接着测试10000次……