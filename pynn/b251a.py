# 2.5.1 准备MNIST训练数据
# part a 理解代码

import numpy
import matplotlib.pyplot

data_file = open("makeyourownneuralnetwork-master/mnist_dataset/mnist_train_100.csv", 'r')
data_list = data_file.readlines()
data_file.close()

all_values = data_list[0].split(',')
# [1:] means that take the list "all_values", excluding the first (the zeroth!) element
# 颜色像素的数值范围从0到255（十六进制：00到FF)，这里是为了控制数值在0.01至0.99（0~1是因为sigmoid()函数的值域是(0,1)，如果神经网络运算过程中的值超过值域就没意义了，神经网络输出值永远小于数据集的数值就没意义了；然后，0和1都会GG，你懂的）
# 防脑子断路：比如你想把120分制的分数转换为百分制的，你可以用 score / 120 * 100 来得到这个分数
scaled_input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
print(scaled_input)

# output nodes is 10 (example)
onodes = 10
# numpy.zeros(10)生成了一个十维的零向量
targets = numpy.zeros(onodes) + 0.01

# 取targets的第[]个元素，方括号里的值由all_values的第一个元素转化为整数后给出
# 此数据集的情况为第1行代表着数字5，然后这一行的第一个数字（即标准答案）为5，它通过这样的方式赋给了变量targets的的第6个元素
# 这样就形成了数字“5”对应的正确目标输出（标准答案）：如果神经网络输出的向量明显靠近(0,0,0,0,0,0.99,0,0,0,0)，则它的判断就正确了
# 另外注意，向量（0.99,0,0,0,0,0,0,0,0,0)代表着数字0的正确输出结果
targets[int(all_values[0])] = 0.99