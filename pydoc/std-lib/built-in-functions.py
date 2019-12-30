# 内置函数
# https://docs.python.org/zh-cn/3/library/functions.html

print('\n✨map()')
# map(function, iterable, ...): 返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器。 如果传入了额外的 iterable 参数，function 必须接受相同个数的实参并被应用于从所有可迭代对象中并行获取的项。 当有多个可迭代对象时，最短的可迭代对象耗尽则整个迭代就将结束。 对于函数的输入已经是参数元组的情况，请参阅 itertools.starmap()。
# 这里的function参数是lambda x: x**2，相当于f(x)=x²
# iterable参数是range(10)，也就是整数0至9的range类型
squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares = list(map(lambda x, y: x**2, range(10), 
                   [233, 23, 22, 33]))
print(squares)
squares = list(map(lambda x, y: (x**2, y), range(10), 
                   [233, 23, 22, 33]))
print(squares)
print(type(squares))
print(type(squares[0]))