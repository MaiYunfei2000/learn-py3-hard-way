def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

swapSort([1,5,2,3,5,6,7,8])

# If we make a small change to the line for j in range(i+1, len(L)): such that the code becomes:

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

modSwapSort([1,5,2,3,5,6,7,8])
print()
modSwapSort([1,2])
modSwapSort([2,1])
print()
swapSort([8,7,6,5,3,2,5,1])
modSwapSort([8,7,6,5,3,2,5,1])