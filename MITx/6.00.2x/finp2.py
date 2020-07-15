import random, numpy
import matplotlib.pyplot as plt

xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
# these values are 1 * 1000 arrays
xVals = numpy.array(xVals)
yVals = numpy.array(yVals)
wVals = numpy.array(wVals)
# add by elements
# uniform?
xVals = xVals + xVals
# uniform?
zVals = xVals + yVals
# uniform?
tVals = xVals + yVals + wVals

# let's plot them!

# plt.hist(xVals, bins=10)
# plt.show()

# plt.hist(tVals, bins=10)
# plt.show()

# 2-3
# plt.plot(xVals, zVals)
# plt.show()

# 2-4
# plt.plot(xVals, yVals)
# plt.show()

# 2-5
# plt.plot(xVals, sorted(yVals))
# plt.show()

# 2-6
# plt.plot(sorted(xVals), yVals)
# plt.show()

# 2-7
plt.plot(sorted(xVals), sorted(yVals))
plt.show()