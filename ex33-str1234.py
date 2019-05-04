def loop(num, d):
    i = 0
    numbers = []
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i = i + d
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num2 in numbers:
        print(num2)

num = int(input("input a number for \"num\": "))
d = int(input("input a number for \"d\": "))
loop(num, d)

# ref: [python数据类型转换（str跟int的转换） - Hello World! - CSDN博客](https://blog.csdn.net/shanliangliuxing/article/details/7920400)