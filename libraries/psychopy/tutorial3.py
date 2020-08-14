# 有毒 为什么一下占十几G的内存然后卡死。。。

from __future__ import print_function

"""
This analysis script takes one or more staircase datafiles as input
from a GUI. It then plots the startcases on top of each other on
the left and a combined psychometric function from the same data
on the right
"""

import numpy as np
import matplotlib.pyplot as plt
from psychopy import data, gui, core
from psychopy.tools.filetools import fromFile

# Open a dialog box to select files from 
# https://www.psychopy.org/api/gui.html#fileopendlg
files = gui.fileOpenDlg('.')
if not files:
    core.quit()

# get the data from all the files
allIntensities, allResponses = [], []
for thisFileName in files:
    # https://www.psychopy.org/api/tools/filetools.html#psychopy.tools.filetools.fromFile
    thisDat = fromFile(thisFileName)
    allIntensities.append(thisDat.intensities)
    allResponses.append(thisDat.data)

# plot each staircase
plt.subplot(121)
colors = 'brgkcmbrgkcm'
lines, names = [], []
for fileN, thisStair in enumerate(allIntensities):
    lines.extend(plt.plot(thisStair))
    names = files[fileN]
    plt.plot(thisStair, label=files[fileN])
plt.legend()

# get combined data
combinedInten, combinedResp, combinedN = \
    data.functionFromStaircase(allIntensities, allResponses, 5)
# fit curve - in this case using a Weibull function
fit = data.FitWeibull(combinedInten, combinedResp, guess=[0.2, 0.5])
smoothInt = np.arange(min(combinedInten), max(combinedInten), 0.001)
smoothResp = fit.eval(smoothInt)
thresh = fit.inverse(0.8)
print(thresh)

# plot curve
plt.subplot(122)
plt.plot(smoothInt, smoothResp, '-')
plt.plot([thresh, thresh], [0, 0.8], '--')
plt.plot([0, thresh], [0.8, 0.8], '--')
plt.title('threshold = %0.3f' % thresh)
# plot points
pylab.plot(combinedInten, combinedResp, 'o')
pylab.ylim([0, 1])

pylab.show()