# hw 191012


'''

s = 0 
for i in range(100):
   # 如果i可被10整除
   if i % 10:
       # 执行后面的代码（否则从头开始）
       continue
   s = s + i
   print('i: ', i)
   print('s: ', s)
   
print(s)

'''

'''

while True:
    string = input('请输入字符：')
    
    if string.isdigit() == True:
        print('数字字符')
    elif string.isalpha() == True:
        print('字母字符')
    else:
        print('其它字符')

'''

'''
s = 1

for i in range(2, 201):
    
    if s % 17 == 0 and s % 5 != 0:
        continue
    s = i
    
print(s)

'''

'''
while True:
    
    s = input('input a 3-digit number: ')

    if len(s) == 3 and s.isdigit() == True:
        print('百位数：', s[0],
            '\n十位数：', s[1],
            '\n个位数：', s[-1])
        
    else:
        print('input a number that is 3-digit, please!')
'''

'''
公鸡a，母鸡b，小鸡c
'''

# 公鸡a，母鸡b，小鸡c只。

'''

max = 100
solution = 0

for a in range(1, max + 1):
        
    for b in range(1, max - a + 1):
            
            c = max - a - b
            if (max - a - b)%3 == 0 and (5*a + 3*b + c/3) == 100:
                solution = solution + 1
                print(f'第{solution}种解法：{a}只公鸡，{b}只母鸡，{c}只小鸡。')

print(f'共有{solution}种解法。')

'''