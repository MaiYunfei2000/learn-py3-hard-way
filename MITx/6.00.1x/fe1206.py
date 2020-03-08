import random

def mySort(L):
    """ L, list with unique elements """
    clear = False
    
    check, assi = 0, 0 # debug
    
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                
                assi += 3 # debug
            check += 1
    
    print(assi, check, end='') # debug
    print(L)

def newSort(L):
    """ L, list with unique elements """
    
    check, assi = 0, 0 # debug
    
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
                
                assi += 3 # debug
            
            j += 1
            
            check += 1 # debug
    
    print(assi, check, end='') # debug
    print(L)

ls = list(range(15))
print(ls)
random.shuffle(ls)
print(ls)

mySort(ls.copy())
newSort(ls.copy())

mySort([1,2,3])
newSort([1,2,3])
mySort([3,2,1])
newSort([3,2,1])