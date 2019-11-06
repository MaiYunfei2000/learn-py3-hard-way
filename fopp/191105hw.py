# T1

def f(n):
    s = 0
    
    if n >= 0:
        
        if n % 2 == 1:
            for i in range(1,n+1,2):
                s += 1/i
        elif n % 2 != 1:
            for i in range(2,n+1,2):
                s += 1/i
        return s
        
    else:
        print("请输入自然数！")
        exit(0)

try:
    n = int(input("请输入一个自然数："))
        
except ValueError:
    print("请输入自然数！")
    
#output = f(n)
print(round(f(n), 2))

# T2

def func(ls):
    s = 0.0
    ss = 0.0
    ls_mean = []
    for i in ls:
        s = s + i
    mean_value = s / len(ls)
    for i in ls:
        ss = int(i - mean_value)
        ls_mean.append(ss)
    return ls_mean

ls = eval(input("请输入一个列表："))
print(func(ls))