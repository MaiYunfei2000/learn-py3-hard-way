##### Midterm - Problem 5

##########

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    output = {}
    values = []
    
    for item in d.items():
        
        if item[1] not in values:
            output[item[1]] = [item[0]]
            values.append(item[1])
        else:
            output[item[1]] += [item[0]]
        
        output[item[1]] = sorted(output[item[1]])
    
    return output

##########

d = {1:10, 2:20, 3:30}
print(dict_invert(d))
d = {1:10, 2:20, 3:30, 4:30}
print(dict_invert(d))
d = {4:True, 2:True, 0:True}
print(dict_invert(d))