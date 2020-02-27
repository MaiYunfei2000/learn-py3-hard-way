##### Midterm - Problem 3

##########

import math

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = math.log(num, base)
    
    low = int(exponent)
    high = low + 1
    
    if abs(base ** low - num) > abs(base ** high - num):
        return high
    else:
        return low

##########

print("closest_power(2, 192) should equals 7: ", closest_power(2, 192))
print("closest_power(4, 12) should equals 2: ", closest_power(4, 12))
print("closest_power(5, 22) should equals 2: ", closest_power(5, 22))
print("closest_power(100, 1) should equals 0: ", closest_power(100, 1))
print("closest_power(10, 550) should equals 2: ", closest_power(10, 550))