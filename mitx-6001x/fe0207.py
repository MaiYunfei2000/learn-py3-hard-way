#2
print('\n', "#2", '\n')

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
    
    break
    
print("Number of apples: " + str(numberOfApples))

#3
print('\n', "#3", '\n')

num = 10
while num > 3:
    num -= 1
    print(num)
    
#4
print('\n', "#4", '\n')

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')