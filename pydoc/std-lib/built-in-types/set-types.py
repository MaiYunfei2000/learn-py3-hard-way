##### Set Types (集合类型) — set, frozenset
# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

"""
set 对象是由具有唯一性的 hashable 对象所组成的无序多项集。
常见的用途包括成员检测、从序列中去除重复项以及数学中的集合类
计算，例如交集、并集、差集与对称差集等等。 （关于其他容器对
象请参看 dict, list 与 tuple 等内置类，以及 collections 
模块。）

与其他多项集一样，集合也支持 x in set, len(set) 和
 for x in set。 作为一种无序的多项集，集合并不记录
元素位置或插入顺序。 相应地，集合不支持索引、切片或
其他序列类的操作。

目前有两种内置集合类型，set 和 frozenset。 
set 类型是可变的 --- 其内容可以使用 add() 和 remove() 
这样的方法来改变。 由于是可变类型，它没有哈希值，且不能被用作
字典的键或其他集合的元素。 frozenset 类型是不可变并且为
 hashable --- 其内容在被创建后不能再改变；因此它可以被用作
字典的键或其他集合的元素。

除了可以使用 set 构造器，非空的 set (不是 frozenset) 还
可以通过将以逗号分隔的元素列表包含于花括号之内来创建，例如:
 {'jack', 'sjoerd'}。

两个类的构造器具有相同的作用方式：

class set([iterable])
class frozenset([iterable])
返回一个新的 set 或 frozenset 对象，其元素来自于 iterable。 
集合的元素必须为 hashable。 要表示由集合对象构成的集合，所有的
内层集合必须为 frozenset 对象。 如果未指定 iterable，则将返回
一个新的空集合。
"""

def stest(a):
    print('✨')
    print(a)
    print(type(a))
    print('✨')
    
a = set()
stest(a)
b = frozenset()
stest(b)
c = {'jack', 'sjoerd'}
stest(c)

"""
len(s)
返回集合 s 中的元素数量（即 s 的基数）。

x in s
检测 x 是否为 s 中的成员。

x not in s
检测 x 是否非 s 中的成员。

isdisjoint(other)
如果集合中没有与 other 共有的元素则返回 True。 当且仅当两个集合的交集为空集合时，两者为不相交集合。

issubset(other)
set <= other
检测是否集合中的每个元素都在 other 之中。

set < other
检测集合是否为 other 的真子集，即 set <= other and set != other。

issuperset(other)
set >= other
检测是否 other 中的每个元素都在集合之中。

set > other
检测集合是否为 other 的真超集，即 set >= other and set != other。

union(*others)
set | other | ...
返回一个新集合，其中包含来自原集合以及 others 指定的所有集合中的元素。

intersection(*others)
set & other & ...
返回一个新集合，其中包含原集合以及 others 指定的所有集合中共有的元素。

difference(*others)
set - other - ...
返回一个新集合，其中包含原集合中在 others 指定的其他集合中不存在的元素。

symmetric_difference(other)
set ^ other
返回一个新集合，其中的元素或属于原集合或属于 other 指定的其他集合，但不能同时属于两者。

copy()
返回原集合的浅拷贝。

请注意，非运算符版本的 union(), intersection(), difference()，以及 symmetric_difference(), issubset() 和 issuperset() 方法会接受任意可迭代对象作为参数。 相比之下，它们所对应的运算符版本则要求其参数为集合。 这就排除了容易出错的构造形式例如 set('abc') & 'cbs'，而推荐可读性更强的 set('abc').intersection('cbs')。

set 和 frozenset 均支持集合与集合的比较。 两个集合当且仅当每个集合中的每个元素均包含于另一个集合之内（即各为对方的子集）时则相等。 一个集合当且仅当其为另一个集合的真子集（即为后者的子集但两者不相等）时则小于另一个集合。 一个集合当且仅当其为另一个集合的真超集（即为后者的超集但两者不相等）时则大于另一个集合。

set 的实例与 frozenset 的实例之间基于它们的成员进行比较。 例如 set('abc') == frozenset('abc') 返回 True，set('abc') in set([frozenset('abc')]) 也一样。

子集与相等比较并不能推广为完全排序函数。 例如，任意两个非空且不相交的集合不相等且互不为对方的子集，因此以下 所有 比较均返回 False: a<b, a==b, or a>b。

由于集合仅定义了部分排序（子集关系），因此由集合构成的列表 list.sort() 方法的输出并无定义。

集合的元素，与字典的键类似，必须为 hashable。

混合了 set 实例与 frozenset 的二进制位运算将返回与第一个操作数相同的类型。例如: frozenset('ab') | set('bc') 将返回 frozenset 的实例。

下表列出了可用于 set 而不能用于不可变的 frozenset 实例的操作：

update(*others)
set |= other | ...
更新集合，添加来自 others 中的所有元素。

intersection_update(*others)
set &= other & ...
更新集合，只保留其中在所有 others 中也存在的元素。

difference_update(*others)
set -= other | ...
更新集合，移除其中也存在于 others 中的元素。

symmetric_difference_update(other)
set ^= other
更新集合，只保留存在于集合的一方而非共同存在的元素。

add(elem)
将元素 elem 添加到集合中。

remove(elem)
从集合中移除元素 elem。 如果 elem 不存在于集合中则会引发 KeyError。

discard(elem)
如果元素 elem 存在于集合中则将其移除。

pop()
从集合中移除并返回任意一个元素。 如果集合为空则会引发 KeyError。

clear()
从集合中移除所有元素。
"""