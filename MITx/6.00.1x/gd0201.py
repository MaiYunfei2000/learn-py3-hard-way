import math

def polysum(n, s):
    """
    A regular polygon has n number of sides. Each side has length s.
    """
    area = 0.25 * n * s ** 2 / math.tan(math.pi / n)
    perimeter = n * s
    square_perimeter = perimeter ** 2
    outcome = area + square_perimeter
    
    return round(outcome, 4)
    
##########

