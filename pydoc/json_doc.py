# [json --- JSON 编码和解码器 — Python 3.8.5 文档](https://docs.python.org/zh-cn/3/library/json.html?highlight=json#module-json)

import json

def br():
    print()

# https://docs.python.org/zh-cn/3.6/library/json.html?highlight=json#json.dumps

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

br()
print(j) # ["foo", {"bar": ["baz", null, 1.0, 2]}]
print(type(j)) # <class 'str'>
br()

print(json.dumps("\"foo\bar"))
br()

# 紧凑编码
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))
# 对比一下
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}]))
# 随便玩玩
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',  ', ':  ')))
# 这样乱来就太过分了
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',2333', ':***!')))
br()

# 美化输出
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
# 对比
print(json.dumps({'4': 5, '6': 7}))
print(json.dumps({'4': 5, '6': 7}, indent=2))
br()

# 解码外部 JSON 数据
# 实践情景中一般就是从文件或API中直接读来的字符串对象了
# https://docs.python.org/zh-cn/3.6/library/json.html?highlight=json#json.load
json_data = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(json_data)
print(type(json_data))
br()

# 特殊 JSON 对象解码
import decimal
de = json.loads('1.1', parse_float=decimal.Decimal)
print(de)
print(type(de))
br()

