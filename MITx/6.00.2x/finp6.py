import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    results = []
    results_num = 2 ** len(choices)
    # generate all results
    for i in range(results_num):
        # generate specific result specified by i
        result_str = format("{0:b}".format(i))
        result_str = '0' * (len(choices) - len(result_str)) + result_str
        result = []
        for e in result_str:
            result.append(int(e))
        results.append(result)
    # print(results)
    # compute by following the rule
    computed_results = []
    for result in results:
        computed = sum(np.array(result) * np.array(choices))
        computed_results.append(computed)
    # concatenate the matrices
    data = []
    for i in range(len(results)):
        data.append([results[i], computed_results[i], sum(results[i])])
    # sort it
    data = sorted(data, key=lambda data: data[2])
    # check if sum(result*choices) == total
    for item in data:
        if item[1] == total:
            return np.array(item[0])
    # if not so, pick the one that gives sum(result*choices) closest 
    # to total without going over
    data = sorted(data, key=lambda data: abs(data[1] - total))
    print(np.array(data))
    return np.array(data[0][0])

########################################

# choices = [1,2,2,3]
# total = 4
# # you should return either [0 1 1 0] or [1 0 0 1]
# print(find_combination(choices, total))
#
# choices = [1,1,3,5,3]
# total = 5
# # you should return [0 0 0 1 0]
# print(find_combination(choices, total))
# #
# choices = [1,1,1,9]
# total = 4
# # you should return [1 1 1 0]
# print(find_combination(choices, total))

# should return array([1, 0, 1, 0, 0, 0])
print(find_combination([1, 81, 3, 102, 450, 10], 9))