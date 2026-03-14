#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Tue Jan  7 09:54:24 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from checkKeys
nPumps=0
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'bart2'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/marlenenogueira/Desktop/Lucia_CAD_project/wetransfer_bart_2024-12-05_1413/bart2.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units=None,
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = None
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('resposta_') is None:
        # initialise resposta_
        resposta_ = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resposta_',
        )
    if deviceManager.getDevice('bankButton') is None:
        # initialise bankButton
        bankButton = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='bankButton',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    _fundo_branco_ = visual.ImageStim(
        win=win,
        name='_fundo_branco_', 
        image='branco.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    welcome_ = visual.TextStim(win=win, name='welcome_',
        text='Bem vindo/a!\n\n\n\n\n\n\n\nDesde já, obrigada pela sua participação!\n',
        font='Comic Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    resposta_ = keyboard.Keyboard(deviceName='resposta_')
    smile = visual.ImageStim(
        win=win,
        name='smile', units='norm', 
        image='smile_inicial.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text_3 = visual.TextStim(win=win, name='text_3',
        text="\n\nPara avançar pressione a tecla 'ENTER'",
        font='Open Sans',
        pos=(0, -0.55), draggable=False, height=0.029, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "bart_manual" ---
    fundo_branco = visual.ImageStim(
        win=win,
        name='fundo_branco', 
        image='branco.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    balão = visual.ImageStim(
        win=win,
        name='balão', units='height', 
        image='redBalloon.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.6, 0.3), draggable=False, size=(0.18, 0.18),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    euro = visual.ImageStim(
        win=win,
        name='euro', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0.3), draggable=False, size=(0.18, 0.18),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    balão_rebentado = visual.ImageStim(
        win=win,
        name='balão_rebentado', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.6, -0.1), draggable=False, size=(0.27, 0.27),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    perder_dinheiro = visual.ImageStim(
        win=win,
        name='perder_dinheiro', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, -0.1), draggable=False, size=(0.30, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    instruções1 = visual.TextStim(win=win, name='instruções1',
        text='Neste jogo tem de ganhar o máximo possível numa competição de encher balões.\n\nCada vez que enche o balão, acumula euros. \n\nQuando quiser, pode parar de encher o balão e guardar esse valor. \n\nNo entanto, se encher demasiadas vezes o balão e ele rebentar, perde o o valor acumulado nesse mesmo balão. ',
        font='Comic Sans',
        units='norm', pos=(0, 0), draggable=False, height=0.09, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    seta_avançar = visual.ImageStim(
        win=win,
        name='seta_avançar', 
        image='Seta1.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, -0.8), draggable=False, size=(0.25, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    text_avançar_2 = visual.TextStim(win=win, name='text_avançar_2',
        text='Avançar',
        font='Open Sans',
        pos=(0.5, -0.8), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    mouse_1 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_1.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "instructions_2" ---
    fundobranco1 = visual.ImageStim(
        win=win,
        name='fundobranco1', 
        image='branco.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    enter_tecla = visual.ImageStim(
        win=win,
        name='enter_tecla', units='height', 
        image='enter_tecla.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(-0.63, -0.15), draggable=False, size=(0.33, 0.09),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    instruções2 = visual.TextStim(win=win, name='instruções2',
        text="Os balões podem rebentar a qualquer momento, desde o início.\n\nMas, quanto mais encher, maior a probabilidade de ele rebentar.\n\nIsto significa que os balões podem ocasionalmente alcançar um tamanho em que quase preenchem o ecrã, mas a maioria vai rebentar muito antes disso. \nDeve pressionar:\n\n 'ESPAÇO' para encher o balão\n\n'ENTER' para guardar o valor do balão que está a encher e avançar para o próximo balão\n\nTem alguma dúvida?",
        font='Comic Sans',
        units='norm', pos=(0, 0), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    encher_balão = visual.ImageStim(
        win=win,
        name='encher_balão', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.43, 0.02), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    guardar_dinheiro = visual.ImageStim(
        win=win,
        name='guardar_dinheiro', units='height', 
        image='guardar_dinheiro.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.55, -0.15), draggable=False, size=(0.17, 0.16),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    seta_avançar_2 = visual.ImageStim(
        win=win,
        name='seta_avançar_2', 
        image='Seta1.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, -0.8), draggable=False, size=(0.25, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_avançar = visual.TextStim(win=win, name='text_avançar',
        text='Avançar',
        font='Open Sans',
        pos=(0.5, -0.8), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    bankButton = keyboard.Keyboard(deviceName='bankButton')
    # Run 'Begin Experiment' code from updateEarnings
    lastBalloonEarnings=0.0
    thisBalloonEarnings=0.0
    nReps=0
    balloonBody = visual.ImageStim(
        win=win,
        name='balloonBody', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=270.0, pos=[0,0], draggable=False, size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    molduraRM1 = visual.ImageStim(
        win=win,
        name='molduraRM1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.4, -0.4), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    molduraRM2 = visual.ImageStim(
        win=win,
        name='molduraRM2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    molduraBVM = visual.ImageStim(
        win=win,
        name='molduraBVM', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.4), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    molduraBM = visual.ImageStim(
        win=win,
        name='molduraBM', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.65, 0.4), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    reminderMsg1 = visual.TextStim(win=win, name='reminderMsg1',
        text='ESPAÇO para encher o balão',
        font='Comic Sans',
        units='height', pos=(-0.4,-0.4), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    reminderMsg2 = visual.TextStim(win=win, name='reminderMsg2',
        text='ENTER para guardar o valor deste balão',
        font='Comic Sans',
        units='height', pos=(0.4, -0.4), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    balloonValMsg = visual.TextStim(win=win, name='balloonValMsg',
        text='',
        font='Comic Sans',
        units='height', pos=(0, 0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    bankedMsg = visual.TextStim(win=win, name='bankedMsg',
        text='',
        font='Comic Sans',
        units='height', pos=(0.5, 0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
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
        pos=(0, 0), draggable=False, height=0.09, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "final_score" ---
    fundobranco4 = visual.ImageStim(
        win=win,
        name='fundobranco4', 
        image='branco.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    finalScore = visual.TextStim(win=win, name='finalScore',
        text='',
        font='Comic Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "farwell" ---
    _fundo_branco_final = visual.ImageStim(
        win=win,
        name='_fundo_branco_final', 
        image='branco.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    farwell_ = visual.TextStim(win=win, name='farwell_',
        text='A tarefa terminou. \n\n\nA tua participação foi fundamental para a realização deste estudo!\n\nObrigada!\n\n\n\n\n\n\n\nObrigada mais uma vez! ',
        font='Comic Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    smile_final = visual.ImageStim(
        win=win,
        name='smile_final', 
        image='smile_final.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[_fundo_branco_, welcome_, resposta_, smile, text_3],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for resposta_
    resposta_.keys = []
    resposta_.rt = []
    _resposta__allKeys = []
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    thisExp.addData('welcome.started', welcome.tStart)
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
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
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *_fundo_branco_* updates
        
        # if _fundo_branco_ is starting this frame...
        if _fundo_branco_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            _fundo_branco_.frameNStart = frameN  # exact frame index
            _fundo_branco_.tStart = t  # local t and not account for scr refresh
            _fundo_branco_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(_fundo_branco_, 'tStartRefresh')  # time at next scr refresh
            # update status
            _fundo_branco_.status = STARTED
            _fundo_branco_.setAutoDraw(True)
        
        # if _fundo_branco_ is active this frame...
        if _fundo_branco_.status == STARTED:
            # update params
            pass
        
        # *welcome_* updates
        
        # if welcome_ is starting this frame...
        if welcome_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_.frameNStart = frameN  # exact frame index
            welcome_.tStart = t  # local t and not account for scr refresh
            welcome_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_, 'tStartRefresh')  # time at next scr refresh
            # update status
            welcome_.status = STARTED
            welcome_.setAutoDraw(True)
        
        # if welcome_ is active this frame...
        if welcome_.status == STARTED:
            # update params
            pass
        
        # *resposta_* updates
        waitOnFlip = False
        
        # if resposta_ is starting this frame...
        if resposta_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resposta_.frameNStart = frameN  # exact frame index
            resposta_.tStart = t  # local t and not account for scr refresh
            resposta_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resposta_, 'tStartRefresh')  # time at next scr refresh
            # update status
            resposta_.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resposta_.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resposta_.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resposta_.status == STARTED and not waitOnFlip:
            theseKeys = resposta_.getKeys(keyList=['a'], ignoreKeys=["escape"], waitRelease=False)
            _resposta__allKeys.extend(theseKeys)
            if len(_resposta__allKeys):
                resposta_.keys = _resposta__allKeys[-1].name  # just the last key pressed
                resposta_.rt = _resposta__allKeys[-1].rt
                resposta_.duration = _resposta__allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *smile* updates
        
        # if smile is starting this frame...
        if smile.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smile.frameNStart = frameN  # exact frame index
            smile.tStart = t  # local t and not account for scr refresh
            smile.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smile, 'tStartRefresh')  # time at next scr refresh
            # update status
            smile.status = STARTED
            smile.setAutoDraw(True)
        
        # if smile is active this frame...
        if smile.status == STARTED:
            # update params
            pass
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome.stopped', welcome.tStop)
    # check responses
    if resposta_.keys in ['', [], None]:  # No response was made
        resposta_.keys = None
    thisExp.addData('resposta_.keys',resposta_.keys)
    if resposta_.keys != None:  # we had a response
        thisExp.addData('resposta_.rt', resposta_.rt)
        thisExp.addData('resposta_.duration', resposta_.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "bart_manual" ---
    # create an object to store info about Routine bart_manual
    bart_manual = data.Routine(
        name='bart_manual',
        components=[fundo_branco],
    )
    bart_manual.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for bart_manual
    bart_manual.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    bart_manual.tStart = globalClock.getTime(format='float')
    bart_manual.status = STARTED
    thisExp.addData('bart_manual.started', bart_manual.tStart)
    bart_manual.maxDuration = None
    # keep track of which components have finished
    bart_manualComponents = bart_manual.components
    for thisComponent in bart_manual.components:
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
    bart_manual.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundo_branco* updates
        
        # if fundo_branco is starting this frame...
        if fundo_branco.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundo_branco.frameNStart = frameN  # exact frame index
            fundo_branco.tStart = t  # local t and not account for scr refresh
            fundo_branco.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundo_branco, 'tStartRefresh')  # time at next scr refresh
            # update status
            fundo_branco.status = STARTED
            fundo_branco.setAutoDraw(True)
        
        # if fundo_branco is active this frame...
        if fundo_branco.status == STARTED:
            # update params
            pass
        
        # if fundo_branco is stopping this frame...
        if fundo_branco.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fundo_branco.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fundo_branco.tStop = t  # not accounting for scr refresh
                fundo_branco.tStopRefresh = tThisFlipGlobal  # on global time
                fundo_branco.frameNStop = frameN  # exact frame index
                # update status
                fundo_branco.status = FINISHED
                fundo_branco.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            bart_manual.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bart_manual.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "bart_manual" ---
    for thisComponent in bart_manual.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for bart_manual
    bart_manual.tStop = globalClock.getTime(format='float')
    bart_manual.tStopRefresh = tThisFlipGlobal
    thisExp.addData('bart_manual.stopped', bart_manual.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if bart_manual.maxDurationReached:
        routineTimer.addTime(-bart_manual.maxDuration)
    elif bart_manual.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[fundobranco, balão, euro, balão_rebentado, perder_dinheiro, instruções1, seta_avançar, text_avançar_2, mouse_1],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
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
    # store start times for instructions
    instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions.tStart = globalClock.getTime(format='float')
    instructions.status = STARTED
    thisExp.addData('instructions.started', instructions.tStart)
    instructions.maxDuration = None
    # keep track of which components have finished
    instructionsComponents = instructions.components
    for thisComponent in instructions.components:
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
    instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundobranco* updates
        
        # if fundobranco is starting this frame...
        if fundobranco.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundobranco.frameNStart = frameN  # exact frame index
            fundobranco.tStart = t  # local t and not account for scr refresh
            fundobranco.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundobranco, 'tStartRefresh')  # time at next scr refresh
            # update status
            fundobranco.status = STARTED
            fundobranco.setAutoDraw(True)
        
        # if fundobranco is active this frame...
        if fundobranco.status == STARTED:
            # update params
            pass
        
        # *balão* updates
        
        # if balão is starting this frame...
        if balão.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            balão.frameNStart = frameN  # exact frame index
            balão.tStart = t  # local t and not account for scr refresh
            balão.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(balão, 'tStartRefresh')  # time at next scr refresh
            # update status
            balão.status = STARTED
            balão.setAutoDraw(True)
        
        # if balão is active this frame...
        if balão.status == STARTED:
            # update params
            pass
        
        # *euro* updates
        
        # if euro is starting this frame...
        if euro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            euro.frameNStart = frameN  # exact frame index
            euro.tStart = t  # local t and not account for scr refresh
            euro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(euro, 'tStartRefresh')  # time at next scr refresh
            # update status
            euro.status = STARTED
            euro.setAutoDraw(True)
        
        # if euro is active this frame...
        if euro.status == STARTED:
            # update params
            pass
        
        # *balão_rebentado* updates
        
        # if balão_rebentado is starting this frame...
        if balão_rebentado.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            balão_rebentado.frameNStart = frameN  # exact frame index
            balão_rebentado.tStart = t  # local t and not account for scr refresh
            balão_rebentado.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(balão_rebentado, 'tStartRefresh')  # time at next scr refresh
            # update status
            balão_rebentado.status = STARTED
            balão_rebentado.setAutoDraw(True)
        
        # if balão_rebentado is active this frame...
        if balão_rebentado.status == STARTED:
            # update params
            pass
        
        # *perder_dinheiro* updates
        
        # if perder_dinheiro is starting this frame...
        if perder_dinheiro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            perder_dinheiro.frameNStart = frameN  # exact frame index
            perder_dinheiro.tStart = t  # local t and not account for scr refresh
            perder_dinheiro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(perder_dinheiro, 'tStartRefresh')  # time at next scr refresh
            # update status
            perder_dinheiro.status = STARTED
            perder_dinheiro.setAutoDraw(True)
        
        # if perder_dinheiro is active this frame...
        if perder_dinheiro.status == STARTED:
            # update params
            pass
        
        # *instruções1* updates
        
        # if instruções1 is starting this frame...
        if instruções1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruções1.frameNStart = frameN  # exact frame index
            instruções1.tStart = t  # local t and not account for scr refresh
            instruções1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruções1, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruções1.status = STARTED
            instruções1.setAutoDraw(True)
        
        # if instruções1 is active this frame...
        if instruções1.status == STARTED:
            # update params
            pass
        
        # *seta_avançar* updates
        
        # if seta_avançar is starting this frame...
        if seta_avançar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            seta_avançar.frameNStart = frameN  # exact frame index
            seta_avançar.tStart = t  # local t and not account for scr refresh
            seta_avançar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seta_avançar, 'tStartRefresh')  # time at next scr refresh
            # update status
            seta_avançar.status = STARTED
            seta_avançar.setAutoDraw(True)
        
        # if seta_avançar is active this frame...
        if seta_avançar.status == STARTED:
            # update params
            pass
        
        # *text_avançar_2* updates
        
        # if text_avançar_2 is starting this frame...
        if text_avançar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_avançar_2.frameNStart = frameN  # exact frame index
            text_avançar_2.tStart = t  # local t and not account for scr refresh
            text_avançar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_avançar_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_avançar_2.status = STARTED
            text_avançar_2.setAutoDraw(True)
        
        # if text_avançar_2 is active this frame...
        if text_avançar_2.status == STARTED:
            # update params
            pass
        # *mouse_1* updates
        
        # if mouse_1 is starting this frame...
        if mouse_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_1.frameNStart = frameN  # exact frame index
            mouse_1.tStart = t  # local t and not account for scr refresh
            mouse_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_1, 'tStartRefresh')  # time at next scr refresh
            # update status
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
                    clickableList = environmenttools.getFromNames(seta_avançar, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_1):
                            gotValidClick = True
                            mouse_1.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_1.clicked_name.append(None)
                    x, y = mouse_1.getPos()
                    mouse_1.x.append(x)
                    mouse_1.y.append(y)
                    buttons = mouse_1.getPressed()
                    mouse_1.leftButton.append(buttons[0])
                    mouse_1.midButton.append(buttons[1])
                    mouse_1.rightButton.append(buttons[2])
                    mouse_1.time.append(mouse_1.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions
    instructions.tStop = globalClock.getTime(format='float')
    instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions.stopped', instructions.tStop)
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
    
    # --- Prepare to start Routine "instructions_2" ---
    # create an object to store info about Routine instructions_2
    instructions_2 = data.Routine(
        name='instructions_2',
        components=[fundobranco1, enter_tecla, instruções2, encher_balão, guardar_dinheiro, seta_avançar_2, text_avançar, mouse_2],
    )
    instructions_2.status = NOT_STARTED
    continueRoutine = True
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
    # store start times for instructions_2
    instructions_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_2.tStart = globalClock.getTime(format='float')
    instructions_2.status = STARTED
    thisExp.addData('instructions_2.started', instructions_2.tStart)
    instructions_2.maxDuration = None
    # keep track of which components have finished
    instructions_2Components = instructions_2.components
    for thisComponent in instructions_2.components:
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
    
    # --- Run Routine "instructions_2" ---
    instructions_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundobranco1* updates
        
        # if fundobranco1 is starting this frame...
        if fundobranco1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundobranco1.frameNStart = frameN  # exact frame index
            fundobranco1.tStart = t  # local t and not account for scr refresh
            fundobranco1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundobranco1, 'tStartRefresh')  # time at next scr refresh
            # update status
            fundobranco1.status = STARTED
            fundobranco1.setAutoDraw(True)
        
        # if fundobranco1 is active this frame...
        if fundobranco1.status == STARTED:
            # update params
            pass
        
        # *enter_tecla* updates
        
        # if enter_tecla is starting this frame...
        if enter_tecla.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enter_tecla.frameNStart = frameN  # exact frame index
            enter_tecla.tStart = t  # local t and not account for scr refresh
            enter_tecla.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enter_tecla, 'tStartRefresh')  # time at next scr refresh
            # update status
            enter_tecla.status = STARTED
            enter_tecla.setAutoDraw(True)
        
        # if enter_tecla is active this frame...
        if enter_tecla.status == STARTED:
            # update params
            pass
        
        # *instruções2* updates
        
        # if instruções2 is starting this frame...
        if instruções2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruções2.frameNStart = frameN  # exact frame index
            instruções2.tStart = t  # local t and not account for scr refresh
            instruções2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruções2, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruções2.status = STARTED
            instruções2.setAutoDraw(True)
        
        # if instruções2 is active this frame...
        if instruções2.status == STARTED:
            # update params
            pass
        
        # *encher_balão* updates
        
        # if encher_balão is starting this frame...
        if encher_balão.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encher_balão.frameNStart = frameN  # exact frame index
            encher_balão.tStart = t  # local t and not account for scr refresh
            encher_balão.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encher_balão, 'tStartRefresh')  # time at next scr refresh
            # update status
            encher_balão.status = STARTED
            encher_balão.setAutoDraw(True)
        
        # if encher_balão is active this frame...
        if encher_balão.status == STARTED:
            # update params
            pass
        
        # *guardar_dinheiro* updates
        
        # if guardar_dinheiro is starting this frame...
        if guardar_dinheiro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            guardar_dinheiro.frameNStart = frameN  # exact frame index
            guardar_dinheiro.tStart = t  # local t and not account for scr refresh
            guardar_dinheiro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(guardar_dinheiro, 'tStartRefresh')  # time at next scr refresh
            # update status
            guardar_dinheiro.status = STARTED
            guardar_dinheiro.setAutoDraw(True)
        
        # if guardar_dinheiro is active this frame...
        if guardar_dinheiro.status == STARTED:
            # update params
            pass
        
        # *seta_avançar_2* updates
        
        # if seta_avançar_2 is starting this frame...
        if seta_avançar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            seta_avançar_2.frameNStart = frameN  # exact frame index
            seta_avançar_2.tStart = t  # local t and not account for scr refresh
            seta_avançar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seta_avançar_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            seta_avançar_2.status = STARTED
            seta_avançar_2.setAutoDraw(True)
        
        # if seta_avançar_2 is active this frame...
        if seta_avançar_2.status == STARTED:
            # update params
            pass
        
        # *text_avançar* updates
        
        # if text_avançar is starting this frame...
        if text_avançar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_avançar.frameNStart = frameN  # exact frame index
            text_avançar.tStart = t  # local t and not account for scr refresh
            text_avançar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_avançar, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_avançar.status = STARTED
            text_avançar.setAutoDraw(True)
        
        # if text_avançar is active this frame...
        if text_avançar.status == STARTED:
            # update params
            pass
        # *mouse_2* updates
        
        # if mouse_2 is starting this frame...
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # update status
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
                    clickableList = environmenttools.getFromNames(seta_avançar_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_2.clicked_name.append(None)
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_2" ---
    for thisComponent in instructions_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_2
    instructions_2.tStop = globalClock.getTime(format='float')
    instructions_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_2.stopped', instructions_2.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_2.x', mouse_2.x)
    thisExp.addData('mouse_2.y', mouse_2.y)
    thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
    thisExp.addData('mouse_2.midButton', mouse_2.midButton)
    thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
    thisExp.addData('mouse_2.time', mouse_2.time)
    thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name)
    thisExp.nextEntry()
    # the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler2(
        name='trials_2',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        'trialTypes_B1.xlsx', 
        selection='0:128'
    )
    , 
        seed=None, 
    )
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "trial_2" ---
        # create an object to store info about Routine trial_2
        trial_2 = data.Routine(
            name='trial_2',
            components=[fundobranco2, bankButton, balloonBody, molduraRM1, molduraRM2, molduraBVM, molduraBM, reminderMsg1, reminderMsg2, balloonValMsg, bankedMsg],
        )
        trial_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        fundobranco2.setImage('branco.jpeg')
        # create starting attributes for bankButton
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
        # store start times for trial_2
        trial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial_2.tStart = globalClock.getTime(format='float')
        trial_2.status = STARTED
        thisExp.addData('trial_2.started', trial_2.tStart)
        trial_2.maxDuration = None
        # keep track of which components have finished
        trial_2Components = trial_2.components
        for thisComponent in trial_2.components:
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
        # if trial has changed, end Routine now
        if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
            continueRoutine = False
        trial_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fundobranco2* updates
            
            # if fundobranco2 is starting this frame...
            if fundobranco2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fundobranco2.frameNStart = frameN  # exact frame index
                fundobranco2.tStart = t  # local t and not account for scr refresh
                fundobranco2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fundobranco2, 'tStartRefresh')  # time at next scr refresh
                # update status
                fundobranco2.status = STARTED
                fundobranco2.setAutoDraw(True)
            
            # if fundobranco2 is active this frame...
            if fundobranco2.status == STARTED:
                # update params
                pass
            
            # *bankButton* updates
            waitOnFlip = False
            
            # if bankButton is starting this frame...
            if bankButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bankButton.frameNStart = frameN  # exact frame index
                bankButton.tStart = t  # local t and not account for scr refresh
                bankButton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bankButton, 'tStartRefresh')  # time at next scr refresh
                # update status
                bankButton.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(bankButton.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(bankButton.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if bankButton.status == STARTED and not waitOnFlip:
                theseKeys = bankButton.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _bankButton_allKeys.extend(theseKeys)
                if len(_bankButton_allKeys):
                    bankButton.keys = _bankButton_allKeys[-1].name  # just the last key pressed
                    bankButton.rt = _bankButton_allKeys[-1].rt
                    bankButton.duration = _bankButton_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from updateEarnings
            thisBalloonEarnings=nPumps*0.50
            
            # *balloonBody* updates
            
            # if balloonBody is starting this frame...
            if balloonBody.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                balloonBody.frameNStart = frameN  # exact frame index
                balloonBody.tStart = t  # local t and not account for scr refresh
                balloonBody.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(balloonBody, 'tStartRefresh')  # time at next scr refresh
                # update status
                balloonBody.status = STARTED
                balloonBody.setAutoDraw(True)
            
            # if balloonBody is active this frame...
            if balloonBody.status == STARTED:
                # update params
                balloonBody.setPos([0, -0.35 + balloonSize / 2], log=False)
                balloonBody.setSize(balloonSize, log=False)
            
            # *molduraRM1* updates
            
            # if molduraRM1 is starting this frame...
            if molduraRM1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                molduraRM1.frameNStart = frameN  # exact frame index
                molduraRM1.tStart = t  # local t and not account for scr refresh
                molduraRM1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(molduraRM1, 'tStartRefresh')  # time at next scr refresh
                # update status
                molduraRM1.status = STARTED
                molduraRM1.setAutoDraw(True)
            
            # if molduraRM1 is active this frame...
            if molduraRM1.status == STARTED:
                # update params
                pass
            
            # *molduraRM2* updates
            
            # if molduraRM2 is starting this frame...
            if molduraRM2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                molduraRM2.frameNStart = frameN  # exact frame index
                molduraRM2.tStart = t  # local t and not account for scr refresh
                molduraRM2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(molduraRM2, 'tStartRefresh')  # time at next scr refresh
                # update status
                molduraRM2.status = STARTED
                molduraRM2.setAutoDraw(True)
            
            # if molduraRM2 is active this frame...
            if molduraRM2.status == STARTED:
                # update params
                pass
            
            # *molduraBVM* updates
            
            # if molduraBVM is starting this frame...
            if molduraBVM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                molduraBVM.frameNStart = frameN  # exact frame index
                molduraBVM.tStart = t  # local t and not account for scr refresh
                molduraBVM.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(molduraBVM, 'tStartRefresh')  # time at next scr refresh
                # update status
                molduraBVM.status = STARTED
                molduraBVM.setAutoDraw(True)
            
            # if molduraBVM is active this frame...
            if molduraBVM.status == STARTED:
                # update params
                pass
            
            # *molduraBM* updates
            
            # if molduraBM is starting this frame...
            if molduraBM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                molduraBM.frameNStart = frameN  # exact frame index
                molduraBM.tStart = t  # local t and not account for scr refresh
                molduraBM.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(molduraBM, 'tStartRefresh')  # time at next scr refresh
                # update status
                molduraBM.status = STARTED
                molduraBM.setAutoDraw(True)
            
            # if molduraBM is active this frame...
            if molduraBM.status == STARTED:
                # update params
                pass
            
            # *reminderMsg1* updates
            
            # if reminderMsg1 is starting this frame...
            if reminderMsg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reminderMsg1.frameNStart = frameN  # exact frame index
                reminderMsg1.tStart = t  # local t and not account for scr refresh
                reminderMsg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reminderMsg1, 'tStartRefresh')  # time at next scr refresh
                # update status
                reminderMsg1.status = STARTED
                reminderMsg1.setAutoDraw(True)
            
            # if reminderMsg1 is active this frame...
            if reminderMsg1.status == STARTED:
                # update params
                pass
            
            # *reminderMsg2* updates
            
            # if reminderMsg2 is starting this frame...
            if reminderMsg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reminderMsg2.frameNStart = frameN  # exact frame index
                reminderMsg2.tStart = t  # local t and not account for scr refresh
                reminderMsg2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reminderMsg2, 'tStartRefresh')  # time at next scr refresh
                # update status
                reminderMsg2.status = STARTED
                reminderMsg2.setAutoDraw(True)
            
            # if reminderMsg2 is active this frame...
            if reminderMsg2.status == STARTED:
                # update params
                pass
            
            # *balloonValMsg* updates
            
            # if balloonValMsg is starting this frame...
            if balloonValMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                balloonValMsg.frameNStart = frameN  # exact frame index
                balloonValMsg.tStart = t  # local t and not account for scr refresh
                balloonValMsg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(balloonValMsg, 'tStartRefresh')  # time at next scr refresh
                # update status
                balloonValMsg.status = STARTED
                balloonValMsg.setAutoDraw(True)
            
            # if balloonValMsg is active this frame...
            if balloonValMsg.status == STARTED:
                # update params
                balloonValMsg.setText(f"Valor deste balão:\n{round(thisBalloonEarnings, 2)}€", log=False)
            
            # *bankedMsg* updates
            
            # if bankedMsg is starting this frame...
            if bankedMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bankedMsg.frameNStart = frameN  # exact frame index
                bankedMsg.tStart = t  # local t and not account for scr refresh
                bankedMsg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bankedMsg, 'tStartRefresh')  # time at next scr refresh
                # update status
                bankedMsg.status = STARTED
                bankedMsg.setAutoDraw(True)
            
            # if bankedMsg is active this frame...
            if bankedMsg.status == STARTED:
                # update params
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
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_2" ---
        for thisComponent in trial_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial_2
        trial_2.tStop = globalClock.getTime(format='float')
        trial_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial_2.stopped', trial_2.tStop)
        # check responses
        if bankButton.keys in ['', [], None]:  # No response was made
            bankButton.keys = None
        trials_2.addData('bankButton.keys',bankButton.keys)
        if bankButton.keys != None:  # we had a response
            trials_2.addData('bankButton.rt', bankButton.rt)
            trials_2.addData('bankButton.duration', bankButton.duration)
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
        # create an object to store info about Routine feedback_2
        feedback_2 = data.Routine(
            name='feedback_2',
            components=[fundobranco3, feedbackMsg22],
        )
        feedback_2.status = NOT_STARTED
        continueRoutine = True
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
        # store start times for feedback_2
        feedback_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_2.tStart = globalClock.getTime(format='float')
        feedback_2.status = STARTED
        thisExp.addData('feedback_2.started', feedback_2.tStart)
        feedback_2.maxDuration = None
        # keep track of which components have finished
        feedback_2Components = feedback_2.components
        for thisComponent in feedback_2.components:
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
        # if trial has changed, end Routine now
        if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
            continueRoutine = False
        feedback_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fundobranco3* updates
            
            # if fundobranco3 is starting this frame...
            if fundobranco3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fundobranco3.frameNStart = frameN  # exact frame index
                fundobranco3.tStart = t  # local t and not account for scr refresh
                fundobranco3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fundobranco3, 'tStartRefresh')  # time at next scr refresh
                # update status
                fundobranco3.status = STARTED
                fundobranco3.setAutoDraw(True)
            
            # if fundobranco3 is active this frame...
            if fundobranco3.status == STARTED:
                # update params
                pass
            
            # if fundobranco3 is stopping this frame...
            if fundobranco3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fundobranco3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fundobranco3.tStop = t  # not accounting for scr refresh
                    fundobranco3.tStopRefresh = tThisFlipGlobal  # on global time
                    fundobranco3.frameNStop = frameN  # exact frame index
                    # update status
                    fundobranco3.status = FINISHED
                    fundobranco3.setAutoDraw(False)
            
            # *feedbackMsg22* updates
            
            # if feedbackMsg22 is starting this frame...
            if feedbackMsg22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackMsg22.frameNStart = frameN  # exact frame index
                feedbackMsg22.tStart = t  # local t and not account for scr refresh
                feedbackMsg22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackMsg22, 'tStartRefresh')  # time at next scr refresh
                # update status
                feedbackMsg22.status = STARTED
                feedbackMsg22.setAutoDraw(True)
            
            # if feedbackMsg22 is active this frame...
            if feedbackMsg22.status == STARTED:
                # update params
                pass
            
            # if feedbackMsg22 is stopping this frame...
            if feedbackMsg22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackMsg22.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackMsg22.tStop = t  # not accounting for scr refresh
                    feedbackMsg22.tStopRefresh = tThisFlipGlobal  # on global time
                    feedbackMsg22.frameNStop = frameN  # exact frame index
                    # update status
                    feedbackMsg22.status = FINISHED
                    feedbackMsg22.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_2" ---
        for thisComponent in feedback_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_2
        feedback_2.tStop = globalClock.getTime(format='float')
        feedback_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_2.stopped', feedback_2.tStop)
        # Run 'End Routine' code from code_7
        bart_manual_count = bart_manual_count + 1 
        bart_manual_resp[bart_manual_count] = {}
        bart_manual_resp[bart_manual_count]['user_pumps'] = nPumps
        bart_manual_resp[bart_manual_count]['max_pumps'] = maxPumps
        thisExp.addData('subjResponse', nPumps)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_2.maxDurationReached:
            routineTimer.addTime(-feedback_2.maxDuration)
        elif feedback_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_2'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "final_score" ---
    # create an object to store info about Routine final_score
    final_score = data.Routine(
        name='final_score',
        components=[fundobranco4, finalScore],
    )
    final_score.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    finalScore.setText(f"Muito bem! Amealhou um total de {round(bankedEarnings, 2)}€")
    # store start times for final_score
    final_score.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    final_score.tStart = globalClock.getTime(format='float')
    final_score.status = STARTED
    thisExp.addData('final_score.started', final_score.tStart)
    final_score.maxDuration = None
    # keep track of which components have finished
    final_scoreComponents = final_score.components
    for thisComponent in final_score.components:
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
    final_score.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundobranco4* updates
        
        # if fundobranco4 is starting this frame...
        if fundobranco4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundobranco4.frameNStart = frameN  # exact frame index
            fundobranco4.tStart = t  # local t and not account for scr refresh
            fundobranco4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundobranco4, 'tStartRefresh')  # time at next scr refresh
            # update status
            fundobranco4.status = STARTED
            fundobranco4.setAutoDraw(True)
        
        # if fundobranco4 is active this frame...
        if fundobranco4.status == STARTED:
            # update params
            pass
        
        # if fundobranco4 is stopping this frame...
        if fundobranco4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fundobranco4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                fundobranco4.tStop = t  # not accounting for scr refresh
                fundobranco4.tStopRefresh = tThisFlipGlobal  # on global time
                fundobranco4.frameNStop = frameN  # exact frame index
                # update status
                fundobranco4.status = FINISHED
                fundobranco4.setAutoDraw(False)
        
        # *finalScore* updates
        
        # if finalScore is starting this frame...
        if finalScore.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finalScore.frameNStart = frameN  # exact frame index
            finalScore.tStart = t  # local t and not account for scr refresh
            finalScore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finalScore, 'tStartRefresh')  # time at next scr refresh
            # update status
            finalScore.status = STARTED
            finalScore.setAutoDraw(True)
        
        # if finalScore is active this frame...
        if finalScore.status == STARTED:
            # update params
            pass
        
        # if finalScore is stopping this frame...
        if finalScore.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finalScore.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                finalScore.tStop = t  # not accounting for scr refresh
                finalScore.tStopRefresh = tThisFlipGlobal  # on global time
                finalScore.frameNStop = frameN  # exact frame index
                # update status
                finalScore.status = FINISHED
                finalScore.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            final_score.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in final_score.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "final_score" ---
    for thisComponent in final_score.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for final_score
    final_score.tStop = globalClock.getTime(format='float')
    final_score.tStopRefresh = tThisFlipGlobal
    thisExp.addData('final_score.stopped', final_score.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if final_score.maxDurationReached:
        routineTimer.addTime(-final_score.maxDuration)
    elif final_score.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "farwell" ---
    # create an object to store info about Routine farwell
    farwell = data.Routine(
        name='farwell',
        components=[_fundo_branco_final, farwell_, smile_final],
    )
    farwell.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for farwell
    farwell.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    farwell.tStart = globalClock.getTime(format='float')
    farwell.status = STARTED
    thisExp.addData('farwell.started', farwell.tStart)
    farwell.maxDuration = None
    # keep track of which components have finished
    farwellComponents = farwell.components
    for thisComponent in farwell.components:
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
    farwell.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 8.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *_fundo_branco_final* updates
        
        # if _fundo_branco_final is starting this frame...
        if _fundo_branco_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            _fundo_branco_final.frameNStart = frameN  # exact frame index
            _fundo_branco_final.tStart = t  # local t and not account for scr refresh
            _fundo_branco_final.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(_fundo_branco_final, 'tStartRefresh')  # time at next scr refresh
            # update status
            _fundo_branco_final.status = STARTED
            _fundo_branco_final.setAutoDraw(True)
        
        # if _fundo_branco_final is active this frame...
        if _fundo_branco_final.status == STARTED:
            # update params
            pass
        
        # if _fundo_branco_final is stopping this frame...
        if _fundo_branco_final.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > _fundo_branco_final.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                _fundo_branco_final.tStop = t  # not accounting for scr refresh
                _fundo_branco_final.tStopRefresh = tThisFlipGlobal  # on global time
                _fundo_branco_final.frameNStop = frameN  # exact frame index
                # update status
                _fundo_branco_final.status = FINISHED
                _fundo_branco_final.setAutoDraw(False)
        
        # *farwell_* updates
        
        # if farwell_ is starting this frame...
        if farwell_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            farwell_.frameNStart = frameN  # exact frame index
            farwell_.tStart = t  # local t and not account for scr refresh
            farwell_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(farwell_, 'tStartRefresh')  # time at next scr refresh
            # update status
            farwell_.status = STARTED
            farwell_.setAutoDraw(True)
        
        # if farwell_ is active this frame...
        if farwell_.status == STARTED:
            # update params
            pass
        
        # if farwell_ is stopping this frame...
        if farwell_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > farwell_.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                farwell_.tStop = t  # not accounting for scr refresh
                farwell_.tStopRefresh = tThisFlipGlobal  # on global time
                farwell_.frameNStop = frameN  # exact frame index
                # update status
                farwell_.status = FINISHED
                farwell_.setAutoDraw(False)
        
        # *smile_final* updates
        
        # if smile_final is starting this frame...
        if smile_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smile_final.frameNStart = frameN  # exact frame index
            smile_final.tStart = t  # local t and not account for scr refresh
            smile_final.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smile_final, 'tStartRefresh')  # time at next scr refresh
            # update status
            smile_final.status = STARTED
            smile_final.setAutoDraw(True)
        
        # if smile_final is active this frame...
        if smile_final.status == STARTED:
            # update params
            pass
        
        # if smile_final is stopping this frame...
        if smile_final.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smile_final.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                smile_final.tStop = t  # not accounting for scr refresh
                smile_final.tStopRefresh = tThisFlipGlobal  # on global time
                smile_final.frameNStop = frameN  # exact frame index
                # update status
                smile_final.status = FINISHED
                smile_final.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            farwell.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in farwell.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "farwell" ---
    for thisComponent in farwell.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for farwell
    farwell.tStop = globalClock.getTime(format='float')
    farwell.tStopRefresh = tThisFlipGlobal
    thisExp.addData('farwell.stopped', farwell.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if farwell.maxDurationReached:
        routineTimer.addTime(-farwell.maxDuration)
    elif farwell.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
