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



#### 4.4.3 添加dropout正则化

## dropout是神经网络最有效最常用的正则化方法之一，出自Geoffrey Hinton和他的学生。
## 对某层使用dropout，就是在训练过程中将该层的一些输出特征「舍弃」（设置为0）

## 「dropout比率」(dropout rate)：被设为0的特征所占的比例

## 测试时没有单元被舍弃，而是按dropout比率缩小该层的输出值
    # 为什么❓
        ## 输出时比训练时有更多的单元被激活，需要加以平衡
            # “更多单元被激活”和“平衡”具体是指什么？
                # 哦，应该是指，输出时不像训练时会有一片0

## 在Keras中通过Dropout层向网络中引入dropout，dropout将被应用于前一层的输出

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))



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