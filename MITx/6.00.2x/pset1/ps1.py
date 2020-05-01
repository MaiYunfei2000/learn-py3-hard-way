def dprint(statement):
    """
    for debugging
    can only print global variables
    """
    print("dprint " + statement + ":", eval(statement))

###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    
    # 把字典转为含有键值对形成的二元组的清单
    cows_ls = list(cows.items())
    # 将清单按照二元组的第1项降序排序
    cows_ls = sorted(cows_ls, key=lambda size: size[1], reverse=True)
    # 将排序好的列表转换为字典
    cows_sorted = dict(cows_ls)
    
    # 使用贪心算法：持续循环直到cows_sorted清空。
    while cows_sorted != {}:
        # 持续循环的时候，要干什么呢？
            # 那就是找出当前存在的最大的牛牛，看是否可以塞进去。
            # 塞不进去就就找更小的一头牛牛。
            # 直到飞船塞不下任何牛牛，飞船起飞，进行一趟运送。
            # 然后回来，重复上述过程。
        
        # 先把牛牛们按重量排好序如何呢？
            # 该如何开始着手呢？
            # 应该在循环外完成。
        
        ship = []
        load = 0
        # 将牛牛塞进飞船
        for cow in cows_sorted.copy():
            # 只要这头牛牛可以塞进飞船就把它塞进去
            if load + cows_sorted[cow] <= limit:
                # 牛牛上船
                ship.append(cow)
                # 飞船增加负荷
                load += cows_sorted[cow]
                # 牛圈中少了这头牛牛
                del cows_sorted[cow]
        # 飞船进行一趟行程
        trips.append(ship)
        
    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_list = list(cows.keys())
    # 枚举所有可能情况
    schemes = [item for item in get_partitions(cows_list)]
    schemes = sorted(schemes, key=lambda item: len(item))
    # print("trips[0]", schemes[0])
    # print("trips[1]", schemes[1])
    
    # 判断这样的装载方案是否可以运作
    def is_loadable(trip):
        total_weight = 0
        for cow in trip:
            # print("DEBUG:", cow)
            total_weight += cows[cow]
        if total_weight <= limit:
            return True
        else:
            return False
    # 判断这样的行程方案是否可以运作
    def is_work(trips):
        check_ls = []
        # 必须要每一个trip都OK才行
        for trip in trips:
            if is_loadable(trip):
                check_ls.append(True)
            else:
                check_ls.append(False)
        if all(check_ls) == True:
            return True
        else:
            return False
    
    # 一次次地尝试行程方案
    for trips in schemes:
        # print(trips) # debug
        if is_work(trips):
            return trips

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
# print(cows)

start = time.time()
print(greedy_cow_transport(cows, limit))
end = time.time()
greedy_time = end - start

start = time.time()
print(brute_force_cow_transport(cows, limit))
end = time.time()
brute_time = end - start

print("greedy faster?", greedy_time < brute_time)

# brute_force_cow_transport({'Milkshake': 40, 'Miss Bella': 25, 'Boo': 20, 'MooMoo': 50, 'Lotus': 40, 'Horns': 25}, 100)