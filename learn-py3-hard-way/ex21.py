# 定义函数add()，函数的功能为返回参数a+b的值（需要一个变量名）。
def add(a, b):
    print(f"ADDING {a} + {b}")
    # 返回a+b的值。
    return a + b # 如果注释掉此行，打印的变量为“None”。

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return int(a / b)


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# 将age+height-(iq/2)*weight的值赋给变量what。
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")