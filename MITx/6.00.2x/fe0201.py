class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'

def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
        # 你转换为二进制就好理解了，比如 2*6 就是
            # 从 000000 到 111111 的全部情形
    for i in range(2**N):
        #print("i", bin(i))
        combo = []
        # 比如 N = 6 ，那便 range(N) 便是 0，1，2，3，4，5
            # 也就是说，在这里，j 代表着二进制形式的数字的位数
        for j in range(N):
            #print("j", j)
            # test bit jth of integer i
                # [BitwiseOperators - Python Wiki](https://wiki.python.org/moin/BitwiseOperators)
                # [Python位运算符详解](http://c.biancheng.net/view/2184.html)
                # [一篇读懂Python中的位运算 - 听雨危楼 - 博客园](https://www.cnblogs.com/Neeo/articles/10536202.html)
            # 如果 i 右移 j 位之后除以 2 的余数为 1 —— 这代表什么意思呢？
                # 比如说最开始i=0即000001，j=0，1右移0位后还是1，表达式为True
                # 然后i=0，j=1，1右移1位变为0，此处至随后i=1的所有情况都为False
                # 然后i=1即000010，j=0，False；j=1为000001，True，随后为False
                # i=2即000011，j=0，True，j=1，True，随后False
                # 这是什么意思呢？首先得回答每个i代表着什么。
                    # i的每一位数都代表一个item的选取与否（1选取，0不选）
                    # 111111代表全选，000000代表全不选，也就是i代表着全部的情形——2^n
                # 那这个 if statement 到底是什么意思呢？
                    # 右移j位代表什么意思？为了什么？
                # 看起来就像是某种过滤装置，从2^n个情形中“淘汰”掉一批情形
                    # 为什么要“淘汰”？这些被“淘汰”的情形有什么特点？
                        # 移位之后为0，即某一位（j代表的那一位）为0
                            # j=0时即为从右往左第1位的情况
                            # j=1时即为从右往左第2位的情况
                            # ……
                # Search Tree Enumeration 的视觉上水平翻转过来的版本？
            # 喂，你是不是应该理一理combo是什么意思
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        # [6. 表达式 — Python 3.8.2 文档] (https://docs.python.org/zh-cn/3/reference/expressions.html#yieldexpr)
        # 生成当前的combo
        yield combo
    pass
    """
    这里的目的就是对于for循环中每个i都输出一个combo即集合，你看，你不先搞清楚input和output就一头扎进去，
    然后把自己搞得一脸懵逼，这不活该嘛。
        
    好了，现在进入某一个i了，假定这个bin(i)是101010（对应42，base-10），即，
        选clock，不选painting，选radio，不选vase，选book，不选computer
    
    我们要怎么生成这个物品集合呢？你看清楚，这个combo是一个list，
        所以就想办法让这些item，append或不append进去呗！
    
    好了现在开始进入j的for循环！
    
    j=0，此时考察的是101010的从右往左的第1位，此时i右移0位得到101010，
        101010除以2得到10101余0，表达式为False，于是不会发生：
            items[0]即clock被append进combo……等等，为什么是这样，
            看结果，跟我设想的不一样啊啊啊？
    
    哦原来我找错了，应该是set 43…… i等于42时实际上是第43个啊啊啊啊啊(╯‵□′)╯︵┻━┻
    
    101010 >> 0 : 0b101010 % 2 得 0
    101010 >> 1 : 0b10101 % 2 得 1
    101010 >> 2 : 0b1010 得 0
    101010 >> 3 : 0b101 得 1
    101010 >> 4 : 0b10 得 0
    101010 >> 5 : 0b1 得 1
    
    那就说得通了。这里原来是1代表不选，0代表选啊……
    
    前面理解的，这是决策树（从左到右）的镜像，确实如此。
    
    反正无论if statement那里是==0还是==1亦或!=0还是!=1，最终生成的子集都一样，
        只是生成的顺序倒了过来而已。
    
    其实如果这些东西能可视化的话理解起来会非常迅速！可以避免自己傻乎乎地捣鼓那么久。
        那么自己有必要系统地练习如何可视化各种abstraction了！
    """

"""
As above, suppose we have a generator that returns every combination of 
objects in one bag. We can represent this as a list of 1s and 0s denoting 
whether each item is in the bag or not.

Write a generator that returns every arrangement of items such that each 
is in one or none of two different bags. Each combination should be given 
as a tuple of two lists, the first being the items in bag1, and the second 
being the items in bag2.
"""

"""
Note this generator should be pretty similar to the powerSet generator 
above.

We mentioned that the number of possible combinations for N items into 
one bag is  2^𝑛 . How many possible combinations exist when there are 
two bags? Think about this for a few minutes, then click the following
hint to confirm if your guess is correct. Remember that a given item 
can only be in bag1, bag2, or neither bag -- it is not possible for an 
item to be present in both bags!
"""

"""
* With two bags, there are  3𝑛  possible combinations available.
* With one bag we determined there were  2𝑛  possible combinations 
  available by representing the bag as a list of binary bits, 0 or 1. 
  Since there are N bits, and they can be one of two possibilities, 
  there must be  2𝑛  possibilities.
* With two bags there thus must be  3𝑛  possible combinations. You 
  can imagine this by representing the two bags as a list of 
  "trinary" bits, 0, 1, or 2 (a 0 if an item is in neither bag; 1 if it 
  is in bag1; 2 if it is in bag2). With the "trinary" bits, there are N 
  bits that can each be one of three possibilities - thus there must be
    3𝑛  possible combinations.
"""

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    # e.g. range(3**3), namely, 0 to 26
    for i in range(3**N):
        bag1 = []
        bag2 = []
        # test "bit" jth of integer i
        # e.g. range(3), namely, 0 to 2
        for j in range(N):
            # if certain "bit" is 2, append the item to bag2
            # elif is 1, append to bag1
            # else (i.e. 0), don't append (omitted)
            bit = i // (3 ** j) % 3
            if bit == 2:
                bag2.append(items[j])
            elif bit == 1:
                bag1.append(items[j])
        yield (bag1, bag2)

############################################################

items = buildItems()
"""
print('------')
for i in items:
    print(i)
print('------')
"""


setNum = 0
"""
for i in powerSet(items):
    setNum += 1
    print("set", setNum)
    for j in i:
        print(j)
"""

items = [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                   ('painting', 90, 9),
                                   ('radio', 20, 4))]

for i in yieldAllCombos(items):
    setNum += 1
    print("<< Set", setNum, ">>")
    bag = 1
    for j in i:
        print("\t[[ Bag", bag, "]]")
        for k in j:
            print("\t\t", k)
        bag += 1