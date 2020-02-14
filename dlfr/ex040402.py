##### 4.4 过拟合与欠拟合

"""
基于3.4节电影分类模型进行改进。
"""

from keras.datasets import imdb
from keras import models 
from keras import layers
import matplotlib.pyplot as plt



(train_data, train_labels), (test_data, test_labels) = imdb.load_data(
    num_words=10000)

import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')



#### 4.4.2 添加权重正则化

## 一种常见的降低过拟合的方法是强制让模型权重只能取较小的值，从而限制模型的复杂度，使权重值的分布更加「规则」（regular）。这种方法叫「权重正则化」（weight regularization），实现方法是向网络损失函数中添加与较大权重值相关的「成本」（cost）（❓所以「成本」是什么意思）
"""
成本有两种形式：

- L1正则化（L1 regularization）：添加的成本与权重系数的绝对值[权重的「L1范数(norm)」]成正比。
- L2正则化（L2 regularization）：添加的成本与权重系数的平方（权重的「L2范数」成正比。也叫「权重衰减」（weight decay）。
"""

### 4-6 向模型添加L2权重正则化

from keras import regularizers

model = models.Sequential()
## l2(0.001)：该层权重矩阵的每个系数都会使网络总损失增加0.001 * weight_coefficient_value
model.add(layers.Dense(16, kernel_regularizer=regularizers.l2(0.001),
                         activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, kernel_regularizer=regularizers.l2(0.001),
                         activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

### 4-7 Keras中不同的权重正则化项

while True:
    break
    
    regularizers.l1(0.001) ## L1正则化
    
    regularizers.l1_l2(l1=0.001, l2=0.001) ## 同时做l1和l2正则化
    
    

# 编译、验证及可视化

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

x_val = x_train[:10000]
partial_x_train = x_train[10000:]

y_val = y_train[:10000]
partial_y_train = y_train[10000:]

history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20, 
                    batch_size=512, 
                    validation_data=(x_val, y_val))

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