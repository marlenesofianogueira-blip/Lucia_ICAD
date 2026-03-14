#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on janeiro 06, 2025, at 19:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from checkKeys
nPumps=0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.2'
expName = 'bart2'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\nativ\\Documentos\\UMinho\\Tarefa BART\\BART\\bart_merged_3.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# --- Initialize components for Routine "welcome" ---
_fundo_branco_ = visual.ImageStim(
    win=win,
    name='_fundo_branco_', 
    image='branco.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
welcome_ = visual.TextStim(win=win, name='welcome_',
    text='Bem vindo/a!\n\n\n\n\n\n\n\nDesde já, obrigada pela sua participação!\n',
    font='Comic Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resposta_ = keyboard.Keyboard()
smile = visual.ImageStim(
    win=win,
    name='smile', units='norm', 
    image='smile_inicial.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text="\n\nPara avançar pressione a tecla 'ENTER'",
    font='Open Sans',
    pos=(0, -0.55), height=0.029, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "bart_manual" ---
fundo_branco = visual.ImageStim(
    win=win,
    name='fundo_branco', 
    image='branco.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from code_6
bart_manual_count = 0
bart_manual_resp = {}
bankedEarnings=0


# --- Initialize components for Routine "instructions" ---
fundobranco = visual.ImageStim(
    win=win,
    name='fundobranco', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
balão = visual.ImageStim(
    win=win,
    name='balão', units='height', 
    image='redBalloon.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, 0.3), size=(0.18, 0.18),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
euro = visual.ImageStim(
    win=win,
    name='euro', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.6, 0.3), size=(0.18, 0.18),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
balão_rebentado = visual.ImageStim(
    win=win,
    name='balão_rebentado', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, -0.1), size=(0.27, 0.27),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
perder_dinheiro = visual.ImageStim(
    win=win,
    name='perder_dinheiro', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.1), size=(0.30, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
instruções1 = visual.TextStim(win=win, name='instruções1',
    text='Neste jogo tem de ganhar o máximo possível numa competição de encher balões.\n\nCada vez que enche o balão, acumula euros. \n\nQuando quiser, pode parar de encher o balão e guardar esse valor. \n\nNo entanto, se encher demasiadas vezes o balão e ele rebentar, perde o o valor acumulado nesse mesmo balão. ',
    font='Comic Sans',
    units='norm', pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
seta_avançar = visual.ImageStim(
    win=win,
    name='seta_avançar', 
    image='Seta1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.8), size=(0.25, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
text_avançar_2 = visual.TextStim(win=win, name='text_avançar_2',
    text='Avançar',
    font='Open Sans',
    pos=(0.5, -0.8), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
mouse_1 = event.Mouse(win=win)
x, y = [None, None]
mouse_1.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_3" ---
fundobranco1 = visual.ImageStim(
    win=win,
    name='fundobranco1', 
    image='branco.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
enter_tecla = visual.ImageStim(
    win=win,
    name='enter_tecla', units='height', 
    image='enter_tecla.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(-0.63, -0.15), size=(0.33, 0.09),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
instruções2 = visual.TextStim(win=win, name='instruções2',
    text="Os balões podem rebentar a qualquer momento, desde o início.\n\nMas, quanto mais encher, maior a probabilidade de ele rebentar.\n\nIsto significa que os balões podem ocasionalmente alcançar um tamanho em que quase preenchem o ecrã, mas a maioria vai rebentar muito antes disso. \nDeve pressionar:\n\n 'ESPAÇO' para encher o balão\n\n'ENTER' para guardar o valor do balão que está a encher e avançar para o próximo balão\n\nTem alguma dúvida?",
    font='Comic Sans',
    units='norm', pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
encher_balão = visual.ImageStim(
    win=win,
    name='encher_balão', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.43, 0.02), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
guardar_dinheiro = visual.ImageStim(
    win=win,
    name='guardar_dinheiro', units='height', 
    image='guardar_dinheiro.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0.55, -0.15), size=(0.17, 0.16),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
seta_avançar_2 = visual.ImageStim(
    win=win,
    name='seta_avançar_2', 
    image='Seta1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.8), size=(0.25, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
text_avançar = visual.TextStim(win=win, name='text_avançar',
    text='Avançar',
    font='Open Sans',
    pos=(0.5, -0.8), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# --- Initialize components for Routine "trial_2" ---
fundobranco2 = visual.ImageStim(
    win=win,
    name='fundobranco2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
bankButton = keyboard.Keyboard()
# Run 'Begin Experiment' code from updateEarnings
lastBalloonEarnings=0.0
thisBalloonEarnings=0.0
nReps=0
balloonBody = visual.ImageStim(
    win=win,
    name='balloonBody', units='height', 
    image='sin', mask=None, anchor='center',
    ori=270.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
molduraRM1 = visual.ImageStim(
    win=win,
    name='molduraRM1', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
molduraRM2 = visual.ImageStim(
    win=win,
    name='molduraRM2', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, -0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
molduraBVM = visual.ImageStim(
    win=win,
    name='molduraBVM', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
molduraBM = visual.ImageStim(
    win=win,
    name='molduraBM', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.65, 0.4), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
reminderMsg1 = visual.TextStim(win=win, name='reminderMsg1',
    text='ESPAÇO para encher o balão',
    font='Comic Sans',
    units='height', pos=(-0.4,-0.4), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
reminderMsg2 = visual.TextStim(win=win, name='reminderMsg2',
    text='ENTER para guardar o valor deste balão',
    font='Comic Sans',
    units='height', pos=(0.4, -0.4), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
balloonValMsg = visual.TextStim(win=win, name='balloonValMsg',
    text='',
    font='Comic Sans',
    units='height', pos=(0, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
bankedMsg = visual.TextStim(win=win, name='bankedMsg',
    text='',
    font='Comic Sans',
    units='height', pos=(0.5, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
# Run 'Begin Experiment' code from setBalloonSize
balloonSize=0.08
balloonMsgHeight=0.01

# --- Initialize components for Routine "feedback_2" ---
fundobranco3 = visual.ImageStim(
    win=win,
    name='fundobranco3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from checkPopped
feedbackText=""
from psychopy import sound
bang = sound.Sound("balloon_explosion.wav")
coins = sound.Sound("coins.wav")
feedbackMsg22 = visual.TextStim(win=win, name='feedbackMsg22',
    text='',
    font='Comic Sans',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "final_score" ---
fundobranco4 = visual.ImageStim(
    win=win,
    name='fundobranco4', 
    image='branco.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
finalScore = visual.TextStim(win=win, name='finalScore',
    text='',
    font='Comic Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "farwell" ---
_fundo_branco_final = visual.ImageStim(
    win=win,
    name='_fundo_branco_final', 
    image='branco.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
farwell_ = visual.TextStim(win=win, name='farwell_',
    text='A tarefa terminou. \n\n\nA tua participação foi fundamental para a realização deste estudo!\n\nObrigada!\n\n\n\n\n\n\n\nObrigada mais uma vez! ',
    font='Comic Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
smile_final = visual.ImageStim(
    win=win,
    name='smile_final', 
    image='smile_final.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
resposta_.keys = []
resposta_.rt = []
_resposta__allKeys = []
# keep track of which components have finished
welcomeComponents = [_fundo_branco_, welcome_, resposta_, smile, text_3]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *_fundo_branco_* updates
    if _fundo_branco_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        _fundo_branco_.frameNStart = frameN  # exact frame index
        _fundo_branco_.tStart = t  # local t and not account for scr refresh
        _fundo_branco_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(_fundo_branco_, 'tStartRefresh')  # time at next scr refresh
        _fundo_branco_.setAutoDraw(True)
    
    # *welcome_* updates
    if welcome_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_.frameNStart = frameN  # exact frame index
        welcome_.tStart = t  # local t and not account for scr refresh
        welcome_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_, 'tStartRefresh')  # time at next scr refresh
        welcome_.setAutoDraw(True)
    
    # *resposta_* updates
    waitOnFlip = False
    if resposta_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resposta_.frameNStart = frameN  # exact frame index
        resposta_.tStart = t  # local t and not account for scr refresh
        resposta_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resposta_, 'tStartRefresh')  # time at next scr refresh
        resposta_.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resposta_.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resposta_.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resposta_.status == STARTED and not waitOnFlip:
        theseKeys = resposta_.getKeys(keyList=['return'], waitRelease=False)
        _resposta__allKeys.extend(theseKeys)
        if len(_resposta__allKeys):
            resposta_.keys = _resposta__allKeys[-1].name  # just the last key pressed
            resposta_.rt = _resposta__allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *smile* updates
    if smile.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        smile.frameNStart = frameN  # exact frame index
        smile.tStart = t  # local t and not account for scr refresh
        smile.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(smile, 'tStartRefresh')  # time at next scr refresh
        smile.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resposta_.keys in ['', [], None]:  # No response was made
    resposta_.keys = None
thisExp.addData('resposta_.keys',resposta_.keys)
if resposta_.keys != None:  # we had a response
    thisExp.addData('resposta_.rt', resposta_.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "bart_manual" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
bart_manualComponents = [fundo_branco]
for thisComponent in bart_manualComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "bart_manual" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fundo_branco* updates
    if fundo_branco.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fundo_branco.frameNStart = frameN  # exact frame index
        fundo_branco.tStart = t  # local t and not account for scr refresh
        fundo_branco.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fundo_branco, 'tStartRefresh')  # time at next scr refresh
        fundo_branco.setAutoDraw(True)
    if fundo_branco.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fundo_branco.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            fundo_branco.tStop = t  # not accounting for scr refresh
            fundo_branco.frameNStop = frameN  # exact frame index
            fundo_branco.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in bart_manualComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "bart_manual" ---
for thisComponent in bart_manualComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
fundobranco.setImage('branco.jpeg')
euro.setImage('euro.png')
balão_rebentado.setImage('balao_rebentado.jpeg')
perder_dinheiro.setImage('perder_dinheiro.jpeg')
# setup some python lists for storing info about the mouse_1
mouse_1.x = []
mouse_1.y = []
mouse_1.leftButton = []
mouse_1.midButton = []
mouse_1.rightButton = []
mouse_1.time = []
mouse_1.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [fundobranco, balão, euro, balão_rebentado, perder_dinheiro, instruções1, seta_avançar, text_avançar_2, mouse_1]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fundobranco* updates
    if fundobranco.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fundobranco.frameNStart = frameN  # exact frame index
        fundobranco.tStart = t  # local t and not account for scr refresh
        fundobranco.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fundobranco, 'tStartRefresh')  # time at next scr refresh
        fundobranco.setAutoDraw(True)
    
    # *balão* updates
    if balão.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        balão.frameNStart = frameN  # exact frame index
        balão.tStart = t  # local t and not account for scr refresh
        balão.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(balão, 'tStartRefresh')  # time at next scr refresh
        balão.setAutoDraw(True)
    
    # *euro* updates
    if euro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        euro.frameNStart = frameN  # exact frame index
        euro.tStart = t  # local t and not account for scr refresh
        euro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(euro, 'tStartRefresh')  # time at next scr refresh
        euro.setAutoDraw(True)
    
    # *balão_rebentado* updates
    if balão_rebentado.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        balão_rebentado.frameNStart = frameN  # exact frame index
        balão_rebentado.tStart = t  # local t and not account for scr refresh
        balão_rebentado.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(balão_rebentado, 'tStartRefresh')  # time at next scr refresh
        balão_rebentado.setAutoDraw(True)
    
    # *perder_dinheiro* updates
    if perder_dinheiro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        perder_dinheiro.frameNStart = frameN  # exact frame index
        perder_dinheiro.tStart = t  # local t and not account for scr refresh
        perder_dinheiro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(perder_dinheiro, 'tStartRefresh')  # time at next scr refresh
        perder_dinheiro.setAutoDraw(True)
    
    # *instruções1* updates
    if instruções1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruções1.frameNStart = frameN  # exact frame index
        instruções1.tStart = t  # local t and not account for scr refresh
        instruções1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruções1, 'tStartRefresh')  # time at next scr refresh
        instruções1.setAutoDraw(True)
    
    # *seta_avançar* updates
    if seta_avançar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seta_avançar.frameNStart = frameN  # exact frame index
        seta_avançar.tStart = t  # local t and not account for scr refresh
        seta_avançar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seta_avançar, 'tStartRefresh')  # time at next scr refresh
        seta_avançar.setAutoDraw(True)
    
    # *text_avançar_2* updates
    if text_avançar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_avançar_2.frameNStart = frameN  # exact frame index
        text_avançar_2.tStart = t  # local t and not account for scr refresh
        text_avançar_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_avançar_2, 'tStartRefresh')  # time at next scr refresh
        text_avançar_2.setAutoDraw(True)
    # *mouse_1* updates
    if mouse_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_1.frameNStart = frameN  # exact frame index
        mouse_1.tStart = t  # local t and not account for scr refresh
        mouse_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_1, 'tStartRefresh')  # time at next scr refresh
        mouse_1.status = STARTED
        mouse_1.mouseClock.reset()
        prevButtonState = mouse_1.getPressed()  # if button is down already this ISN'T a new click
    if mouse_1.status == STARTED:  # only update if started and not finished!
        buttons = mouse_1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(seta_avançar)
                    clickableList = seta_avançar
                except:
                    clickableList = [seta_avançar]
                for obj in clickableList:
                    if obj.contains(mouse_1):
                        gotValidClick = True
                        mouse_1.clicked_name.append(obj.name)
                x, y = mouse_1.getPos()
                mouse_1.x.append(x)
                mouse_1.y.append(y)
                buttons = mouse_1.getPressed()
                mouse_1.leftButton.append(buttons[0])
                mouse_1.midButton.append(buttons[1])
                mouse_1.rightButton.append(buttons[2])
                mouse_1.time.append(mouse_1.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_1.x', mouse_1.x)
thisExp.addData('mouse_1.y', mouse_1.y)
thisExp.addData('mouse_1.leftButton', mouse_1.leftButton)
thisExp.addData('mouse_1.midButton', mouse_1.midButton)
thisExp.addData('mouse_1.rightButton', mouse_1.rightButton)
thisExp.addData('mouse_1.time', mouse_1.time)
thisExp.addData('mouse_1.clicked_name', mouse_1.clicked_name)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
encher_balão.setImage('encher_balao.jpeg')
# setup some python lists for storing info about the mouse_2
mouse_2.x = []
mouse_2.y = []
mouse_2.leftButton = []
mouse_2.midButton = []
mouse_2.rightButton = []
mouse_2.time = []
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_3Components = [fundobranco1, enter_tecla, instruções2, encher_balão, guardar_dinheiro, seta_avançar_2, text_avançar, mouse_2]
for thisComponent in instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fundobranco1* updates
    if fundobranco1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fundobranco1.frameNStart = frameN  # exact frame index
        fundobranco1.tStart = t  # local t and not account for scr refresh
        fundobranco1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fundobranco1, 'tStartRefresh')  # time at next scr refresh
        fundobranco1.setAutoDraw(True)
    
    # *enter_tecla* updates
    if enter_tecla.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter_tecla.frameNStart = frameN  # exact frame index
        enter_tecla.tStart = t  # local t and not account for scr refresh
        enter_tecla.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter_tecla, 'tStartRefresh')  # time at next scr refresh
        enter_tecla.setAutoDraw(True)
    
    # *instruções2* updates
    if instruções2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruções2.frameNStart = frameN  # exact frame index
        instruções2.tStart = t  # local t and not account for scr refresh
        instruções2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruções2, 'tStartRefresh')  # time at next scr refresh
        instruções2.setAutoDraw(True)
    
    # *encher_balão* updates
    if encher_balão.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        encher_balão.frameNStart = frameN  # exact frame index
        encher_balão.tStart = t  # local t and not account for scr refresh
        encher_balão.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(encher_balão, 'tStartRefresh')  # time at next scr refresh
        encher_balão.setAutoDraw(True)
    
    # *guardar_dinheiro* updates
    if guardar_dinheiro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        guardar_dinheiro.frameNStart = frameN  # exact frame index
        guardar_dinheiro.tStart = t  # local t and not account for scr refresh
        guardar_dinheiro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(guardar_dinheiro, 'tStartRefresh')  # time at next scr refresh
        guardar_dinheiro.setAutoDraw(True)
    
    # *seta_avançar_2* updates
    if seta_avançar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seta_avançar_2.frameNStart = frameN  # exact frame index
        seta_avançar_2.tStart = t  # local t and not account for scr refresh
        seta_avançar_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seta_avançar_2, 'tStartRefresh')  # time at next scr refresh
        seta_avançar_2.setAutoDraw(True)
    
    # *text_avançar* updates
    if text_avançar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_avançar.frameNStart = frameN  # exact frame index
        text_avançar.tStart = t  # local t and not account for scr refresh
        text_avançar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_avançar, 'tStartRefresh')  # time at next scr refresh
        text_avançar.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(seta_avançar_2)
                    clickableList = seta_avançar_2
                except:
                    clickableList = [seta_avançar_2]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                x, y = mouse_2.getPos()
                mouse_2.x.append(x)
                mouse_2.y.append(y)
                buttons = mouse_2.getPressed()
                mouse_2.leftButton.append(buttons[0])
                mouse_2.midButton.append(buttons[1])
                mouse_2.rightButton.append(buttons[2])
                mouse_2.time.append(mouse_2.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_3" ---
for thisComponent in instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_2.x', mouse_2.x)
thisExp.addData('mouse_2.y', mouse_2.y)
thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
thisExp.addData('mouse_2.midButton', mouse_2.midButton)
thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
thisExp.addData('mouse_2.time', mouse_2.time)
thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes_B1.xlsx', selection='0:128'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    fundobranco2.setImage('branco.jpeg')
    bankButton.keys = []
    bankButton.rt = []
    _bankButton_allKeys = []
    # Run 'Begin Routine' code from updateEarnings
    if nReps==20:
        break
        
    balloonBody.setImage('redBalloon.png')
    molduraRM1.setImage('molduraRM1e2.png')
    molduraRM2.setImage('molduraRM1e2.png')
    molduraBVM.setImage('molduraBVM.png')
    molduraBM.setImage('Bau.png')
    # Run 'Begin Routine' code from setBalloonSize
    balloonSize=0.08
    popped=False
    nPumps=0
    # keep track of which components have finished
    trial_2Components = [fundobranco2, bankButton, balloonBody, molduraRM1, molduraRM2, molduraBVM, molduraBM, reminderMsg1, reminderMsg2, balloonValMsg, bankedMsg]
    for thisComponent in trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundobranco2* updates
        if fundobranco2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundobranco2.frameNStart = frameN  # exact frame index
            fundobranco2.tStart = t  # local t and not account for scr refresh
            fundobranco2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundobranco2, 'tStartRefresh')  # time at next scr refresh
            fundobranco2.setAutoDraw(True)
        
        # *bankButton* updates
        waitOnFlip = False
        if bankButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bankButton.frameNStart = frameN  # exact frame index
            bankButton.tStart = t  # local t and not account for scr refresh
            bankButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bankButton, 'tStartRefresh')  # time at next scr refresh
            bankButton.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(bankButton.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(bankButton.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if bankButton.status == STARTED and not waitOnFlip:
            theseKeys = bankButton.getKeys(keyList=['return'], waitRelease=False)
            _bankButton_allKeys.extend(theseKeys)
            if len(_bankButton_allKeys):
                bankButton.keys = _bankButton_allKeys[-1].name  # just the last key pressed
                bankButton.rt = _bankButton_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from updateEarnings
        thisBalloonEarnings=nPumps*0.50
        
        # *balloonBody* updates
        if balloonBody.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            balloonBody.frameNStart = frameN  # exact frame index
            balloonBody.tStart = t  # local t and not account for scr refresh
            balloonBody.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(balloonBody, 'tStartRefresh')  # time at next scr refresh
            balloonBody.setAutoDraw(True)
        if balloonBody.status == STARTED:  # only update if drawing
            balloonBody.setPos([0, -0.35 + balloonSize / 2], log=False)
            balloonBody.setSize(balloonSize, log=False)
        
        # *molduraRM1* updates
        if molduraRM1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            molduraRM1.frameNStart = frameN  # exact frame index
            molduraRM1.tStart = t  # local t and not account for scr refresh
            molduraRM1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(molduraRM1, 'tStartRefresh')  # time at next scr refresh
            molduraRM1.setAutoDraw(True)
        
        # *molduraRM2* updates
        if molduraRM2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            molduraRM2.frameNStart = frameN  # exact frame index
            molduraRM2.tStart = t  # local t and not account for scr refresh
            molduraRM2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(molduraRM2, 'tStartRefresh')  # time at next scr refresh
            molduraRM2.setAutoDraw(True)
        
        # *molduraBVM* updates
        if molduraBVM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            molduraBVM.frameNStart = frameN  # exact frame index
            molduraBVM.tStart = t  # local t and not account for scr refresh
            molduraBVM.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(molduraBVM, 'tStartRefresh')  # time at next scr refresh
            molduraBVM.setAutoDraw(True)
        
        # *molduraBM* updates
        if molduraBM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            molduraBM.frameNStart = frameN  # exact frame index
            molduraBM.tStart = t  # local t and not account for scr refresh
            molduraBM.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(molduraBM, 'tStartRefresh')  # time at next scr refresh
            molduraBM.setAutoDraw(True)
        
        # *reminderMsg1* updates
        if reminderMsg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reminderMsg1.frameNStart = frameN  # exact frame index
            reminderMsg1.tStart = t  # local t and not account for scr refresh
            reminderMsg1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reminderMsg1, 'tStartRefresh')  # time at next scr refresh
            reminderMsg1.setAutoDraw(True)
        
        # *reminderMsg2* updates
        if reminderMsg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reminderMsg2.frameNStart = frameN  # exact frame index
            reminderMsg2.tStart = t  # local t and not account for scr refresh
            reminderMsg2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reminderMsg2, 'tStartRefresh')  # time at next scr refresh
            reminderMsg2.setAutoDraw(True)
        
        # *balloonValMsg* updates
        if balloonValMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            balloonValMsg.frameNStart = frameN  # exact frame index
            balloonValMsg.tStart = t  # local t and not account for scr refresh
            balloonValMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(balloonValMsg, 'tStartRefresh')  # time at next scr refresh
            balloonValMsg.setAutoDraw(True)
        if balloonValMsg.status == STARTED:  # only update if drawing
            balloonValMsg.setText(f"Valor deste balão:\n{round(thisBalloonEarnings, 2)}€", log=False)
        
        # *bankedMsg* updates
        if bankedMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bankedMsg.frameNStart = frameN  # exact frame index
            bankedMsg.tStart = t  # local t and not account for scr refresh
            bankedMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bankedMsg, 'tStartRefresh')  # time at next scr refresh
            bankedMsg.setAutoDraw(True)
        if bankedMsg.status == STARTED:  # only update if drawing
            bankedMsg.setText(f"Já ganhou:\n{round(bankedEarnings, 2)}€", log=False)
        # Run 'Each Frame' code from checkKeys
        if event.getKeys(['space']):
          nPumps=nPumps+1
          if nPumps>maxPumps:
            popped=True
            continueRoutine=False
        # Run 'Each Frame' code from setBalloonSize
        balloonSize=0.1+nPumps*0.015
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_2" ---
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if bankButton.keys in ['', [], None]:  # No response was made
        bankButton.keys = None
    trials_2.addData('bankButton.keys',bankButton.keys)
    if bankButton.keys != None:  # we had a response
        trials_2.addData('bankButton.rt', bankButton.rt)
    # Run 'End Routine' code from updateEarnings
    #calculate cash 'earned'
    if popped:
      thisBalloonEarnings=0.00
      lastBalloonEarnings=0.00
    else:   lastBalloonEarnings=thisBalloonEarnings
    bankedEarnings = bankedEarnings+lastBalloonEarnings
    nReps=nReps+1 
    # Run 'End Routine' code from setBalloonSize
    #save data
    trials_2.addData('nPumps', nPumps)
    trials_2.addData('size', balloonSize)
    trials_2.addData('earnings', thisBalloonEarnings)
    trials_2.addData('popped', popped)
    
    # the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    fundobranco3.setImage('branco.jpeg')
    # Run 'Begin Routine' code from checkPopped
    if popped==True:
      feedbackText="Ups! Perdeu o valor deste balão!"
      bang.play()
    else:
      feedbackText=f"Guardou +{round(lastBalloonEarnings,2)}€" 
      coins.play()
    feedbackMsg22.setText(feedbackText)
    # keep track of which components have finished
    feedback_2Components = [fundobranco3, feedbackMsg22]
    for thisComponent in feedback_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback_2" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundobranco3* updates
        if fundobranco3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundobranco3.frameNStart = frameN  # exact frame index
            fundobranco3.tStart = t  # local t and not account for scr refresh
            fundobranco3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundobranco3, 'tStartRefresh')  # time at next scr refresh
            fundobranco3.setAutoDraw(True)
        if fundobranco3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fundobranco3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fundobranco3.tStop = t  # not accounting for scr refresh
                fundobranco3.frameNStop = frameN  # exact frame index
                fundobranco3.setAutoDraw(False)
        
        # *feedbackMsg22* updates
        if feedbackMsg22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackMsg22.frameNStart = frameN  # exact frame index
            feedbackMsg22.tStart = t  # local t and not account for scr refresh
            feedbackMsg22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackMsg22, 'tStartRefresh')  # time at next scr refresh
            feedbackMsg22.setAutoDraw(True)
        if feedbackMsg22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackMsg22.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                feedbackMsg22.tStop = t  # not accounting for scr refresh
                feedbackMsg22.frameNStop = frameN  # exact frame index
                feedbackMsg22.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_2" ---
    for thisComponent in feedback_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_7
    bart_manual_count = bart_manual_count + 1 
    bart_manual_resp[bart_manual_count] = {}
    bart_manual_resp[bart_manual_count]['user_pumps'] = nPumps
    bart_manual_resp[bart_manual_count]['max_pumps'] = maxPumps
    thisExp.addData('subjResponse', nPumps)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# --- Prepare to start Routine "final_score" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
finalScore.setText(f"Muito bem! Amealhou um total de {round(bankedEarnings, 2)}€")
# keep track of which components have finished
final_scoreComponents = [fundobranco4, finalScore]
for thisComponent in final_scoreComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "final_score" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fundobranco4* updates
    if fundobranco4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fundobranco4.frameNStart = frameN  # exact frame index
        fundobranco4.tStart = t  # local t and not account for scr refresh
        fundobranco4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fundobranco4, 'tStartRefresh')  # time at next scr refresh
        fundobranco4.setAutoDraw(True)
    if fundobranco4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fundobranco4.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            fundobranco4.tStop = t  # not accounting for scr refresh
            fundobranco4.frameNStop = frameN  # exact frame index
            fundobranco4.setAutoDraw(False)
    
    # *finalScore* updates
    if finalScore.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalScore.frameNStart = frameN  # exact frame index
        finalScore.tStart = t  # local t and not account for scr refresh
        finalScore.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalScore, 'tStartRefresh')  # time at next scr refresh
        finalScore.setAutoDraw(True)
    if finalScore.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finalScore.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            finalScore.tStop = t  # not accounting for scr refresh
            finalScore.frameNStop = frameN  # exact frame index
            finalScore.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_scoreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "final_score" ---
for thisComponent in final_scoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "farwell" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
farwellComponents = [_fundo_branco_final, farwell_, smile_final]
for thisComponent in farwellComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "farwell" ---
while continueRoutine and routineTimer.getTime() < 8.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *_fundo_branco_final* updates
    if _fundo_branco_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        _fundo_branco_final.frameNStart = frameN  # exact frame index
        _fundo_branco_final.tStart = t  # local t and not account for scr refresh
        _fundo_branco_final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(_fundo_branco_final, 'tStartRefresh')  # time at next scr refresh
        _fundo_branco_final.setAutoDraw(True)
    if _fundo_branco_final.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > _fundo_branco_final.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            _fundo_branco_final.tStop = t  # not accounting for scr refresh
            _fundo_branco_final.frameNStop = frameN  # exact frame index
            _fundo_branco_final.setAutoDraw(False)
    
    # *farwell_* updates
    if farwell_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        farwell_.frameNStart = frameN  # exact frame index
        farwell_.tStart = t  # local t and not account for scr refresh
        farwell_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(farwell_, 'tStartRefresh')  # time at next scr refresh
        farwell_.setAutoDraw(True)
    if farwell_.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > farwell_.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            farwell_.tStop = t  # not accounting for scr refresh
            farwell_.frameNStop = frameN  # exact frame index
            farwell_.setAutoDraw(False)
    
    # *smile_final* updates
    if smile_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        smile_final.frameNStart = frameN  # exact frame index
        smile_final.tStart = t  # local t and not account for scr refresh
        smile_final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(smile_final, 'tStartRefresh')  # time at next scr refresh
        smile_final.setAutoDraw(True)
    if smile_final.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > smile_final.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            smile_final.tStop = t  # not accounting for scr refresh
            smile_final.frameNStop = frameN  # exact frame index
            smile_final.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in farwellComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "farwell" ---
for thisComponent in farwellComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-8.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
