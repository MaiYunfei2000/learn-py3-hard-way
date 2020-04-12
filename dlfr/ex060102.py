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
    # 标记个数、最大单词索引是什么意思？+1是为什么？🚧
        # 哦，标记应该就是官方文档中的 index 。
    # 嵌入的维度又是什么意思？这个因素会影响什么？🚧
# 创建一个类Embedding的对象
embedding_layer = Embedding(1000, 64)
# 不知道是原作还是翻译的锅，还是看官方文档好懂……
    # 1000 就是只能有 1000 种词，64 就是 Embedding 层输出的张量的第2轴的维度数。

# print(embedding_layer)

# https://keras.io/layers/embeddings/
# keras.layers.Embedding(input_dim, output_dim, embeddings_initializer='uniform', embeddings_regularizer=None, activity_regularizer=None, embeddings_constraint=None, mask_zero=False, input_length=None)
    # Turns positive integers (indexes) into dense vectors of fixed size（将正整数（索引——比如说单词索引，MYF注）们转换为特定 size 的密集向量）. eg. [[4], [20]] -> [[0.25, 0.1], [0.6, -0.2]] 显然，这里二维变成三维了。（为什么后者相较前者是 dense 的？🚧）
    # This layer can only be used as the first layer in a model.
    
    # input_dim: int > 0. Size of the vocabulary, i.e. maximum integer index + 1.
    # output_dim: int >= 0. Dimension of the dense embedding.
    # 其它参数的说明略。

"""官方的例子：
model = Sequential()
model.add(Embedding(1000, 64, input_length=10))
# the model will take as input an integer matrix of size (batch, input_length). （也就是 (1000, 64) 咯？不对，1000的意思不是这个，见下一行。）
# the largest integer (i.e. word index) in the input should be
# no larger than 999 (vocabulary size). 噢，原来是这个意思。也就是说，这限制了输入的张量中的元素只能是0~999的整数（也就是说最多有1000种单词）。
# now model.output_shape == (None, 10, 64), where None is the batch dimension.

input_array = np.random.randint(1000, size=(32, 10))
# 生成元素值为 1000 以下的随机数矩阵，形状为32*10
# https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.random.randint.html

model.compile('rmsprop', 'mse')
output_array = model.predict(input_array)
assert output_array.shape == (32, 10, 64)

>>> output_array.shape
(32, 10, 64)

# 发现了什么没有？只考虑形状的话，
# 这个 3D 张量就是由 64 个 2D 张量叠成的一个“长方体”。

"""

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

print("x_train[0]:", x_train[0])
print("y_train:", y_train)
print("x_train.shape, y_train.shape:", x_train.shape, y_train.shape)

## 将整数列表转换成形状为(samples, maxlen)的二维整数张量
# https://keras.io/preprocessing/sequence/ 然后手动查找 pad_sequences
    # pad_sequences(sequences, maxlen=None, dtype='int32', padding='pre', truncating='pre', value=0.0)
    # 这个函数将[具有num_samples个整数序列（列表）]的列表 transforms 为一个形状为 (num_samples, num_timesteps) 的 2D NumPy array 。
    # 如果提供了 maxlen 参数的值， num_timesteps 值就是 maxlen 值，否则，则是最长的那条序列的长度。
    # 长度小于 num_timesteps 的序列会填补上 value 值（默认为0）。例如 maxlen=5，而某列表中的某条序列是 [2, 3, 3]，那么这个序列会变成 [2, 3, 3, 0, 0]（不一定是在后面填补，见下一行）。
    # 长度大于 num_timesteps 的序列则会被截断，至于怎么截断（在哪个位置截断）则依次取决参数 truncating，补全（见上一行）的方式则取决于 padding 参数。这两个参数的值默认都是 'pre' 。
        # padding 参数：'pre'在前面填补；'post'在后面填补。
        # truncating 参数：'pre'切割掉前面的；'post'切割掉后面的。
    """你捣鼓捣鼓就明白了：
    >>> a = [[1,1,1]]
    >>> a_i = preprocessing.sequence.pad_sequences(a, maxlen=5)
    >>> a_i
    array([[0, 0, 1, 1, 1]], dtype=int32)
    >>> a_ii = preprocessing.sequence.pad_sequence(a, maxlen=5, padding='post', value=3.0)
    >>> a_ii = preprocessing.sequence.pad_sequences(a, maxlen=5, padding='post', value=3.0)
    >>> a_ii
    array([[1, 1, 1, 3, 3]], dtype=int32)
    >>> preprocessing.sequence.pad_sequences(a_ii, maxlen=2, truncating='post')
    array([[1, 1]], dtype=int32)
    """
# maxlen就是前面设定的那个20。这里把第1轴形状变为20，也就是指截取文本的前20个单词吗？还是会干什么（某种形式的压缩）？
    # 截取文本的前20个单词。
    # 为什么是这样子做？为什么是20而不是其它？为什么是截掉后面的，而不是截掉前面的？🚧
# sample呢？这里就是指训练集（下一行）和测试集（下下行）的样本量
x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)
# print("x_train:", x_train)
# print(type(x_train))
# print("x_train.shape[0] == y_train.shape[0]:", x_train.shape[0] == y_train.shape[0])

# 怎么将原张量转换为现在这个新的整数张量呢？发生了什么？这样的编码形式可以表示出什么/具有什么意义？
    # 就是为了压缩数据的“稠密度”，给机器减负。
    # 原本的 one-hot 形式的编码中，一个个向量的长度有一万两万之多
        # （长度的大小如何取决于你想让神经网络有多大的词汇量），
        # 然后把其中一个 0 标记为 1，就让这个向量指代一个单词。
        # （你应该还记得， MNIST 里面的数字的表征用的也是 one-hot 编码。)
        # 于是，这样多折腾电脑啊！

# 前后样本轴（第0轴）没有发生变化，只是第1轴变化了
# 那第1轴发生了什么呢？哦，解决了，看前面 pad_sequences() 注释。

# 原来就是这样嘛！所以要认真阅读官方文档！根本就不复杂不玄乎！



### 6-7 在IMDB数据上使用Embedding层和分类器

from keras.models import Sequential
from keras.layers import Flatten, Dense, Embedding

model = Sequential()
## 制定Embedding层的最大输入长度，以便后面将嵌入输入展平。Embedding层激活的形状为(samples, maxlen, 8)
# 输入张量有10000的词汇量，输出张量的第2轴具有8个维度，输入张量的第1个轴有maxlen及20个维度
model.add(Embedding(10000, 8, input_length=maxlen))

## 将三维的嵌入张量展平成形状为 (samples, maxlen * 8) 的二维张量
# 这个 Flatten 层紧随 Embedding 层其后，
    # 接收 Embedding 层的输入作为 Flatten 层的输出。
model.add(Flatten())
# 这个层到底是干什么的呢？
# https://keras.io/layers/core/ 搜索 Flatten
# keras.layers.Flatten(data_format=None)
    # Flattens the input. Does not affect the batch size.
    # 例子：
    """
    model = Sequential()
    model.add(Conv2D(64, (3, 3),
                     input_shape=(3, 32, 32), padding='same',))
    # now: model.output_shape == (None, 64, 32, 32)

    model.add(Flatten())
    # now: model.output_shape == (None, 65536)
    """
# 为什么要展平成二维张量呢？因为神经网络只能接收一维张量鸭！



## 在上面添加分类器
model.add(Dense(1, activation='sigmoid'))
# 我已经疑惑很久了， Dense 层是干什么的？
# https://keras.io/layers/core/ 第一个模块就是 Dense
# keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
# Just your regular densely-connected NN layer. （只是常规的紧密连接的神经网络层。）
    # 噢，我懂了！这玩意就是一个普普通通的层。比如说 MNIST 数据集用到经典神经网络的最后一层就是酱紫的东西！它就单纯再用 Sigmoid 激活函数处理一次信息就吐出去了，不会有什么花里胡哨的奇怪东西！

# 编译模型
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
# print a summary representation of model
# https://keras.io/models/about-keras-models/
model.summary()

history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_split=0.2)
                    
                    

# 一脸懵逼……

# 两个月后再来重新理了一遍，不懵逼啦！！！ 200412