##### 3.5 新闻分类：多分类问题



#### 3.5.1 加载路透社数据集

## 路透社的短新闻文段及对应主题。共有46个主题。

from keras.datasets import reuters

## 参数num_words=10000：将数据限定为前10000个最常出现的单词。
(train_data, train_labels), (test_data, test_labels) = reuters.load_data(
    num_words=10000)

"""
## 8982个训练样本，2246个测试样本。
>>> len(train_data)
8982
>>> len(test_data)
2246
"""



#### 3.5.2 准备数据

## 可用上一节相同的代码将数据向量化。

import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

## 向量化训练数据
x_train = vectorize_sequences(train_data)
## 向量化测试数据
x_test = vectorize_sequences(test_data)

## 标签的向量化有两种方法。一是one-hot编码/「分类编码」(categorical encoding)。
while True:
    break
    
    def to_one_hot(labels, dimension=46):
        results = np.zeros((len(labels), dimension))
        for i, label in enumerate(labels):
            results[i, label] = 1.
        return results
    
    ## 向量化训练标签
    one_hot_train_labels = to_one_hot(train_labels)
    ## 向量化测试标签
    one_hot_train_labels = to_one_hot(test_labels)

## 另一种是使用Keras的内置函数（MNIST例子中已出现）

from keras.utils.np_utils import to_categorical

one_hot_train_labels = to_categorical(train_labels)
one_hot_test_labels = to_categorical(test_labels)



#### 3.5.3 构建网络

### 模型定义

from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
## 输出层有46个节点，对应46个类别
## softmax激活：输出一个表示概率分布的向量，向量所有维度的值的和为1
model.add(layers.Dense(46, activation='softmax'))

### 编译模型

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy', ## 分类交叉熵
              metrics=['accuracy'])



#### 3.5.4 验证你的方法

### 留出验证集

# 数据
x_val = x_train[:1000]
partial_x_train = x_train[1000:]
# 标签
y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]

"""
### 训练模型

history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val))

### 绘制训练损失和验证损失

import matplotlib.pyplot as plt

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

### 绘制训练精度和验证精度

plt.clf()

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()
"""

## ✨可见网络在训练9轮后开始过拟合。
## 对训练网络的指导意见是：训练9个世代是最佳的。

### 从头开始重新训练一个模型

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(partial_x_train,
          partial_y_train,
          epochs=9,
          batch_size=512,
          validation_data=(x_val, y_val))
results = model.evaluate(x_test, one_hot_test_labels)

print(results)


# https://docs.python.org/zh-cn/3/library/copy.html?highlight=copy#module-copy
import copy

# 创建test_labels的浅拷贝
test_labels_copy = copy.copy(test_labels)
# https://numpy.org/devdocs/reference/random/generated/numpy.random.shuffle.html
np.random.shuffle(test_labels_copy)
hits_array = np.array(test_labels) == np.array(test_labels_copy)
# 果然跟matlab矩阵一样，是对每个元素进行比较然后返回布尔值到相应位置上
print(hits_array)
print(float(np.sum(hits_array)) / len(test_labels))
## 0.18655387355298308


## 完全随机的精度约为19%，而前面的方法得到了约80%的精度。



### 3.5.5 在新数据上生成预测结果

predictions = model.predict(x_test)

"""
## 每个元素都是长度为46的向量
>>> predictions[0].shape
(46,)
## 向量所有元素总和为1
>>> np.sum(predictions[0])
1
## 概率值最大的元素就是预测的类别
>>> np.argmax(prediction[0])
4
"""