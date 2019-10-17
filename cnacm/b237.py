# 2.3.7 绘制数组

# 使用颜色显示3*2数组，具有相同值的数组单元颜色也相同

import matplotlib.pyplot as plt
import numpy as np

a = np.zeros([3,2])
a[0,0] = 1
a[0,1] = 2
a[1,0] = 9
a[2,1] = 12

# %matplotlib inline
# 上一行代码似乎是专门针对IPython的，目的是在Notebook上绘制图形而非在独立的外部窗口中

# imshow()为创建绘图的指令
# interpolation：告诉Python不要为了让绘图看起来更平滑而混合颜色（然而注释掉了也没变化鸭？？）
plt.imshow(a, interpolation='nearest')
# 如果没有下一行代码的话，小火箭出现一下又消失了，不知道具体怎么理解
plt.show() # 删掉前面代码而使用plt.show(a)会报错