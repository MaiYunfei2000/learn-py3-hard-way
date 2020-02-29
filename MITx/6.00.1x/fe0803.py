# denom不变；对列表里的值依次作simple_divide()，然后返回新列表
def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]

############################################################

def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

############################################################

# 此处denom为0
fancy_divide([0, 2, 4], 0)