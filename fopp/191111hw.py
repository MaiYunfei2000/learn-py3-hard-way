# 191111作业

# text is not allowed
def filter_text(v):
    
    try: return float(v)
    except ValueError:
        print("请输入一个数！")
        exit(0)

# T1 编写函数，接收一个正偶数为参数，输出两个素数，并且这两个素数之和等于原来的正偶数。如果存在多组符合条件的素数，则全部输出。例如10=3+7，8=3+5。

# is_prime_number
def isprime(x):
    m = 0
    
    for i in range(1, x+1):
        
        if x % i == 0:
            m += 1
    
    if m == 2:
        return True
    else:
        return False

# is_positive_even_number
def ispoe(x):
    
    if (x > 0) and (x % 2 == 0):
        return x
    else:
        print("请输入正偶数！")
        exit(0)

num = ispoe(filter_text((input("请输入一个正偶数："))))

for num in range(1, num+1):
    for i in range(1, num):
        
        j = num - i
        
        if isprime(i) == True and isprime(j) == True and i <= j:
            print("{} = {} + {}".format(num, i, j))

# T2 编写函数，计算形式如a + aa + aaa + aaaa + ... + aaa...aaa的表达式的值，其中a为小于10的自然数。a接收字符类型。

# is_natural_number_less_than_ten
def isnlt(x):
    
    if (x >= 0) and (x < 10) and (x % 1 == 0):
        return x
    else:
        print("请输入小于10的自然数！")
        exit(0)

num = isnlt(filter_text((input("请输入一个小于10的自然数："))))
strnum = str(num)
sn = 0

for num in range(1, num+1):
    
    an = strnum * int(num)
    sn += int(an)

print(sn)

# T3 用lambda函数实现练习2青蛙跳。
# （一只青蛙一次可以跳1级台阶，也可以跳2级台阶。求该青蛙跳一个n级台阶总共有多少种跳法）

# is_non_zero_natural_umber
def isnz(x):
    
    if (x > 0) and (x % 1 == 0):
        return x
    else:
        print("请输入一个非0自然数！")
        exit(0)

num = isnz(filter_text((input("请输入一个非0自然数："))))

# Fibonacci sequence
fib = lambda n: n if n <= 2 else fib(n-1) + fib(n-2)

print("总共有{}种跳法。".format(fib(num)))