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

for label_type in ['neg', 'pos']:
    dir_name = os.path.join(train_dir, label_type)
    # https://docs.python.org/zh-cn/3/library/os.html?highlight=os%20listdir#os.listdir
    # 返回一个列表，该列表包含了 path 中所有文件与目录的名称。该列表按任意顺序排列，并且不包含特殊条目 '.' 和 '..'，即使它们确实在目录中存在
    # 这个列表没有套娃
    print(os.listdir(dir_name))
    print(os.listdir(dir_name)[0])
    
    for fname in os.listdir(dir_name):
        if fname[-4:] == '.txt':
            f = open(os.path.join(dir_name, fname))
            texts.append(f.read())
            f.close()
            if label_type == 'neg':
                labels.append(0)
            else:
                labels.append(1)

### 2. 对数据进行分词

### 6-9 对IMDB原始数据的文本进行分词

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np