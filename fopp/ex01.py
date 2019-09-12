# 练习教材第一章中的实例
print("\nexample 1.3: Fibonacci sequence\n")
# 将数值0和1依次赋给变量a和b
a, b = 0, 1
while a < 10000:
    # end=''是什么意思？
    '''
    help(print)
    
    print(...)
        print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)

        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    '''
    print(a, end=',')
    # 将b和a+b的值依次赋给变量a和b
    a, b = b, a + b

'''    
print("\nexample 1.4: draw a set of concentric circles using \{turtle\}\n")

import turtle

turtle.pensize(2)
turtle.circle(10)
turtle.circle(20)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)
print('try different shapes!')
'''

# 更多关于turtle模块
# [turtle --- 海龟绘图 — Python 3.7.4 文档](https://docs.python.org/zh-cn/3/library/turtle.html?highlight=turtle#module-turtle)

print("\nexample 1.5: output the date and time of this computer\n")

# 为什么调用这个或其它一些模块需要用from，而另一些不用？
from datetime import datetime

now = datetime.now()
print(now)
# 注释掉这两行代码啥都没变……可能是因为我这里的日期格式本来就是中国的
now.strftime("%x")
now.strftime("%X")
# [time --- 时间的访问和转换 — Python 3.7.4 文档](https://docs.python.org/zh-cn/3/library/time.html?highlight=strftime#time.strftime)

# [datetime --- 基本的日期和时间类型 — Python 3.7.4 文档](https://docs.python.org/zh-cn/3/library/datetime.html?highlight=datetime#module-datetime)

print('more practice: 1 ', end='')
print('test')