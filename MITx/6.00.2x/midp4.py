def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    x1, x2, x3, x4 = 0, 0, 0, 0
    total = 0
    
    # decide x1
    while True:
        if x1 * 25 < s:
            x1 += 1
        elif x1 * 25 == s:
            break
        else:
            x1 -= 1
            break
    total += x1 * 25
    
    # decide x2
    while True:
        if total + x2 * 10 < s:
            x2 += 1
        elif total + x2 * 10 == s:
            break
        else:
            x2 -= 1
            break
    total += x2 * 10
    
    # decide x3
    while True:
        if total + x3 * 5 < s:
            x3 += 1
        elif total + x3 * 5 == s:
            break
        else:
            x3 -= 1
            break
    total += x3 * 5
    
    # decide x4
    while True:
        if total + x4 < s:
            x4 += 1
        elif total + x4 == s:
            break
        else:
            x4 -= 1
            break
    
    return [x1, x2, x3, x4]

print(solve(20))