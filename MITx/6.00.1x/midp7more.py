# https://stackoverflow.com/questions/42874825/python-functions-with-multiple-parameter-brackets

def func(a):
    def func2(b):
        return a + b
    return func2

print(func(1))
func2 = func(1) ## You don't have to call it func2 here
print(func2(2)) 

print()
print(func(1)(2)) ## func(1) returns func2 which is then called with (2)

# ......好吧