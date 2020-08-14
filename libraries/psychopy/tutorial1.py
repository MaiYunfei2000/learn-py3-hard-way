# [Tutorial 1: Generating your first stimulus — PsychoPy v2020.2](https://www.psychopy.org/coder/tutorial1.html)

from psychopy import visual, core, event # import some libraries from PsychoPy

# create a window
myWindow = visual.Window([800, 600], monitor="testMonitor", units="deg")

# create some stimuli
# https://www.psychopy.org/api/visual/gratingstim.html#psychopy.visual.GratingStim
grating = visual.GratingStim(win=myWindow, mask="circle", size=3, pos=[-4,0], sf=3)
fixation = visual.GratingStim(win=myWindow, size=0.5, pos=[0,0], sf=0, rgb=-1)

# draw the stimuli and update the window
grating.draw()
fixation.draw()
myWindow.update()

# pause, so you get a chance to see it!
# [psychopy.core - basic functions (clocks etc.) — PsychoPy v2020.2](https://www.psychopy.org/api/core.html#psychopy.core.wait)
core.wait(5.0)

# for frameN in range(200): # run for 200 frames
# or you can:
while True:
    grating.setPhase(0.05, '+') # advance phase by 0.05 of a cycle
    grating.draw()
    fixation.draw()
    myWindow.update()
    
    # https://www.psychopy.org/api/event.html#psychopy.event.getKeys
    key = event.getKeys() # Let's see what happens
    if len(key) > 0:
        print(key) # cool
        break
    event.clearEvents()

# cleanup
myWindow.close()
core.quit()