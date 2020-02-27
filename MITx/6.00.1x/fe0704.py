def union(set1, set2):
    """
    set1 and set2 are collections of objects, each of which might be
    empty.
    Each set has no duplicates within itself, but there may be objects
    that are in both sets. Objects are assumed to be of the same type.
    
    This function returns one set containing all elements from both
    input sets, but with no duplicates.
    """
    # 如果set1长度为0
    if len(set1) == 0:
        return set2
    # 如果set1的首个元素也在set2中
    elif set1[0] in set2:
        return union(set1[1:], set2)
    # 如果set1长度不为0，首个元素也不在set2中
    else:
        return set1[0] + union(set1[1:], set2)
    
    """
    对于glass box test，还要考虑递归后的函数：
    
    # 如果set1[1:]即set1去除首个元素之后剩下的东西为空
    # 如果set1[1:][0]即set1的第1个元素在set2中
    # 如果上面两种情况都不符
        
    对于一个suite，应当使用一个最小的组合跑遍所有可能。
    """