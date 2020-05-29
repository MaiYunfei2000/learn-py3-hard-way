"""
You have a bucket with 3 red balls and 3 green balls. Assume that once 
you draw a ball out of the bucket, you don't replace it. What is the 
probability of drawing 3 balls of the same color?

Write a Monte Carlo simulation to solve the above problem. Feel free 
to write a helper function if you wish.
"""

########################################

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    balls = ['red', 'green'] * 3
    inRightCond = 0
    for i in range(numTrials):
        # choose 3 balls randomly
        sample = random.sample(balls, 3)
        # print("sample", sample)
        if sample[0] == sample[1] == sample[2]:
            inRightCond += 1
    return inRightCond / numTrials

########################################

print(noReplacementSimulation(5000))