# [Tutorial 2: Measuring a JND using a staircase procedure — PsychoPy v2020.2](https://www.psychopy.org/coder/tutorial2.html)

"""measure your JND in orientation using a staircase method"""
import random
import numpy as np
from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile

##### Get info from the user

# try to get a previous parameters file
try:
    expInfo = fromFile('lastParams.pickle')
# if not there then use a default set
except:
    # short for "experiment information"
    expInfo = {'observer': 'jwp', 'refOrientation':0}
# add the current time to the information
expInfo['dateStr'] = data.getDateStr()

# let's allow the user to change them in a dialogue box (called `dlg`)

# present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='simple JND Experiment', fixed=['dateStr'])
# If they hit OK then dlg.OK=True, in which case we’ll use the updated values and save them straight to a parameters file (the one we try to load above).
if dlg.OK:
    toFile('lastParams.pickle', expInfo) # save params to file for next time
else:
    core.quit() # the user hit cancel so exit

##### Setup the information for trials

# make a text file to save data
# create a filename from the subject+date+".csv"
fileName = expInfo['observer'] + expInfo['dateStr']
dataFile = open(fileName + '.csv', 'w')
dataFile.write('targetSide,oriIncrement,correct\n')

# create the staircase handler
staircase = data.StairHandler(startVal = 20.0,
                              stepType = 'db', stepSizes=[8,4,4,2],
                              nUp=1, nDown=3, # will home in on the 80% threshold
                              nTrials=1)

##### Build your stimuli

# create window and stimuli
win = visual.Window([800,600], allowGUI=True,
                    monitor='testMonitor', units='deg')
foil = visual.GratingStim(win, sf=1, size=4, mask='gauss',
                          ori=expInfo['refOrientation'])
target = visual.GratingStim(win, sf=1, size=4, mask='gauss',
                            ori=expInfo['refOrientation'])
fixation = visual.GratingStim(win, color=-1, colorSpace='rgb',
                              tex=None, mask='circle', size=0.2)
# and some handy clocks to keep track of time
globalClock = core.Clock()
trialClock = core.Clock()

# display instructions and wait
message1 = visual.TextStim(win, pos=[0,+3], text='Hit a key when ready.')
message2 = visual.TextStim(win, pos=[0,-3],
    text="Then press left or right to identify the %.1f deg probe." % expInfo['refOrientation'])
message1.draw()
message2.draw()
fixation.draw()
win.flip()
# pause until there's a keypress

##### Control the presentation of the stimuli

# will continue staircase until it terminates
for thisIncrement in staircase:
    # set location of stimuli
    targetSide = random.choice([-1,1])
    # will be either +1(right) or -1(left)
    foil.setPos([-5*targetSide, 0])
    # in other location
    target.setPos([5*targetSide, 0])
    
    # set orientation of probe
    foil.setOri(expInfo['refOrientation'] + thisIncrement)
    
    # draw all stimuli
    foil.draw()
    target.draw()
    fixation.draw()
    win.flip()
    
    # wait 500ms; use a loop of x frames for more accurate timing
    core.wait(0.5)
    
    ##### Get input from the subject

    # get response
    thisResp = None
    while thisResp == None:
        allKeys = event.waitKeys()
        for thisKey in allKeys:
            if thisKey == 'left':
                if targetSide == -1:
                    thisResp = 1 # correct
                else:
                    thisResp = -1 # incorrect
            elif thisKey == 'right':
                if targetSide == 1:
                    thisResp = 1 # correct
                else:
                    thisResp = -1 # incorrect
            elif thisKey in ['q', 'escape']:
                core.quit() # abort experiment
        event.clearEvents() # clear other (e.g. mouse) events -- they clog the buffer
    
    # add the data to the staircase so it can calculate the next level
    staircase.addData(thisResp)
    dataFile.write('%i, %.3f, %i\n' % (targetSide, thisIncrement, thisResp))
    core.wait(1)

##### Output your data and clean up

# staircase has ended
dataFile.close()
# special python binary file to save all the info
staircase.saveAsPickle(fileName)

# give some output to user in the command line in the output window
print('reversals:')
print(staircase.reversalIntensities)
approxThreshold = np.average(staircase.reversalIntensities[-6:])
print('mean of final 6 reversals = %.3f' % approxThreshold)

# give some on-screen feedback
feedback1 = visual.TextStim(
        win, pos=[0, +3],
        text = 'mean of final 6 reversals = %.3f' % approxThreshold)

feedback1.draw()
fixation.draw()
win.flip()
event.waitKeys() # wait for participant to respond

win.close()
core.quit()