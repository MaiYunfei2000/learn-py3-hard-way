##### 6.2 理解循环神经网络

#### 6.2.1 Keras中的循环层

from keras.layers import SimpleRNN

## SimpleRNN层与其它Keras层一样可以处理序列批量
## 它接收形状为(batch_size, timesteps, input_features)的输入，而不是(timesteps, input_features)

## 一个使用SimpleRNN的例子：只返回最后一个timestep的输出

from keras.models import Sequential
from keras.layers import Embedding, SimpleRNN
model = Sequential()
# Embedding层是干嘛的来着？
    # 搞词嵌入的。
        # 🚧给此层输入什么？
        # 🚧此层会输出什么？
model.add(Embedding(10000, 32))
## 若在32后面多加一个return_sequences=True，则使此例返回完整的状态序列（状态序列是什么意思❓哦，一个个状态形成的序列。）
model.add(SimpleRNN(32))
model.summary()

## 为了提高网络的表示能力，将多个循环层逐个堆叠有时也是很有用的。此时需要让所有中间层都返回完整的输出序列。
model = Sequential()
model.add(Embedding(10000, 32))
model.add(SimpleRNN(32, return_sequences=True))
model.add(SimpleRNN(32, return_sequences=True))
model.add(SimpleRNN(32, return_sequences=True))
## 最后一层仅返回最终输出
model.add(SimpleRNN(32))
model.summary()


## 接下来，将此模型应用于IMDB电影评论分类问题

## 首先，对数据进行预处理
### 6-22 准备IMDB数据
from keras.datasets import imdb
from keras.preprocessing import sequence

## 作为特征的单词个数
max_features = 10000
## 在这么多单词之后截断文本（这些单词都属于前max_features个最常见的单词）
maxlen = 500
batch_size = 32

print('Loading data...')
(input_train, y_train), (input_test, y_test) = imdb.load_data(
    # https://keras.io/datasets/#imdb-movie-reviews-sentiment-classification
    num_words=max_features)
print(len(input_train), 'train sequences')
print(len(input_test), 'test sequences')

print('Pad sequences (samples x time)')
input_train = sequence.pad_sequences(input_train, maxlen=maxlen)
input_test = sequence.pad_sequences(input_test, maxlen=maxlen)
print('input_train shape:', input_train.shape)
print('input_test shape:', input_test.shape)


### 6-23 用 Embedding 层和 SimpleRNN 层来训练模型

from keras.layers import Dense

model = Sequential()
model.add(Embedding(max_features, 32))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(input_train, y_train,
                    epochs=10,
                    batch_size=128,
                    validation_split=0.2)


### 6-24 绘制结果

import matplotlib.pyplot as plt

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

# 'bo': 蓝色圆点
# [matplotlib.pyplot.plot — Matplotlib 3.2.1 documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html?highlight=plot#matplotlib.pyplot.plot)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
# [matplotlib.pyplot.legend — Matplotlib 3.2.1 documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html?highlight=pyplot%20legend#matplotlib.pyplot.legend)
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()