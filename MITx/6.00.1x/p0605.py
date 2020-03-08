def search(L, e):
    for i in range(len(L)):
        
        print(L[i]) # de
        
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        
        print(L[size-i-1],L[i],size-i-1) # de
        
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

L = [1, 2, 3, 5, 7, 9, 10]

print(search(L,3))
print('-'*50)
print(newsearch(L,3))

print('second' + '='*50)

print(search(L,4))
print('-'*50)
print(newsearch(L,4))

print('third' + '='*50)

print(search(L,11))
print('-'*50)
print(newsearch(L,11))

print('fourth' + '='*50)

print(search([],11))
print('-'*50)
print(newsearch([],11))

print('third' + '='*50)

print(search([1],11))
print('-'*50)
print(newsearch([1],11))

print('third' + '='*50)

print(search([1,2],11))
print('-'*50)
print(newsearch([1,2],11))