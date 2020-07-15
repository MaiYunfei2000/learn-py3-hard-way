import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# die = Die([1,2,3,4,5,6])
# print(die.roll())
# print(die.roll())
# print(die.roll())

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    # trials
    longest_runs = []
    for trial in range(numTrials):
        # rolls
        rolls = []
        for roll in range(numRolls):
            rolls.append(die.roll())
        
        # print(rolls) # DEBUGGING STATEMENT!!!!!!
        
        # count the length of this run
        runs = []
        if len(rolls) == 1:
            runs.append(1)
        for i in range(1, len(rolls)):
            if i == 1:
                if rolls[1] == rolls[0]:
                    run_count = 2
                else:
                    run_count = 1
                    runs.append(1)
            elif i > 1:
                if rolls[i] == rolls[i-1]:
                    run_count += 1
                else:
                    runs.append(run_count)
                    run_count = 1
            if i == len(rolls) - 1:
                runs.append(run_count)
        # pick the longest run
        longest_run = max(runs)
        longest_runs.append(longest_run)
    # calculate the mean value of the longest runs
    mean, std = getMeanAndStd(longest_runs)
    # make the histogram
    makeHistogram(longest_runs, 10, 'Longest run', 'Frequency')
    return round(mean, 3)
    
# One test case
# print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
# print(getAverage(Die([1]), 10, 1000))
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))