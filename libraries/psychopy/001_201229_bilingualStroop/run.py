# -*- coding: utf-8 -*-

import random
import pandas as pd
from textwrap import dedent
from datetime import datetime
from psychopy import core, clock, data, gui, visual
from psychopy.hardware import keyboard

##### 1. 初始化

# 非调试模式请注释掉
random.seed(0)

# 定义每个 blocks 的 trials 重复多少次
nTrials = 1

#### 基础信息

psychopyVer = '2020.2.10'
expName = 'BilingualStroop'
# 将用于生成收集被试信息的对话框，键为项目名，值为默认选项
expInfo = {'被试编号': '000', '性别': '女', '年龄': '00', '组别': 'A'}

# 弹出 GUI 窗口收集被试信息，并修改 expInfo 的相应值
# https://www.psychopy.org/api/gui.html#psychopy.gui.DlgFromDict
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)

dateStrOri = str(datetime.now())
dateStr = ''.join(dateStrOri[:-10].split('-'))
dateStr = '_'.join(dateStr.split(' '))
dateStr = ''.join(dateStr.split(':'))
expInfo['日期'] = dateStrOri
expInfo['实验名称'] = expName
expInfo['PsychoPy版本'] = psychopyVer

# 用户选择 cancel 则中止实验，否则继续下去
if dlg.OK == False:
    print("实验被取消。")
    core.quit()
# expInfo = None # ⚠️ 仅限于 debug 时

print('正在初始化……')
   
#### 安排刺激的所有水平

condEN = pd.DataFrame({
    'word': ['red'] * 3 + ['green'] * 3 + ['blue'] * 3,
    'letterColor': ['red', 'green', 'blue'] * 3,
    'corrAns': ['left', 'down', 'right'] * 3,
    'congruent': [1, 0, 0, 0, 1, 0, 0, 0, 1]
})
condCH = pd.DataFrame({
    'word': ['红'] * 3 + ['绿'] * 3 + ['蓝'] * 3,
    'letterColor': ['red', 'green', 'blue'] * 3,
    'corrAns': ['left', 'down', 'right'] * 3,
    'congruent': [1, 0, 0, 0, 1, 0, 0, 0, 1]
})
condEN.to_excel('condEN.xlsx')
condCH.to_excel('condCH.xlsx')

#### 初始化实验安排

fileName = expName + u'Data/%s_%s_%s' % (expName, expInfo['被试编号'], dateStr)
exp = data.ExperimentHandler(name=expName,
                             version='2020.2',
                             extraInfo=expInfo,
                             dataFileName=fileName)

print('即将启动 PsychoPy ……')
print()

# 设定窗口
    # 主要包括大小、是否全屏等
    # 其它为通常不需要变甚至不需要设定的参数
# 🚧'testMonitor'在正式实验中要改吗？
# https://www.psychopy.org/api/visual/window.html#psychopy.visual.Window
def setWin():
    """
    方便关掉 win 之后又立即打开而无需输入多行代码。
    """
    global win
    win = visual.Window(size=[800, 600],
                        fullscr=False,
                        screen=0, 
                        winType='pyglet', 
                        # allowGUI=True,
                        monitor='testMonitor', 
                        color=[0,0,0], 
                        units='pix')

setWin()

#### 准备接下来要使用的视觉对象

# 注视点
# 🚧要是能做成一个 class Cross(Line) 就好了呢 然鹅需要搞懂一层层源码qwq
def drawFixation(size=1, lineWidth=5):
    horiLine = visual.Line(win, [-5, 0], [5, 0],
                           lineWidth=lineWidth, size=size,
                           autoDraw=False)
    vertLine = visual.Line(win, (0,-5), (0,5),
                           lineWidth=lineWidth, size=size,
                           autoDraw=False)
    horiLine.draw()
    vertLine.draw()

#### 设置按键并准备记录

# https://www.psychopy.org/api/hardware/keyboard.html
# https://www.psychopy.org/_modules/psychopy/hardware/keyboard.html#Keyboard
resp = keyboard.Keyboard() # bufferSize=1
# create a default keyboard (e.g. to check for escape)
defaultKb = keyboard.Keyboard()

##### 2. 开始实验程序

group = expInfo['组别']
langList = ['CH', 'EN'] if group=='A' else ['EN', 'CH']
#### 一个个 block 地遍历
for language in langList:
    
    #### 指导语
    langNameCH = '英语' if language=='EN' else '汉语'
    instructionStr = dedent(f"""
        接下来会呈现系列单词，语言为【{langNameCH}】。
        你需要在单词出现后立即按键反应。

        红色字体按“←”
        绿色字体按“↓”
        蓝色字体按“→”

        请尽量又快又准地反应。
        按空格键开始程序。
        """)
    # instructionStr = f"""接下来会呈现系列单词，语言为【{langNameCH}】。\n你需要在单词出现后立即按键反应。\n\n红色字体按“←”\n绿色字体按“↓”\n蓝色字体按“→”\n\n请尽量又快又准地反应。\n\n按空格键开始程序。"""
    instructionText = visual.TextStim(win,
                                      text=instructionStr,
                                      font='SimSun',
                                      height=25)
    instructionText.setAutoDraw(True)
    win.flip()
    # 按空格以继续
    resp.clearEvents(eventType='keyboard')
    while True:
        key = resp.getKeys('space')
        if len(key):
            break
        if defaultKb.getKeys(["escape"]):
            core.quit()
        win.flip()
    instructionText.setAutoDraw(False)
    win.flip()
    
    ### 初始化 trialHandler
    exec(f'trialList{language} = data.importConditions("cond{language}.xlsx")')
    # 这些是 OrderedDict ；总之就是要元素是字典的列表，还挺麻烦的……
    # trialListEN = data.importConditions('condEN.xlsx')
    # trialListJP = data.importConditions('condJP.xlsx')
    # https://www.psychopy.org/api/data.html#psychopy.data.TrialHandler
    trials = data.TrialHandler(eval(f"trialList{language}"), 
                               nReps=nTrials, 
                               method='random',
                               extraInfo=expInfo,
                               seed=0)

    exp.addLoop(trials)
    
    print(trials)
    
    #### 一个个 trial 地遍历
    for thisTrial in trials:
        # 从 trialHandler 中提取出每轮试次的信息
        """
        本实验中有：word, letterColor, corrAns, congruent 这些变量
        """
        # print("thisTrial:", thisTrial)
        for varName in thisTrial:
            exec(varName + '= thisTrial[varName]')
        
        ### 初始化键盘
        resp.clearEvents(eventType='keyboard')
        
        ### 呈现 500ms 的注视点
        drawFixation(2)
        win.flip()
        core.wait(0.5)
    
        ### 呈现文字刺激直到用户按键
        # 初始化文字刺激
        font = 'SimSun' if language=='CH' else 'Times New Roman'
        textStim = visual.TextStim(win,
                                   text=word,
                                   color=letterColor,
                                   font=font,
                                   height=100)
        textStim.setAutoDraw(True)
        # 呈现文字刺激
        # textStim.draw()
        win.flip()
        # 开始计时
        timer = clock.Clock()
        # TODO: 搞明白 waitRelease 参数的作用
            # https://www.psychopy.org/api/hardware/keyboard.html
        looping = True
        
        while looping:
            keypress = resp.getKeys(['left', 'down', 'right'], waitRelease=True)
            win.flip()
            if len(keypress):
                rt = round(timer.getTime() * 1000)
                keyName = keypress[0].name
                isCorrect = (keyName == corrAns)
                textStim.setAutoDraw(False)
                looping = False        
            if defaultKb.getKeys(["escape"]):
                print("程序提前终止。")
                core.quit()
        
        ### 记录数据
        trials.addData('RT', rt)
        trials.addData('keyPress', keyName)
        trials.addData('isCorrect', isCorrect)
        
        win.flip()
        core.wait(0.5)
        
        # 输出本 trial 数据
        exp.nextEntry()
    
        print("pressed[" + keyName + '],', str(rt) + 'ms', [key.name for key in keypress]) # debug use

##### 3. 结束实验程序

print()
print('=' * 50)
print('实验进程已结束。')
print('=' * 50)

# win.close()
core.quit()