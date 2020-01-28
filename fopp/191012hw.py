# 1.改造练习1的程序，实现循环判断用户输入的字符是数字字符，字母字符还是其他字符，当输入exit, 退出程序。

from sys import exit

while True:
    string = input('请输入字符：')
    
    if string.isdigit() == True:
        print('数字字符')
    elif string.isalpha() == True and string != 'exit':
        print('字母字符')
    elif string == 'exit':
        exit(0)
    else:
        print('其它字符')

# 可以改进：把exit的判断放在if那里，然后elif那里就不用and balabala...
  
# 2.P121 4.1题 猜数游戏

import random

time = 0
num = random.randrange(1,10)

def loop():
    
        if inp == num:
            print(f'猜测{time}次，你猜中了！')
            exit(0)
        if inp < num:
            print(f'遗憾，太小了。')
        if inp > num:
            print(f'遗憾，太小了。')

print('这是一个猜数游戏，请猜一个整数。\n')

while True:

    try:
        inp = int(input('请输入猜测的数：'))
        time += 1
        loop()
        
    except ValueError:
        print('嘿，输入一个整数！')         

# 3.勾股定理中3个数的关系是a2+b2=c2，编写一个程序，统计30以内满足上述条件的整数组合个数，如3、4、5就是一个组合。

i = 0

for a in range(1,31):
    
    for b in range(a+1,31):
        
        for c in range(b+1,31):
            
            if a*a+b*b == c*c:
                i += 1
                print(f'第{i}个组合：{a}²+{b}²={c}²')
            

print(f'共{i}个组合。')