# 任务：模拟从100张卡片(上面编号1-100)中抽取10张卡片，每次抽完取一个平均数，抽100000次，再取10000个平均数的平均数和标准差（标准误）

# 加载包"numpy"作为"np"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 这一行是什么意思？
np.random.seed(100)

# copy from https://www.jianshu.com/p/ee43c55123f8🚧
# jupyter 的魔术关键字（magic keywords）
# 在文档中显示 matplotlib 包生成的图形
# 设置图形的风格
%matplotlib inline 
%config InlineBackend.figure_format = 'retina'

# 生成表格：1至100，转换成数列，赋给变量population
list01 = []
for i in range(1, 101):
    list01.append(i)
population = np.array(list01)

print("这是100个数据：\n", population)
# 给序列population求平均数
print("平均数：", population.mean())
# 给序列population求标准差
print("标准差：", population.std())
print("标准误理论值：std/√10 = ", population.std() / np.sqrt(10))

#num = input("\n下面进行抽样，请输入抽样次数：")
# 重复抽取num次该样本量的样本
sample = np.random.choice(population, size=(100000, 10)).mean(axis=1)
# 计算num个样本所代表的分布的均值和标准差
print("样本均值分布的均值：", sample.mean())
print("样本均值分布的标准差：", sample.std())