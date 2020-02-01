##### 2.1 初识神经网络
#### 代码清单2-1 加载Keras中的MNIST数据集
"""
作者：只是给个示例，现在不用搞懂一些像是魔法一样的内容。
"""

# 从 keras库的datasets模块导入mnist模块
from keras.datasets import mnist

# 哼，看来之后的代码宽度上限都设为90好了
# 执行了模块mnist的load_data函数，看起来这个函数会返回一个元素为二元组的二元组
    # 二元组的每个元素（里面的二元组）都是数据集的图像和相应标签
    # 真好奇mnist.py的代码呢，之后去看一看
# 将mnist数据集里的训练数据和测试数据加载至这些元组里
    # 数据集从 https://s3.amazonaws.com/img-datasets/mnist.npz 下载
    # ⚠️第一次需要联网，并且要翻墙，并且要取消全局证书验证，否则会报错 urllib.error.URLError: urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]，方法是：
        # import ssl
        # ssl._create_default_https_context = ssl._create_unverified_context
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# keras里已经载入numpy库了
# 这个变量是个NumPy的ndarray呢
# 获取train_images的维度信息
    # 更多细节：[numpy.ndarray.shape — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html)
print(train_images.shape)
# 返回(60000, 28, 28)，也就是说这里有60000个28*28的黑白位图

print(len(train_labels))
# 返回60000，也就是相对应地有60000个标签

print(train_labels)
# "dtype=uint8"是什么意思？