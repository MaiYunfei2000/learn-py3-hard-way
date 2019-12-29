# 对应课件而非课本第七章
# see more: https://docs.python.org/zh-cn/3/library/json.html?highlight=json

import json

example = {"hahaha": "nothing"}

print(example)
print(type(example))

ohhh = json.dumps(example)
print(ohhh)
print(type(ohhh))

back = json.loads(ohhh)
print(back)
print(type(back))

ohhh = json.dumps(example, sort_keys=True, indent=4)
print(ohhh)
print(type(ohhh))

ex7 = open('ex07.json', 'w+')
json.dump(example, ex7, sort_keys=False, indent=4)

# make it more complicated

last = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], sort_keys=True, indent=4)
print(last)
print(type(last))

print('====================')

# convert csv to json

sourcefile = open("price.csv", "r", -1, 'utf-8')
fr = sourcefile.readlines()
ls = []

for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(','))
sourcefile.close()

fw = open("price.json", "w")
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0],ls[i]))
json.dump(ls[1:], fw, sort_keys=True,
          indent=4, ensure_ascii=False)
fw.close()

# convert json to csv⚠️未debug

ex7p = open("ex07plus.json", 'w+')
ex7p.write("['foo', {'bar': ('baz', None, 1.0, 2)}]")
ls = json.load(ex7p)

print(ls)
print(type(ls))
print()

data = [list(ls[0].keys())]
print(data)
print()

for item in ls:
    data.append(list(item.values()))

fr.close()

fw = open("ex07_from_json.csv", 'w')
for item in data:
    fw.write(",".join(item) + "\n")
fw.close()