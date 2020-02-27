##### Midterm - Problem 7

# https://stackoverflow.com/questions/42874825/python-functions-with-multiple-parameter-brackets

# ......

##########

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    poly = sorted(list(range(0, len(L))))
    poly.reverse()
    
    def func(x):
        s = 0
        for i in range(len(L)):
            s += L[i] * x ** poly[i]
        return s
    
    return func

##########

x = 10

print(general_poly([1, 2, 3, 4])(x))
print(general_poly([0, 0, 0, 0])(x))
print(general_poly([0, 0, 0, 1])(x))
print(general_poly([0, 0, 2, 0])(x))