##### 7.1.1 函数式 API 简介

from keras import Input, layers

## 一个张量
input_tensor = Input(shape=(32,))
## 一个层是一个函数
dense = layers.Dense(32, activation='relu')
## 可以在一个张量上调用一个层，它会返回一个张量
output_tensor = dense(input_tensor)


### 首先看一个最简单的示例，并列展示一个简单的 Sequential 模型以及对应的函数式 API 实现

from keras.models import Sequential, Model
from keras import layers
from keras import Input

seq_model = Sequential()
seq_model.add(layers.Dense(32, activation='relu', input_shape=(64,)))
seq_model.add(layers.Dense(32, activation='relu'))
seq_model.add(layers.Dense(10, activation='softmax'))

## 对应的函数式 API 实现
input_tensor = Input(shape=(64,))
x = layers.Dense(32, activation='relu')(input_tensor)
x = layers.Dense(32, activation='relu')(x)
output_tensor = layers.Dense(10, activation='softmax')(x)

## Model 类将输入张量和输出张量转换为一个模型
model = Model(input_tensor, output_tensor)

model.summary()

### 对这种 Model 实例进行编译、训练或评估时，其 API 与 Sequential 模型相同

## 编译模型
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

## 生成用于训练的虚构 Numpy 数据
import numpy as np
x_train = np.random.random((1000, 64))
y_train = np.random.random((1000, 10))

## 训练 10 轮模型
model.fit(x_train, y_train, epochs=10, batch_size=128)

## 评估模型
score = model.evaluate(x_train, y_train)