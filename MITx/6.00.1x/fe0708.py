def f(n):
    """
    n: integer, n >= 0.
    """
    if n == 0:
        return 1
    else:
        return n * f(n-1)

print(f(3), f(1), f(0))