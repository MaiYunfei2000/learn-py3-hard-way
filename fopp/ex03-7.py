# 3.7 实例4：文本进度条

import time
# Python标准库——通用操作系统服务，详见https://docs.python.org/zh-cn/3/library/time.html

"""

## 3.7.1 简单的开始

scale = 10
print("------开始------")
for i in range(scale+1):
    # '**'的个数，从0至10
    a = '**' * i
    # '..'的个数，从10至0
    b = '..' * (scale - i)
    # 动态变化的百分数
    c = (i/scale) * 100
    print("%{:^3.0f}[{}->{}]".format(c, a, b))
    # 程序挂起0.04秒，也就是0.04秒后才继续往下执行代码
    time.sleep(0.04)
print("------结束------")

## 3.7.2 单行动态刷新

for i in range(101):
    # 
    # \r：把输出指针移动到行首而不换行
    # end=""：以空字符结束，不然就跳行了
    print("\r{:2}%".format(i), end="")
    time.sleep(0.04)

print()

"""

## 3.7.3 带刷新的文本进度条

scale = 50
# str.center：https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=center#str.center
# 返回长度为scale与2的浮数即25的字符串，“开始”位于字符串中间，剩余部分使用“-”填充（默认为空格；如果第一个参数小于len(str)则返回str本身）
print("开始".center(scale//2,'-'))
# ?
t = time.clock()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    t -= time.clock()
    # {:^3.0f}: 动态变化的百分数进度c; 
        # ^: 居中; 3: 3位字符串; .0f: ，取0位小数
    # {:2.f}: 伪时间显示，取2位小数
    print("\r{:>3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),
        end='')
    time.sleep(0.05)
print()
print("结束".center(scale//2, '-'))