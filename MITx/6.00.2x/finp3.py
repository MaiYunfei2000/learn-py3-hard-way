import random
        
class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
   
########################################
 
def is_all_in_a_trial(aLecture):
    '''
    aLecture: Lecture object
    
    Simulate 1 time.
    Returns: if all 3 activities take place.
    '''
    # initilize of the variable
    is_all = False
    # stochastically determine if any of these activities takes place
    listen_prob = aLecture.get_listen_prob()
    if random.random() <= listen_prob:
        is_listen = True
    else:
        is_listen = False
    sleep_prob = aLecture.get_sleep_prob()
    if random.random() <= sleep_prob:
        is_sleep = True
    else:
        is_sleep = False
    fb_prob = aLecture.get_fb_prob()
    if random.random() <= fb_prob:
        is_fb = True
    else:
        is_fb = False
    # if all activities take place, set the indicator to be True
    if is_listen and is_sleep and is_fb:
        is_all = True
    return is_all

def a_simulation(aLecture):
    '''
    Returns: number of lectures it takes 
             to have a lecture in which all 3 activities take place
    '''
    # initilize the variables
    num_lectures = 0
    # runs until is_all == True
    is_all = False
    while not is_all:
        is_all = is_all_in_a_trial(aLecture)
        num_lectures += 1
    return num_lectures

def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes 
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence 
             interval around that mean.
    '''
    # initilize the lecture numbers list
    lecture_nums = []
    # runs a Monte Carlo simulation N times and get parameters
    for i in range(N):
        lecture_num = a_simulation(aLecture)
        
        # print(lecture_num) # DEBUG STATEMENT!!!!!!!
        
        lecture_nums.append(lecture_num)
    mean, std = get_mean_and_std(lecture_nums)
    
    # print(std) # DEBUG STATEMENT!!!!!!!
    
    # z score of 0.95 CI
    z = 1.96
    # compute the width of the CI
    width = 2 * std * z
    return (mean, width)

########################################

# sample test cases 
a = Lecture(1, 1, 1)
print(lecture_activities(100, a))
# the above test should print out (1.0, 0.0)
          
b = Lecture(1, 1, 0.5)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)

# 所以为什么离散程度可以这么大？？？