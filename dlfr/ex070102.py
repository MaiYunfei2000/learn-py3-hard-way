##### 7.1.2 多输入模型

### 一个非常简单的多输入模型示例——一个问答模型。
### 典型的问答模型有两个输入：一个自然语言描述的问题和一个文本片段（比如新闻文章），后者提供用于回答问题的信息。然后模型要生成一个回答，在最简单的情况下，这个回答只包含一个词，可以通过对某个预定义的词表做 softmax 得到。

### 以下示例展示了如何用函数式 API 构建这样的模型。我们设置了两个独立分支，首先将文本输入和问题输入分别编码为表示向量，然后连接这些向量，最后，在连接好的表示上添加一个 softmax 分类器。


### 7-1 用函数式 API 实现双输入问答模型

from keras.models import Model
from keras import layers
from keras import Input

text_vocabulary_size = 10000
question_vocabulary_size = 10000
answer_vocabulary_size = 500

## 文本输入是一个长度可变的整数训练。注意，你可以选择对输入进行命名
text_input = Input(shape=(None,), dtype='int32', name='text')

## 将输入嵌入长度为 64 的向量
embedded_text = layers.Embedding(
    text_vocabulary_size, 64, name='embedding_text')(text_input)

## 利用 LSTM 将向量编码为单个向量
encoded_text = layers.LSTM(32, name='LSTM_text')(embedded_text)

## 对问题进行相同的处理（使用不同的层实例）
question_input = Input(shape=(None,),
                       dtype='int32',
                       name='question')

embedded_question = layers.Embedding(
    question_vocabulary_size, 32,
    name='embedding_question')(question_input)
encoded_question = layers.LSTM(16, name='LSTM_question')(embedded_question)

## 将编码后的文本连接起来
concatenated = layers.concatenate([encoded_text, encoded_question],
                                  axis=-1, name='concatenate')

## 在上面添加一个 softmax 分类器
answer = layers.Dense(answer_vocabulary_size,
                      activation='softmax',
                      name='softmax_classifier')(concatenated)

## 在模型实例化时，制定两个输入和输出
model = Model([text_input, question_input], answer)
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['acc'])

model.summary()

### 7-2 将数据输入到多输入模型中

import keras
import numpy as np

num_samples = 1000
max_length = 100

## 生成虚构的 NumPy 数据
text = np.random.randint(1, text_vocabulary_size,
                         size=(num_samples, max_length))

question = np.random.randint(1, question_vocabulary_size,
                             size=(num_samples, max_length))
answers = np.random.randint(answer_vocabulary_size, size=(num_samples))
## 回答是 one-hot 编码的，不是整数
answers = keras.utils.to_categorical(answers, answer_vocabulary_size)
# [工具 - Keras 中文文档](https://keras.io/zh/utils/)
    # 将类向量（整数）转换为二进制类矩阵。
"""
# 考虑一组 3 个类 {0,1,2} 中的 5 个标签数组：
> labels
array([0, 2, 1, 2, 0])
# `to_categorical` 将其转换为具有尽可能多表示类别数的列的矩阵。
# 行数保持不变。
> to_categorical(labels)
array([[ 1.,  0.,  0.],
       [ 0.,  0.,  1.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.],
       [ 1.,  0.,  0.]], dtype=float32)
"""
# 哦，帮忙轻松地进行 one-hot 编码

## 使用输入组成的列表来拟合
model.fit([text, question], answers, epochs=10, batch_size=128)

## 使用输入组成的字典来拟合（只有对输入进行命名之后才能用这种方法）
model.fit({'text': text, 'question': question}, answers,
          epochs=10, batch_size=128)