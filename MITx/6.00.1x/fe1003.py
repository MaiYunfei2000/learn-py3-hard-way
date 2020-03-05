# Write a generator, "genPrimes", that returns the sequence of prime numbers on successive calls to its "next()" method: 2, 3, 5, 7, 11, ...

def isPrime(num):
    checkBoard = []
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def genPrimes():
    num = 1
    while True:
        num += 1
        if isPrime(num):
            yield num

############################################################

"""
for i in range(2, 100):
    if isPrime(i):
        print(i)
"""

primeGenerator = genPrimes()
while True:
    print(primeGenerator.__next__())
    none = input(">>> ")