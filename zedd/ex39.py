# 此次练习学习如何玩转**字典**(dict)

# create a mapping of state to abbreviation（创建一个从洲名称到其缩写名的映射）
# 创建字典states，包含若干从 州 到 州缩写 的映射
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
# 创建字典cities，包含从 州缩写 到 城市 的映射
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
# 将“词条”NY、OR加入字典cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print("\n# print out some cities")

print('-' * 10)
# 打印balabala以及纽约州和俄勒冈州的城市
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print("\n# print some states")

print('-' * 10)
# 打印密歇根州和佛罗里达州的城市缩写
print("Michigan's abbreviation is : ", states['Michigan'])
print("Florida's abbreviation is : ", states['Florida'])

print("\n# do it by using the state then cities dict")

print('-' * 10)
# 这其实就是一个嵌套，states['Michigan']就等于'MI'，这样一来这个cities[states['Michigan']]就等于cities['MI']也就等于'Detroit'
# 可以类比外函数和里函数！
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print("\n# print every state abbreviation")

print('-' * 10)
# list(states.items)应该就是把states里的项目(items)转换成列表形式
# 对于这个列表的所有内容，以state和abbrev两个参数依次对应列表里的两个集合
# 然后打印出来
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print("\ntest: \n", list(cities.items()), "\n")
# Super Stella!!!!!!! Cooooooooool!!!!!!

print("\n# print every city in state")

print('-' * 10)
# 同样地，以这种方式打印出字典cities
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('\n# now do both at the same time')
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    # Wow, cool! 面对多个变量可以用嵌套的方式来把玩

print('-' * 10)
print('\n# safely get a abbreviation by state that might not be there')
# 确认key'Texas'是否存在于dict'states'中
state = states.get('Texas')
# try another: state = states.get('New York')
# get是什么意思？
# 盲猜是这个：https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=get#dict.get
# dict.get(key[, default])：如果 key 存在于字典中则返回 key 的值，否则返回 default。 如果 default 未给出则默认为 None，因而此方法绝不会引发KeyError
# 因此这行代码会返回None

print("print state: ", state)
print("print not state: ", not state, "\n")

if not state:
    # if not 是什么意思？还记得ex35吗？if实际上是if后面的内容为True则执行if下面的代码
    # 如果 not state 的值为真，即state为False
    print("Sorry, no Texas.")

print('\n# get a city with a default value')
# 试试来一个带有默认值的城市吧~
city = cities.get('TX', 'Does Not Exist')
# key'TX'不存在与dict'states中，因此返回默认值'Does Not Exist'给变量city
print(f"The city for the state 'TX' is: {city}")

# 巩固练习1

## Help on class dict in module builtins:

## class dict(object)
##  |  dict() -> new empty dictionary
##  |  dict(mapping) -> new dictionary initialized from a mapping object's
##  |      (key, value) pairs
##  |  dict(iterable) -> new dictionary initialized as if via:
##  |      d = {}
##  |      for k, v in iterable:
##  |          d[k] = v
##  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
##  |      in the keyword argument list.  For example:  dict(one=1, two=2)
##  |
##  |  Methods defined here:
##  |
##  |  __contains__(self, key, /)
##  |      True if D has a key k, else False.
##  |
##  |  __delitem__(self, key, /)
##  |      Delete self[key].
##  |
##  |  __eq__(self, value, /)
##  |      Return self==value.

# 发现了木有，dict是一种class

# 额不对，找错了……

# wai，可以搞多行注释的，你个SB

# 三个单引号或三个双引号，e.g.

'''
111111
222222
333333
'''