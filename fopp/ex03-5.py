# many practice about "string"

# 3.5.1

name = "Python语言程序设计"
print(
name[0],
name[7],
name[11],
name[2:-4],
name[:6],
name[6:],
name[:], sep='\n')
'''依次为：
第1个：P
第8个：言
第12个：计
第3至倒数第4个（不包含倒数第4个）：thon语言
从头至第7个（不包含第7个）：Python
从第7个至结尾：语言程序设计
全部：Python语言程序设计
'''

# 3.5.2

# break: 不如从https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=str#text-sequence-type-str或https://docs.python.org/3/library/stdtypes.html?highlight=str#text-sequence-type-str开始，联系完所有的代码，然后再回课本康康
# 此部分的代码已转移至pydoc/built-in-types.py

x = 'he'
y = 'llo'
print(x + y) # 连接两个字符串
print(x * 3) # 复制n次字符串
print('h' in x) # 前者是否是后者的子串
print(y[2]) # 返回第i个字符
print('abcdefghiljklmn'[2:4]) # 返回前闭后开区间索引的子串

# 返回新字符串，由元素为字符串的组合数据类型（iterable）的元素拼接而成，元素之间由str分割
print('haha'.join(['a','b','c','fff','ggg']))