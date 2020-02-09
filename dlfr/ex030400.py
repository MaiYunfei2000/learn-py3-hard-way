##### 3.4 电影评论分类：二分类问题

import time # 用time.sleep()来辅助debug



#### 3.4.1 IMDB数据集

from keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(
    num_words=10000)
# 如train_data，是个向量。向量中的每个元素为array，如：array([1, 17, 6, 194, 337, 7, 4, 204, 22, 45, 254, 8, 106, 14, 123, 4, 2, 270, 2, 5, 2, 2, 732, 2098, 101, 405, 39, 14, 1034, 4, 1310, 9, 115, 50, 305, 12, 47, 4, 168, 5, 235, 7, 38, 111, 699, 102, 7, 4, 4039, 9245, 9, 24, 6, 78, 1099, 17, 2345, 2, 21, 27, 9685, 6139, 5, 2, 1603, 92, 1183, 4, 1310, 7, 4, 204, 42, 97, 90, 35, 221, 109, 29, 127, 27, 118, 8, 97, 12, 157, 21, 6789, 2, 9, 6, 66, 78, 1099, 4, 631, 1191, 5, 2642, 272, 191, 1070, 6, 7585, 8, 2197, 2, 2, 544, 5, 383, 1271, 848, 1468, 2, 497, 2, 8, 1597, 8778, 2, 21, 60, 27, 239, 9, 43, 8368, 209, 405, 10, 10, 12, 764, 40, 4, 248, 20, 12, 16, 5, 174, 1791, 72, 7, 51, 6, 1739, 22, 4, 204, 131, 9])
# train_data.shape = 25000

# [max(sequence) for sequence in train_data]相当于：
"""
for sequence in train_data:
    max(sequence)
"""
print(max([max(sequence) for sequence in train_data]))


# 将评论解码为英文单词

word_index = imdb.get_word_index()
## 将单词映射为整数索引的字典
    ## 键值颠倒
    # []里的式子产出了一个元素为二元组的列表
    # 对于每个二元组，元素依次为value和key
    # dict.items(): https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=items#dict.items
reverse_word_index = dict(
    [(value, key) for (key, value) in word_index.items()])
## 解码评论
    ## 索引减去了3，因为0、1、2为元数据"padding", "start of sequence", "unknown"分别保留的索引
decoded_review = ' '.join(
    [reverse_word_index.get(i - 3, '?') for i in train_data[0]])



#### 3.4.2 准备数据

## 对列表进行one-hot编码，将其转换成0和1组成的向量

import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    ## 创建一个形状为(len(sequences), dimension)的矩阵
        # numpy.zeros(): https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html
    results = np.zeros((len(sequences), dimension))
    # enumerate(): https://docs.python.org/zh-cn/3/library/functions.html?highlight=enumerate#enumerate
    for i, sequence in enumerate(sequences):
        # 将浮点数1.赋给矩阵results第i行第sequence列的元素
            # 请注意：sequence到底指的是什么？
                # 是sequences的一个个元素即列表，例子见前面的代码注释
        # 所以results[i,sequence]到底是什么？？？？？？？？为什么索引里面会有array？？？？？？
            # 原来如此：是numpy的索引方式，例子见https://www.runoob.com/numpy/numpy-advanced-indexing.html
            # 这块有好多文章可作，那么只好先放过了。更多见[Indexing — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/user/basics.indexing.html)；[Indexing — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html)
        results[i, sequence] = 1.
    return results

## 将训练数据向量化
x_train = vectorize_sequences(train_data)
## 将测试数据向量化
x_test = vectorize_sequences(test_data)

## 将标签向量化
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')



#### 3.4.3 构建网络


### 代码清单3-3 模型定义

from keras import models
from keras import layers

model = models.Sequential()
# 按顺序叠加一个层。类型为Dense，节点16个，激活函数为relu，最后一个参数是？
    # 哦输入层的形状，即10000个节点。用于接收10000维的向量。
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
## relu：整流线性单元(rectified linear unit)，激活函数之一。将负值归零。
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


### 代码清单3-4 编译模型

# 优化器：'rmsprop'；损失函数：二元交叉熵；指标函数：准确率。
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
# 噢，指标函数就是对神经网络性能的度量。与Tariq里面讲的性能/绩效(performance)是一回事。


## 有时会希望自定义优化器的参数，或传入自定义的损失函数或指标函数。

### 代码清单3-5 配置优化器
while True:
    break
    
    from keras import optimizers
    
    model.compile(optimizer=optimizer.RMSprop(lr=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy']) # 后两行没变

## 代码清单3-6 使用自定义的损失和指标
while True:
    break
    
    from keras import losses
    from keras import metrics
    
    model.compile(optimizer=optimizer.RMSprop(lr=0.001),
                  loss=losses.binary_crossentropy,
                  metrics=[metrics.binary_accuracy])


#### 3.4.4 验证你的方法

### 代码清单3-7 留出验证集

## 将原始训练数据留出10000个样本作为验证集

# 截取向量x_train的后10000个单元成为一个向量，赋给变量x_val
x_val = x_train[:10000]
partial_x_train = x_train[10000:]

# 这是标签数据
y_val = y_train[:10000]
partial_y_train = y_train[10000:]


### 代码清单3-8 训练模型

history = model.fit(partial_x_train, # 训练数据
                    partial_y_train, # 训练标签
                    epochs=20, # 世代数
                    batch_size=512, # 批量的大小
                    validation_data=(x_val, y_val)) # 用于验证数据的参数

history_dict = history.history
# 打印字典history_dict的键
print(history_dict.keys())
## 返回：dict_keys(['val_acc', 'acc', 'val_loss', 'loss'])

# 再多打印些东西来玩玩
print(history_dict)


### 代码清单3-9 绘制训练损失和验证损失

import matplotlib.pyplot as plt

history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']

epochs = range(1, len(loss_values) + 1)

plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()