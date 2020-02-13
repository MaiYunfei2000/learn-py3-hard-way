##### 3.6

#### （接上）改进验证过程

from keras.datasets import boston_housing

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

#### 3.6.2 准备数据

### 3-25 数据标准化


mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std

#### 3.6.3 构建网络

### 3-26 模型定义

from keras import models
from keras import layers

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model

#### 3.6.4 使用K折验证来验证你的方法

### 3-27 K折验证
### 3-28 保存每折的验证结果

import numpy as np

k = 4
num_val_samples = len(train_data) // k
# 这两行改动了：世代数改变，mae的变量名改变
num_epochs = 500
all_mae_histories = []

for i in range(k):
    print('processing fold #', i)
    val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
    val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]
    
    partial_train_data = np.concatenate(
        [train_data[:i * num_val_samples],
         train_data[(i + 1) * num_val_samples:]],
        axis=0)
    partial_train_targets = np.concatenate(
        [train_targets[:i * num_val_samples],
         train_targets[(i + 1) * num_val_samples:]],
        axis=0)
    
    model = build_model()
    # 这里开始变了
    history = model.fit(partial_train_data, partial_train_targets,
              validation_data=(val_data, val_targets),
              epochs=num_epochs, batch_size=1)
    history_dict = history.history
    mae_history = history_dict['val_mae']
    all_mae_histories.append(mae_history)

### 3-29 计算所有轮次中K折验证分数平均值

average_mae_history = [
        np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]
# 相当于：
while True:
    break
    average_mae_history = []
    for i in range(num_epochs):
        temp = []
        for x in all_mae_histories:
            temp.append(x[i])
        average_mae_history.append(np.mean(temp))

### 3-30 绘制验证分数
import matplotlib.pyplot as plt

plt.plot(range(1, len(average_mae_history) + 1), average_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()

### 3-31 绘制验证分数（删除前10个数据点）

## 因为前10个值太高了，影响对整个曲线的观察

def smooth_curve(points, factor=0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points

smooth_mae_history = smooth_curve(average_mae_history[10:])

plt.plot(range(1, len(smooth_mae_history) + 1), smooth_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()

## 可看出，验证MAE在80轮之后不再显著降低，之后就开始过拟合
## 继续调参之后可训练最终的生产模型（略）

### 3-32 训练最终模型

model = build_model()
model.fit(train_data, train_targets,
          epochs=80, batch_size=16, verbose=0)
test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)

print(test_mae_score)