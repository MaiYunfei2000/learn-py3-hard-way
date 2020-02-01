##### 2.1 初识神经网络
#### 代码清单2-1 加载Keras中的MNIST数据集
"""
作者：只是给个示例，现在不用搞懂一些像是魔法一样的内容。
"""

# 从 keras库的datasets模块导入mnist模块
from keras.datasets import mnist

## 哼，看来之后的代码宽度上限都设为90好了
## 执行了模块mnist的load_data函数，看起来这个函数会返回一个元素为二元组的二元组
    ## 二元组的每个元素（里面的二元组）都是数据集的图像和相应标签
    ## 真好奇mnist.py的代码呢，之后去看一看
## 将mnist数据集里的训练数据和测试数据加载至这些元组里
    ## 数据集从 https://s3.amazonaws.com/img-datasets/mnist.npz 下载
    ## ⚠️第一次需要联网，并且要翻墙，并且要取消全局证书验证，否则会报错 urllib.error.URLError: urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]，方法是：
        ## import ssl
        ## ssl._create_default_https_context = ssl._create_unverified_context
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

## keras里已经载入numpy库了
## 这个变量是个NumPy的ndarray呢
## 获取train_images的维度信息
    # 更多细节：[numpy.ndarray.shape — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html)
print(train_images.shape)
## 返回(60000, 28, 28)，也就是说这里有60000个28*28的黑白位图

print(len(train_labels))
## 返回60000，也就是相对应地有60000个标签

print(train_labels)
## "dtype=uint8"是什么意思？

#### 代码清单 2-2 网络架构

from keras import models
from keras import layers

# 「层」(layer)是神经网络的核心组件。
# 「层」从输入数据中提取「表示」——我们期望这种表示有助于解决手头的问题。
# 多数深度学习都是将简单的「层」链接起来，从而实现渐进式的「数据蒸馏」(data distillation)。

# 本例中的网络包含两个 Dense 层，它们是密集连接（「全连接」）的神经层。

## 官方文档首页的大开头就见到了Sequential()，这究竟是什么神仙？
## 可能是一类神经网络的初始的、空白的框架
## 通过这种方式可以迅速创建这类神经网络的一个对象，在这里这个对象就是network
network = models.Sequential()
## 给神经网络network增加一层，是一个有着512个节点的Dense层，激活方式为'relu'
    ## 输入形状这个参数的(28*28,)是什么意思呢？也许里面是个向量，向量的每个元素是一个28元组
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
# 第二层即最后一个层是一个 10 路 softmax 层，将返回一个总和 1 的十个概率值组成的数组。
network.add(layers.Dense(10, activation='softmax'))



#### 代码清单 2-3 编译步骤

# 要训练网络，还需要选择「编译」(compile)步骤的三个参数：
    # 「损失函数」(loss function)
    # 「优化器」(optimizer)
    # 「指标」(metric)

## 这个编译方式真的好傻瓜诶……
## 「交叉熵」是什么？
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])



#### 代码清单 2-4 准备图像数据

# 开始训练之前，对数据进行预处理，将其变换为网络要求的形状，并将所有值缩放到[0,1]区间。
# 由上一个练习的操作可知，训练图像保存在一个 uint8 类型的数组中
    # 形状为 (60000, 28*28) ，取值区间为[0,255]
# 需要将其变换为一个 float32 数组，形状不变但取值范围变为[0,1]

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255



#### 代码清单 2-5 准备标签

# 第 3 章会对此进行解释

from keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)



#### 代码清单 2-6 训练并测试 （这是MYF自己加的小标题）

# 用fit方法来「拟合」(fit)模型
    # 参数依次为训练图像，训练标签，训练世代数，和？？
network.fit(train_images, train_labels, epochs=5, batch_size=128)
# 训练过程中显示的：loss为网络在训练数据上的损失，acc为网络在训练数据上的精度


## debug时间
print("shape of test_images and shape of test_labels", test_images.shape, test_labels.shape)
## 尼玛，原来是test_images = 略略略 这里打成train_images.astype了......

## 用evaluate方法来检验模型
test_loss, test_acc = network.evaluate(test_images, test_labels)

print('test_acc:', test_acc)



## 这也太友好了吧！？？才19行代码！