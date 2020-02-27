##### Midterm - Problem 4

##########

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    product = 0
    for i in range(len(listA)):
        product += listA[i] * listB[i]
    
    return product

##########

listA = [1, 2, 3]
listB = [4, 5, 6]
print(dotProduct(listA, listB))