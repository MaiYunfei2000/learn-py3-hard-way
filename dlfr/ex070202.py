##### 7.2.2 TensorBoard 简介：TensorFlow 的可视化框架


### 7-7 使用了 TensorBoard 的文本分类模型

import keras
import tensorflow
from tensorflow.keras import layers
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence

## 作为特征的单词个数
max_features = 2000
## 在这么多单词之后截断文本（这些单词都属于前 max_features 个最常见的单词）
max_len = 500

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
x_train = sequence.pad_sequences(x_train, maxlen=max_len)
x_test = sequence.pad_sequences(x_test, maxlen=max_len)

model = tensorflow.keras.models.Sequential()
model.add(layers.Embedding(max_features, 128,
                           input_length=max_len,
                           name='embed'))
model.add(layers.Conv1D(32, 7, activation='relu'))
model.add(layers.MaxPooling1D(5))
model.add(layers.Conv1D(32, 7, activation='relu'))
model.add(layers.GlobalMaxPooling1D())
model.add(layers.Dense(1))
model.summary()
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['acc'])


### 7-8 为 TensorBoard 日志文件创建一个目录

"""
（命令行内）
$ mkdir my_log_dir
"""


### 7-9 使用一个 TensorBoard 回调函数来训练模型

callbacks = [
    tensorflow.keras.callbacks.TensorBoard(
        ## 日志文件将被写入这个位置
        log_dir='my_log_dir',
        ## 每一轮之后记录激活直方图
        histogram_freq=1,
        ## 每一轮之后记录嵌入数据
        embeddings_freq=1,
    )
]
history = model.fit(x_train, y_train,
                    epochs=20,
                    batch_size=128,
                    validation_split=0.2,
                    callbacks=callbacks)

# 然后，可以在命令行里启动 TensorBoard 服务器
# $ python3 /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/tensorboard/main.py --logdir=my_log_dir