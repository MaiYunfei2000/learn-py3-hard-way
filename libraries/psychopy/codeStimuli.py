# -*- coding: utf-8 -*-

# https://www.psychopy.org/coder/codeStimuli.html

from psychopy import visual, core

# https://www.psychopy.org/api/visual/window.html#psychopy.visual.Window
# set a window of size 800 * 600
win = visual.Window([800, 600], monitor="testMonitor", height=64)
# https://www.psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim
# message = visual.TextStim(win, text='hello')
# https://www.psychopy.org/api/visual/textbox.html#psychopy.visual.TextBox
# If you use Chinese characters, you MUST use Chinese font, otherwise there will be terrible text displaying
message = visual.TextStim(win, text=u'你好', height=64, units='pix', font='SimSun')

# https://www.psychopy.org/api/visual/textstim.html#psychopy.visual.TextStim.autoDraw
message.autoDraw = True # Automatically draw every frame
win.flip()
core.wait(2)
# message.text = 'world'
message.text = u'世界'
win.flip()
core.wait(2)