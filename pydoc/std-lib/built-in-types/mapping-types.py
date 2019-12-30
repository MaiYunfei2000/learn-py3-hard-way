##### Mapping Types (映射类型) -- dict
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

"""
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
返回一个新的字典，基于可选的位置参数❓和可能
为空的关键字参数❓集来初始化。

如果没有给出位置参数，将创建一个空字典。 
如果给出一个位置参数并且其属于映射对象，将
创建一个具有与映射对象相同键值对的字典。 
否则的话，位置参数必须为一个 iterable 
对象。 该可迭代对象中的每一项本身必须为一
个刚好包含两个元素的可迭代对象。 每一项中
的第一个对象将成为新字典的一个键，第二个对
象将成为其对应的值。 如果一个键出现一次以
上，该键的最后一个值将成为其在新字典中对应
的值。

如果给出了关键字参数，则关键字参数及其值会
被加入到基于位置参数创建的字典。 如果要加
入的键已存在，来自关键字参数的值将替代来
自位置参数的值。
"""

# 以下示例返回的字典均等于{"one": 1, "two": 2, "three": 3}

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
# 将dict()里面的zip object转换为dict object
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# dict()里面是一个有着三个元素的列表，每个元素都是二元组
d = dict([('two', 2), ('one', 1), ('three', 3)])
# 键值对的输入顺序不同，仍是同一字典
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

# list(d): 返回字典 d 中使用的所有**键**的列表。
print(list(d))


# len(d): 返回字典 d 中的项数。
print(len(d))


# d[key]: 返回d中以key为键的项。如果映射中不存在key则会引发KeyError
print(d['one'])


# d[key] = value: 将d[key]设为value。
d['one'] = '壹'
print(d['one'])


# key in d: 如果 d 中存在键 key 则返回 True，否则返回 False。
print('two' in d)


# key not in d: 等价于not key in d
print('two' not in d)


# iter(d): 返回以字典的键为元素的迭代器。 这是 iter(d.keys()) 的快捷方式。
iterable = iter(d)
print(iterable)
print(type(iterable))
print(list(iterable))


# clear(): 移除字典中的所有元素。
e.clear()
print(e)


# copy(): 返回原字典的浅拷贝。(浅拷贝是什么意思❓)
e = d.copy()
print(e)


# get(key[, default]): 如果 key 存在于字典中则返回 key 的值，否则返回 default。 如果 default 未给出则默认为 None，因而此方法绝不会引发 KeyError。
print(d.get('one'))
print(d.get('one', "啊蛤♂???"))
print(d.get('four'))
print(d.get('four', "啊蛤♂???"))


# items(): 返回由字典项 ((键, 值) 对) 组成的一个新视图。 参见[视图对象文档](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict-views)
print(d.items())
print(type(d.items()))
f = list(d.items())
print(f)
print(type(f[0]))
g = dict(f)
print(type(g), g)

# keys(): 返回由字典键组成的一个新视图。 参见 视图对象文档。
print('💡💡💡💡💡')
print(d.keys())
print(list(d.keys()))
print('💡💡💡💡💡')

# pop(key[, default]): 如果 key 存在于字典中则将其移除并返回其值，否则返回 default。 如果 default 未给出且 key 不存在于字典中，则会引发 KeyError。
try:
    g1 = g.pop('one')
    g2 = g.pop('five', "ohhh")
    g3 = g.pop('four')
except KeyError:
    print("KeyError")
print(g1, g2)


# popitem(): 从字典中移除并返回一个 (键, 值) 对。 键值对会按 LIFO 的顺序被返回。popitem() 适用于对字典进行消耗性的迭代，这在集合算法中经常被使用。 如果字典为空，调用 popitem() 将引发 KeyError。在 3.7 版更改: 现在会确保采用 LIFO 顺序。 在之前的版本中，popitem() 会返回一个任意的键/值对。
g = []
for i in range(26):
    g.append(i)
txts = '''a b c d e f g h i j 
       k l m n o p q r s t u 
       v w x y z'''
txtls = txts.split()
g = zip(g, txtls)
g = dict(g)
print(g)
print("loop ONE".center(16, '='))
h = []
while g != {}:
    g_loop = g.popitem()
    print(g_loop)
    h.append(g_loop)
print(type(g_loop))
print(h)
h = dict(h)
print(h)
print("loop TWO".center(16, '='))
i = []
for ii in range(26):
    # 如果这里g不改成h就会报错哦~
        # KeyError: 'popitem(): dictionary is empty'
    h_loop = h.popitem()
    print(h_loop)
    i.append(h_loop)
print(type(h_loop))
print(i)
i = dict(i)
print(i)


# reversed(d): 返回一个逆序获取字典键的迭代器。 这是 reversed(d.keys()) 的快捷方式。
    # TypeError: 'dict' object is not reversible❓🚧没明白
#print(reversed(d))


# setdefault(key[, default]): 如果字典存在键 key ，返回它的值。如果不存在，插入值为 default 的键 key ，并返回 default 。 default 默认为 None。
# 略🚧


# update([other]): 使用来自 other 的键/值对更新字典，覆盖原有的键。 返回 None。update() 接受另一个字典对象，或者一个包含键/值对（以长度为二的元组或其他可迭代对象表示）的可迭代对象。 如果给出了关键字参数，则会以其所指定的键/值对更新字典: d.update(red=1, blue=2)。
print(a)
print(type(('one', '壹')))
a.update(one='壹')
print(a)
a.update(two='②')
print(a)
a.update({'three': 'III'})
print(a)
a['one'] = 1
print(a)

# values(): 返回由字典值组成的一个新视图。 参见 视图对象文档。两个 dict.values() 视图之间的相等性比较将总是返回 False。
print(a.values())