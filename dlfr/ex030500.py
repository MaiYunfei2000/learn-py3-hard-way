##### 3.5 新闻分类：多分类问题



#### 3.5.1 加载路透社数据集

from keras.datasets import reuters

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(
    num_words=10000)

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