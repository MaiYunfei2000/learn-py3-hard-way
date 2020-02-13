##### 3.6 预测房价：回归问题

#### 3.6.1 波士顿房价数据集

from keras.datasets import boston_housing

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

"""
>>> train_data.shape
(404, 13)
>>> test_data.shape
(102, 13)
>>> train_targets
array([15.2, 42.3, 50., ..., 29.1])
"""
## 每个样本有13个数值特征，如人均犯罪率、每个住宅的平均房间数、高速公路可达性等



#### 3.6.2 准备数据

### 3-25 数据标准化

# 标准化训练数据：
# 就是统计上的标准化，对x进行(x - x_bar) / std得到标准分数z
# 沿着train_data的第0轴（一列列地）求均值
    # 关于mean：[numpy.mean — NumPy v1.18 Manual](https://numpy.org/doc/1.18/reference/generated/numpy.mean.html)
    # 关于axis[Numpy axes explained - Sharp Sight](https://www.sharpsightlabs.com/blog/numpy-axes-explained/)
mean = train_data.mean(axis=0)
train_data -= mean
# 沿着train_data的第0周求标准差
std = train_data.std(axis=0)
# 整体除以标准差，训练数据标准化完成
train_data /= std

# 同理，标准化测试数据
## 切记，测试数据也应当使用训练数据来标准化
test_data -= mean
test_data /= std



#### 3.6.3 构建网络

### 3-26 模型定义

from keras import models
from keras import layers

## 此次样本数据少。训练数据越少，过拟合会越严重。因此搭建较小的网络。

## 因为需要将同一个模型多次实例化，所以用一个函数来构建模型。
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           # 以train_data第1轴的shape即13作为第一层的节点数
                           input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    ## 线性层。标量回归的典型设置。不会限制输出范围。
    model.add(layers.Dense(1))
    ## mse: 均方误差(mean squared error)，即标准误的平方
        ## 标准误的意义什么来着？？？？？？🚧记得翻回统计书
    ## mae: 平均绝对误差(mean absolute error)，|y^ - y|的均值
        ## 比如这次得到MAE等于0.5，表示预测的房价与实际房价平均相差 0.5千 美元
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model



#### 3.6.4 使用K折验证来验证你的方法

## 由于数据少，验证集会很小。因此验证分数可能会有很大波动，取决于所选的验证集和训练集。也就是说，验证集的划分方式可能会造成验证分数有很大的方差。
## K折交叉验证可将数据分为K个分区（K常取4或5）。每次在模型的K-1个分区上训练，剩余1个分区用于测试。共重复K次，取K个验证分数的平均值。

### 3-27 K折验证

import numpy as np

k = 4
# k分train_data的长度，也就是每一折的样本有101个
num_val_samples = len(train_data) // k
# ?
num_epochs = 100
all_scores = []

# 在第i折训练与验证中
for i in range(k):
    print('processing fold #', i)
    # 验证数据。切片下限为i * num_val_samples，切片上限为(i + 1) * num_val_samples
    val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
    # 验证标签同理
    val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]
    
    # 训练数据和训练标签：余下全部分区的数据（就是上面验证数据的区间的补集）
        # [numpy.concatenate — NumPy v1.18 Manual](https://numpy.org/doc/1.18/reference/generated/numpy.concatenate.html)
            # 沿着（默认）axis=0来拼接两段数组
            # 可理解为seq.join()的推广
    partial_train_data = np.concatenate(
        [train_data[:i * num_val_samples],
         train_data[(i + 1) * num_val_samples:]],
        axis=0)
    partial_train_targets = np.concatenate(
        [train_targets[:i * num_val_samples],
         train_targets[(i + 1) * num_val_samples:]],
        axis=0)
    
    ## 构建Keras模型（已编译）
    model = build_model()
    ## verbose=0: 静默模式 （可是是什么意思❓哦，训练或测试时不显示即时进度）
        # 你看，末尾删掉verbose=0就回复即时状态显示了
    model.fit(partial_train_data, partial_train_targets,
              epochs=num_epochs, batch_size=1)
    # https://keras.io/models/model/#evaluate
        # 依次返回loss和metrics
    val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=0)
    all_scores.append(val_mae)

print(all_scores)
# 注意区分：mean作为属性和作为方法（类比s.sort()与sorted(s)的区别）
print(np.mean(all_scores))
# 在2~3之间，即2000~3000美元，这个预测值和实际值的偏差还是挺大