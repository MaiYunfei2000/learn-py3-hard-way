##### 6.1 处理文本数据

#### 6.1.2 使用词嵌入

## 将单词与向量关联还有另一种常用的强大方法，就是使用密集的词向量（word vector），也叫词嵌入（word embedding）

"""
获取词嵌入有两种方法：

- 在完成主任务（比如文档分类或情感预测）的同时学习词嵌入。
- 在不同于待解决问题的机器学习任务上预计算好词嵌入，然后将其加载到模型中。（预训练词嵌入(pretrained word embedding)）
"""



### 6-5 将一个Embedding层实例化

from keras.layers import Embedding

## Embedding层至少需要两个参数：标记的个数（这里是1000，即最大单词索引+1）和嵌入的维度（这里是64）
embedding_layer = Embedding(1000, 64)
print(embedding_layer)



### 6-6 加载IMDB数据，准备用于Embedding层

from keras.datasets import imdb
from keras import preprocessing
## 作为特征的单词个数
max_features = 10000
## 在这么多单词后截断文本（这些单词都属于前max_features个最常见的单词）
maxlen = 20

# https://keras.io/datasets/#imdb-movie-reviews-sentiment-classification
(x_train, y_train), (x_test, y_test) = imdb.load_data(
    ## 将数据加载为整数列表
    num_words=max_features)

print(x_train[0])
print(y_train)

## 将整数列表转换成形状为(samples, maxlen)的二维整数张量
# https://keras.io/preprocessing/sequence/
x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)
print(x_train[0])
print(type(x_train))
# ❓发生了什么？？？？？？？？？？


### 6-7 在IMDB数据上使用Embedding层和分类器

from keras.models import Sequential
from keras.layers import Flatten, Dense, Embedding

model = Sequential()
## 制定Embedding层的最大输入长度，以便后面将嵌入输入展平。Embedding层激活的形状为(samples, maxlen, 8)
model.add(Embedding(10000, 8, input_length=maxlen))

## 将三维的嵌入张量展平成形状为(samples, maxlen * 8)的二维张量
model.add(Flatten())

## 在上面添加分类器
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
# print a summary representation of model
# https://keras.io/models/about-keras-models/
model.summary()

history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_split=0.2)
                    
                    

# 一脸懵逼……