# Python配置不完全指南

只是把我的行动痕迹沉淀一下而已。

原始帖：[MacOS下的Python配置一条龙 · Issue #2 · MaiYunfei2000/trail-learn-py](https://github.com/MaiYunfei2000/trail-learn-py/issues/2)

后面更新东西直接就在这里改动了。

---

其实对于我这样的小白也不需要干特别多的复杂事情。也就是去官网（homebrew也行）安装python3，然后安装（或升级）pip3，然后用pip3安装一堆堆的Python模块。

## 安装PIP

参考：

- [如何在mac版本的python里安装pip？ - 知乎](https://www.zhihu.com/question/50470150)
- [Mac OSX同时安装Python 2.7和Python3.6及常见问题解决 - 简书](https://www.jianshu.com/p/deb70bd6a555)

Python2(>=2.7)和Python3(>=3.6)里已经自带了pip。不过就像输入`python`会运行python2.7一样，只输入`pip`也运行的是python2.7对应的pip而非3.6的。在运行python3.6时要输入`python3.6`一样，运行python3对应的pip也一定要输入`pip3`。否则会提示：

> DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.

## 然后

在终端或类似的软件用pip安装一堆堆东西。

具体代码放在这供懒懒的小盆友复制粘贴。

将pip3更新至最新版：  
`pip3 install --upgrade pip`

安装各种东西：
```
pip3 install nose
pip3 install jupyter
pip3 install pandas
pip3 install numpy
pip3 install matplotlib
pip3 install seaborn
pip3 install scikit-learn
pip3 install tensorflow
pip3 install scrapy
pip3 install jieba
pip3 install pillow
pip3 install pyinstaller
pip3 install requests
pip3 install beautifulsoup4
```

其他玩法：

* [pip 批量安装 - Google Search](https://www.google.com/search?q=pip+%E6%89%B9%E9%87%8F%E5%AE%89%E8%A3%85&oq=pip+%E6%89%B9%E9%87%8F%E5%AE%89%E8%A3%85&aqs=chrome..69i57.5980j0j7&sourceid=chrome&ie=UTF-8)
* [python pip批量安装扩展包 - vb112479 - CSDN博客](https://blog.csdn.net/qq_18525247/article/details/79553499)

列出当前安装的包：
`pip3 list`

列出可升级的包：
`pip3 list --outdate`

升级一个包：
`pip3 install --upgrade xxx`(“xxx”为相应的包)

## changelog

190913 把旧帖子的内容搬运至md文档；补充一些pip指令。
