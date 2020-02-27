##### Midterm - Problem 6

#########

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    maxNum, minNum = max(a, b), min(a, b)
    remainder = maxNum % minNum
    if remainder == 0:
        return minNum
    else:
        return gcd(minNum, remainder)

#########

a = 1071
b = 462

print(gcd(a, b), "should be", 21)
print(gcd(2, 12), "should be", 2)
print(gcd(6, 12), "should be", 6)
print(gcd(9, 12), "should be", 3)
print(gcd(17, 12), "should be", 1)
#print(gcd(100, 0))