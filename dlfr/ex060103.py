import time

##### 6.1 处理文本数据

#### 6.1.3 整合在一起：从原始文本到词嵌入

### 1. 下载IMDB数据的原始文本

### 6-8 处理IMDB原始数据的标签

import os

imdb_dir = 'aclImdb'
# [os.path --- 常用路径操作 — Python 3.8.2rc1 文档](https://docs.python.org/zh-cn/3/library/os.path.html?highlight=os%20path%20join#os.path.join)
# 然而到底是什么意思……？
train_dir = os.path.join(imdb_dir, 'train')

labels = []
texts = []

# for_loop_indicator = 0 # debug use
for label_type in ['neg', 'pos']:
    dir_name = os.path.join(train_dir, label_type)
    # https://docs.python.org/zh-cn/3/library/os.html?highlight=os%20listdir#os.listdir
    # 返回一个列表，该列表包含了 path 中所有文件与目录的名称。该列表按任意顺序排列，并且不包含特殊条目 '.' 和 '..'，即使它们确实在目录中存在
    # 比如 2644_8.txt ，此列表长度为 25000 ，即列表含有 25000 个文件名
    # print("os.listdir(dir_name)", os.listdir(dir_name))
    # print("os.listdir(dir_name)[0]", os.listdir(dir_name)[0])
    for fname in os.listdir(dir_name):
        
        if fname[-4:] == '.txt':
            f = open(os.path.join(dir_name, fname))
            texts.append(f.read())
            f.close()
            if label_type == 'neg':
                labels.append(0)
            else:
                labels.append(1)
        
    # for_loop_indicator += 1 # debug use
    # print("for_loop_indicator", for_loop_indicator) # debug use
    # print("labels", labels) # debug use
    # print("texts", texts) # debug use
    # time.sleep(0.01)
    # break # debug use

# 也可先把上述模块当成一个黑箱子，只知道它把原始数据处理处理一下变成我们后面可以塞给神经网络用的数据。
# 输出变量看看长啥样就行了。🚧信息量太大，在for循环里试

# 哦，label 就是序号吧？不是，是正负情感标签
# texts 记录的是原文

### 2. 对数据进行分词

### 6-9 对IMDB原始数据的文本进行分词

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

# [Text Preprocessing - Keras Documentation](https://keras.io/preprocessing/text/)
# ↑可查看类 Tokenizer 及其方法的介绍

## 在 100 个单词后截断评论
maxlen = 100
## 在 200 个样本上训练
training_samples = 200
## 在 10000 个样本上验证
    # ？？？这么强的马？
validation_samples = 10000
## 只考虑数据集中前 10000 个最常见的单词（请注意断句：数据集'中'前10000个）
max_words = 10000

# 建立一个分词器的实例
tokenizer = Tokenizer(num_words=max_words)
# 以 texts （即） 为参数，丢给这个分词器处理
    # 具体发生了什么？？？🚧
    # [tf.keras.preprocessing.text.Tokenizer  |  TensorFlow Core v2.1.0](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#fit_on_texts)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# sequences = [[...], ..., [..., 4285], [7395, 4322, 6, 3, 1160, 4888, 32, 3374, 3, 988, 4, 8213, 3, 746, 16, 168, 712, 9, 44, 74, 28, 4, 58, 155, 511, 105, 234, 9, 382, 43, 10, 1744, 5, 856, 3031, 326, 15, 1, 19, 5, 213, 43, 8, 285, 2709, 681, 10, 241, 21, 581, 7, 7, 45, 4045, 1167, 23, 2294, 47, 23, 108, 81, 34, 178, 11, 422, 8, 285, 2709, 108, 81, 178, 5, 137, 5, 3161, 16, 11, 174, 2, 11, 226, 108, 81, 178, 5, 398, 3, 8007, 1036, 4, 11, 19, 8, 65, 1, 174, 6, 2092, 1, 625, 2, 455, 9218, 1, 19, 6, 3, 3777, 8969, 108, 25, 458, 1801, 589, 758, 260, 1431, 5, 1, 1027]]
# >>> np.array(sequences).shape
# (25000,)
"""
从结果来看，这个分词器将所有文本都分词并转换成了数字。
不过这个序列的形状仍然没有变，仍然含有 25000 条列表
"""
# 请看官方文档介绍（链接在顶部）：
# By default, all punctuation is removed, turning the texts into space-separated sequences of words (words maybe include the ' character). These sequences are then split into lists of tokens. They will then be indexed or vectorized.
# 目测 max_words 词频以外的单词会被消除，就跟标点符号（单词中的单引号除外）和空格一样

# 一句话，这个 Tokenizer 就帮你轻松搞定了文本分词工作啦，根本不用自己造轮子
# 当然，中文的话还是要召唤 jieba 了

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index)) # Found 88582 unique tokens.
# 这个 word_index 是个长度 88582 的 dict
# 词典的每个键都是一个被分离出的单词，相应的值位从 1 到 88582 的 int
#（那为什么有 88582 个？？？🚧不是说词频 10000 吗，还是说还没丢出去，只是完成了分词工作）

# 修剪表征着句子的列表的长度为 100
# 样本量没变，样本被修剪整齐了，可以直接转换成矩阵
data = pad_sequences(sequences, maxlen=maxlen) # data.shape 为 (25000, 100)

# [numpy.asarray — NumPy v1.18 Manual](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html?highlight=asarray#numpy.asarray)
    # 哦，跟 np.array(array_like) 是一样的
labels = np.asarray(labels)
print('Shape of data tensor:', data.shape) # Shape of data tensor: (25000, 100)
print('Shape of label tensor:', labels.shape) # Shape of label tensor: (25000,)

## 将数据划分为训练集和验证集，但首先要打乱顺序，因为一开始数据中的样本是排好序的
# （前 12500 为负面评论，剩余一半为正面评论）
# [numpy.arange — NumPy v1.18 Manual](https://numpy.org/doc/stable/reference/generated/numpy.arange.html?highlight=arange#numpy.arange)
    # 跟内置函数 range() 一样，只不过输出的可迭代类型为一维 array 
    # 也就是说，indeces 为 array([0, 1, ... , 24999])
indices = np.arange(data.shape[0])
# [numpy.random.shuffle — NumPy v1.18 Manual](https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html?highlight=shuffle#numpy.random.shuffle)
    # 随机“洗牌”——打乱位置
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
# 这样的索引是什么鬼，哦有点印象，高级切片玩法
# 就是以 indices 相应位置的索引所生成的新顺序输出一个张量
"""
>>> a = np.array([1, 2, 3])
>>> a
array([1, 2, 3])
>>> indices = [1, 2, 0]
>>> b = a[indices]
>>> b
array([2, 3, 1])
"""

# 然后是日常的划分训练集和验证集
x_train = data[:training_samples] # shape: (200, 100)
y_train = labels[:training_samples] # shape: (200,)
x_val = data[training_samples:training_samples+validation_samples] # shape: (10000, 100)
y_val = labels[training_samples:training_samples+validation_samples] # shape: (10000, 100)
# 咦，那就是没有充分利用数据咯？


### 3. 下载 GloVe 词嵌入

# [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)


### 4. 对嵌入进行预处理

### 6-10 解析 GloVe 词嵌入文件

# 在后续过程中构建一个将单词（字符串）映射为其向量表示（数值向量）的索引

glove_dir = 'glove.6B'

embeddings_index = {}
f = open(os.path.join(glove_dir, 'glove.6B.100d.txt'))
for line in f:
    # 将这一行文本以空格为分隔符，切割文本生成一个列表
    values = line.split()
    # 列表第0个数据是单词标记
    word = values[0]
    # 将第1个数据起的列表转换为 numpy 的 32 位浮点数数组
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))
# Found 400000 word vectors.

# 对于数据集，自己来打印打印看是怎么回事，或者去文本文档里看看
# 不，还是别打开文本文档了，电脑会卡死……
# 这是文档的第一行：
# the 0.418 0.24968 -0.41242 0.1217 0.34527 -0.044457 -0.49688 -0.17862 -0.00066023 -0.6566 0.27843 -0.14767 -0.55677 0.14658 -0.0095095 0.011658 0.10204 -0.12792 -0.8443 -0.12181 -0.016801 -0.33279 -0.1552 -0.23131 -0.19181 -1.8823 -0.76746 0.099051 -0.42125 -0.19526 4.0071 -0.18594 -0.52287 -0.31681 0.00059213 0.0074449 0.17778 -0.15897 0.012041 -0.054223 -0.29871 -0.15749 -0.34758 -0.045637 -0.44251 0.18785 0.0027849 -0.18411 -0.11514 -0.78581

# >>> embeddings_index['the']
# array([-0.038194, -0.24487 ,  0.72812 , -0.39961 ,  0.083172,  0.043953,
#        -0.39141 ,  0.3344  , -0.57545 ,  0.087459,  0.28787 , -0.06731 ,
#         0.30906 , -0.26384 , -0.13231 , -0.20757 ,  0.33395 , -0.33848 ,
#        -0.31743 , -0.48336 ,  0.1464  , -0.37304 ,  0.34577 ,  0.052041,
#         0.44946 , -0.46971 ,  0.02628 , -0.54155 , -0.15518 , -0.14107 ,
#        -0.039722,  0.28277 ,  0.14393 ,  0.23464 , -0.31021 ,  0.086173,
#         0.20397 ,  0.52624 ,  0.17164 , -0.082378, -0.71787 , -0.41531 ,
#         0.20335 , -0.12763 ,  0.41367 ,  0.55187 ,  0.57908 , -0.33477 ,
#        -0.36559 , -0.54857 , -0.062892,  0.26584 ,  0.30205 ,  0.99775 ,
#        -0.80481 , -3.0243  ,  0.01254 , -0.36942 ,  2.2167  ,  0.72201 ,
#        -0.24978 ,  0.92136 ,  0.034514,  0.46745 ,  1.1079  , -0.19358 ,
#        -0.074575,  0.23353 , -0.052062, -0.22044 ,  0.057162, -0.15806 ,
#        -0.30798 , -0.41625 ,  0.37972 ,  0.15006 , -0.53212 , -0.2055  ,
#        -1.2526  ,  0.071624,  0.70565 ,  0.49744 , -0.42063 ,  0.26148 ,
#        -1.538   , -0.30223 , -0.073438, -0.28312 ,  0.37104 , -0.25217 ,
#         0.016215, -0.017099, -0.38984 ,  0.87424 , -0.72569 , -0.51058 ,
#        -0.52028 , -0.1459  ,  0.8278  ,  0.27062 ], dtype=float32)

### 6-11 准备 GloVe 词嵌入矩阵

embedding_dim = 100

# 10000 * 100 的全零矩阵
embedding_matrix = np.zeros((max_words, embedding_dim))
for word, i in word_index.items():
    # 对于前 9999 个词：
    if i < max_words:
        # 生成嵌入词向量
        # 索引关系： word_index 的键 => embeddings_index 中相同的键 => embeddings_index 中相应的值，即嵌入词向量
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            ## 嵌入索引 (embeddings_index) 中找不到的词，其嵌入向量全为 0
            embedding_matrix[i] = embedding_vector
# 由此，就构建了一个可以加载到 Embedding 层中的嵌入矩阵

### 5. 定义模型

### 6-12 模型定义

from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense

# 新建一个 Sequential() 类的对象/实例，即新建一个线性堆叠一层层神经网络的模型
# [Guide to the Sequential model - Keras Documentation](https://keras.io/getting-started/sequential-model-guide/)
model = Sequential()
# 这个 Embedding 层输出的矩阵含有 10000 词频，输出数据的嵌入维度为 100 ， 
# 输入向量的维度为 100
model.add(Embedding(max_words, embedding_dim, input_length=maxlen))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()


### 6. 在模型中加载 GloVe 嵌入

### 6-13 将预训练的词嵌入加载到 Embedding 层中

model.layers[0].set_weights([embedding_matrix])
## 冻结 Embedding 层：不应在训练时更新预训练的部分，以免丢失它们所保存的信息
## 随机初始化的层会引起较大的梯度更新，会破坏已经学到的特征
model.layers[0].trainable = False


### 7. 训练模型与评估模型

### 6-14 训练与评估

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['acc'])
history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_data=(x_val, y_val))
model.save_weights('pre_trained_glove_model.h5')


### 6-15 绘制结果

import matplotlib.pyplot as plt

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()

### 6-16 至 6-18 略