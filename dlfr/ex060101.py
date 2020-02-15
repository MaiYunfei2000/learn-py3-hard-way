##### 6.1 处理文本数据

#### 6.1.1 单词和字符的one-hot编码

### 6-1 单词级的one-hot编码（简单示例）

## 「标记」(token)：分解文本得到的单元（单词、字符或n-gram）

import numpy as np

## 初始数据：每个样本是列表的一个元素（本例中的样本是一个句子，但也可以是一整篇文档）
samples = ['The cat sat on the mat.', 'The dog ate my homework.']

## 构建数据中所有标记的索引
token_index = {}
# 对于样本列表中的每一个样本（字符串）：
for sample in samples:
    ## 利用split方法对样本进行分词。在实际应用中还需要去掉标点和特殊字符
    for word in sample.split():
        if word not in token_index:
            ## 为每个唯一单词指定一个唯一索引。注意，没有为索引编号0指定单词❓为什么
            # 给字典token_index添加一个键值对，键为word，值为之前的字典长度+1
            token_index[word] = len(token_index) + 1

print(token_index)

## 对样本进行分词。只考虑单个样本前max_length个单词
max_length = 10

## 将结果保存在results中
# 创建3D零张量，形状为(样本集长度,指定的最大单词数,标记的数目+1)
results = np.zeros(shape=(len(samples), # 样本轴，此例中此轴就两个维度
                          max_length,
                          max(token_index.values()) + 1))

# 按顺序枚举samples的元素，将索引数和元素分别赋给i和sample
    # 即(0, 'The cat sat on the mat.')和(1, 'The dog ate my homework.')
        # （注意，enumerate object里的元素要转换成常见序列类型才能打印出来）
for i, sample in enumerate(samples):
    # 将sample分割成一个个词汇，经枚举转换为列表，并取10个元素
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index = token_index.get(word)
        # くその Python indexing，哼！真得去补课了
        # 以i、j、index分别作为0、1、2轴的索引，对相应位置的元素赋值1.0
        # 如果前面有个地方不+1的话就会IndexError: index 10 is out of bounds for axis 2 with size 10
        results[i, j, index] = 1.

# 可以看到一个个句子被转化为2D张量了
    # 第1轴为单词的位置
    # 第2周围单词的编码
print(results)



### 6-2 字符级的one-hot编码（简单示例）

import string

samples = ['The cat sat on the mat.', 'The dog ate my homework.']
# string.printable是字符串'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'即所有可打印的ASCII字符
characters = string.printable
token_index = dict(zip(characters, range(1, len(characters) + 1)))

max_length = 50
# shape: 样本数，最大长度即截取句子的字符数即50，标记数+1即101
results = np.zeros((len(samples), max_length, max(token_index.values()) + 1))
# 对于样本集的每一个样本索引及样本：
for i, sample in enumerate(samples):
    # 对于样本的每一个字符
    for j, character in enumerate(sample[:max_length]):
        index = token_index.get(character)
        results[i, j, index] = 1.

print(results.shape)
# 每个句子是一个2D张量（50*101矩阵）
    # 第1轴（长度50）为字符的位置，cat这句话有23个字符，从第23行（以0为始）开始就是0向量，下面的几行print验证了推理
    # 第2轴为字符的编码
# 打印首个句子的首个单词的首个字即“T”，可见第56个（起始为0）元素为1
test = [results[0][23+i]==results[0][24+i] for i in range(26)]
print(all(results[0][22]==results[0][23]))
print(all(results[0][23]==results[0][24]))
print(np.array(test).all())
# 哇TAT设计几行代码证明这个结论这么烧头发

# 这个例子与前面例子相比就是token的长度不同，前者为单词，这里为字符



### 6-3 用Keras实现单词级的one-hot编码

from keras.preprocessing.text import Tokenizer

samples = ['The cat sat on the mat.', 'The dog ate my homework.']

## 创建一个分词器（tokenizer），设置为只考虑前1000个最常见的单词
tokenizer = Tokenizer(num_words=1000)
## 构建单词索引
tokenizer.fit_on_texts(samples)

## 将字符串转换为整数索引组成的列表
sequences = tokenizer.texts_to_sequences(samples)
print(sequences)

## 也可以直接得到one-hot二进制表示，这个分词器也支持one-hot编码外的其他向量化形式
one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')
print(one_hot_results)

print(dir(tokenizer))
print(tokenizer)
## 找回单词索引
word_index = tokenizer.word_index
print(word_index)
print('Found %s unique tokens.' % len(word_index))


### 6-4 使用散列技巧的单词级的one-hot编码（简单示例）

# 看来短时间搞不懂了，先跳过。

# https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8
# https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97
# https://baike.baidu.com/item/Hash/390310

## one-hot散列技巧(one-hot hashing trick)：one-hot编码的一种变体。如果词表中唯一标记的数量（什么意思❓）太大而无法直接处理就可以使用这种技巧。
    ## 优点：避免维护一个显式的单词索引，从而节省内存并允许数据的在线编码（读取完所有数据之前就可以立刻生成标记向量）
    ## 缺点：可能出现散列冲突(hash collision)，即两个不同单词可能具有相同散列值

samples = ['The cat sat on the mat.', 'The dog ate my homework.']

## 将单词保存为长度为1000的向量。如果单词数量接近1000个（或更多），那么会遇到很多散列冲突，会降低这种编码方法的准确性
dimensionality = 1000
max_length = 10

results = np.zeros((len(samples), max_length, dimensionality))
for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        ## 将单词散列为0~1000范围内的一个随机整数索引
        # ???????
        index = abs(hash(word)) % dimensionality
        results[i, j, index] = 1.

print(list(results[0][0]))