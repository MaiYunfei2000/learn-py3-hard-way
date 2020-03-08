def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)



print(search([1,2,3],3))
print(search3([1,2,3],3))
print(search([1,2,4],3))
print(search3([1,2,4],3))
print(search([],3))
print(search([],3))

print()

#search3([], 4)
search([1, 2, 3], 4)
search3([1, 2, 3], 4)