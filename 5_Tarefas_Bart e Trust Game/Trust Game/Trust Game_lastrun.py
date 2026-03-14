#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Mon Aug  5 15:59:10 2024
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
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'Trust Game '  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
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
        originPath='/Volumes/Transcend/Trust Game/Trust Game_lastrun.py',
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
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
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
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1280, 800], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = True
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
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
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='event')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
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
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='Pyglet')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
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
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
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
    
    # --- Initialize components for Routine "CoverGame" ---
    CapaJogo = visual.ImageStim(
        win=win,
        name='CapaJogo', 
        image='Capa trust game.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    TítuloJogo = visual.TextStim(win=win, name='TítuloJogo',
        text='Jogo de Confiança',
        font='Comic Sans',
        pos=(0, 0.3), height=0.06, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    TeclaAvançar = visual.TextStim(win=win, name='TeclaAvançar',
        text='Para avançar pressione a "BARRA DE ESPAÇO"',
        font='Open Sans',
        pos=(0, -0.45), height=0.029, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Avançar = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Instructions1" ---
    text1 = visual.TextStim(win=win, name='text1',
        text='INSTRUÇÕES\n\nEste jogo funciona com dinheiro fictício.\n\nNo entanto, no final do jogo, o dinheiro que obtiver vai ser convertido em pontos para sortear um vale de 20€.\n\nEntão, o objetivo deste jogo é obter o máximo de dinheiro possível. \n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    TeclaAvançar_2 = visual.TextStim(win=win, name='TeclaAvançar_2',
        text='Para avançar pressione a SETA',
        font='Open Sans',
        pos=(0, -0.4), height=0.029, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    SetaAvançar_4 = visual.ImageStim(
        win=win,
        name='SetaAvançar_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    AvançarClick_3 = event.Mouse(win=win)
    x, y = [None, None]
    AvançarClick_3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Instructions2" ---
    textInstructions2 = visual.TextStim(win=win, name='textInstructions2',
        text='INSTRUÇÕES\n\nEste jogo é jogado a pares. \nVocê vai jogar com outro participante.\n\nPara ser anónimo o outro jogador vai ser chamado Participante 2.\n\nAmbos começam o jogo com 0€. \n\nO jogo é composto por 15 rondas. \n\nEm cada ronda você recebe 10€ para jogar.\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    SetaAvançar_5 = visual.ImageStim(
        win=win,
        name='SetaAvançar_5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    AvançarClick_4 = event.Mouse(win=win)
    x, y = [None, None]
    AvançarClick_4.mouseClock = core.Clock()
    imageP2 = visual.ImageStim(
        win=win,
        name='imageP2', 
        image='Player2.png', mask=None, anchor='center',
        ori=0.0, pos=(0.45, -0.05), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "Instructions3" ---
    textInstructions3 = visual.TextStim(win=win, name='textInstructions3',
        text='INSTRUÇÕES\n\nDepois de receber os 10€\nVocê pode escolher se quer dividir, ou não, com o Participante 2.\nE quanto quer dividir.\n\nPode escolher qualquer valor inteiro entre 0€ e 10€. \n\nSe escolher 0€:\nO Participante 2 não recebe nenhum dinheiro. \n\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    SetaAvançar_6 = visual.ImageStim(
        win=win,
        name='SetaAvançar_6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    AvançarClick_5 = event.Mouse(win=win)
    x, y = [None, None]
    AvançarClick_5.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Instructions4" ---
    textInstructions4 = visual.TextStim(win=win, name='textInstructions4',
        text='INSTRUÇÕES \n\nSe escolher partilhar algum dinheiro:\n\nO Participante 2 recebe o dinheiro a triplicar.\nE depois pode escolher devolver-lhe algum dinheiro, ou não. \n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    SetaAvançar_7 = visual.ImageStim(
        win=win,
        name='SetaAvançar_7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    AvançarClick_6 = event.Mouse(win=win)
    x, y = [None, None]
    AvançarClick_6.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "InstructionEx" ---
    SetaAvançar_8 = visual.ImageStim(
        win=win,
        name='SetaAvançar_8', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    AvançarClick_7 = event.Mouse(win=win)
    x, y = [None, None]
    AvançarClick_7.mouseClock = core.Clock()
    textExample = visual.TextStim(win=win, name='textExample',
        text='INSTRUÇÕES\n\nPor exemplo:\nSe você der 5€ ao Participante 2, ele vai receber 15€. \n\nEle pode escolher dividir os 15€ de qualquer forma. \n\nPode não partilhar e escolher ficar com os 15€.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "PracticeBegin" ---
    textPracticeBegin = visual.TextStim(win=win, name='textPracticeBegin',
        text='INSTRUÇÕES\n\nCada ronda termina com a decisão do Participante 2. \n\nComeça uma nova ronda e volta a receber 10€ para jogar. \n\nO saco de moedas mostra o dinheiro total que acumula no jogo.\n\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    SetaAvançar_2 = visual.ImageStim(
        win=win,
        name='SetaAvançar_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    AvançarClick_2 = event.Mouse(win=win)
    x, y = [None, None]
    AvançarClick_2.mouseClock = core.Clock()
    imageE1 = visual.ImageStim(
        win=win,
        name='imageE1', 
        image='SacoMoedas.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.4), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "WaitJogo" ---
    textJogo = visual.TextStim(win=win, name='textJogo',
        text='O Jogo vai começar!\n\nTem alguma dúvida que queira esclarecer com o investigador antes do jogo começar?\n\nSe não tiver dúvidas, selecione a seta para avançar. \n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    SetaAvançar_3 = visual.ImageStim(
        win=win,
        name='SetaAvançar_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    AvançarClick = event.Mouse(win=win)
    x, y = [None, None]
    AvançarClick.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial" ---
    closeEnvelope = visual.ImageStim(
        win=win,
        name='closeEnvelope', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.35), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    openEnvelope = visual.ImageStim(
        win=win,
        name='openEnvelope', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.4), size=(0.6, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    SetaConfiar = visual.ImageStim(
        win=win,
        name='SetaConfiar', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, -0.4), size=(0.25, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Confiar1 = visual.TextStim(win=win, name='Confiar1',
        text='',
        font='Open Sans',
        pos=(0.5, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-3.0);
    ConfiarClick = event.Mouse(win=win)
    x, y = [None, None]
    ConfiarClick.mouseClock = core.Clock()
    Player3 = visual.ImageStim(
        win=win,
        name='Player3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.35), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    Response = visual.TextStim(win=win, name='Response',
        text='',
        font='Open Sans',
        pos=(0, -0.41), height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    Question = visual.TextStim(win=win, name='Question',
        text='',
        font='Open Sans',
        pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    keyResp = keyboard.Keyboard()
    # Run 'Begin Experiment' code from code
    SelfScore= 0
    Player2Score=0
    nReps=1
    SacoMoedas = visual.ImageStim(
        win=win,
        name='SacoMoedas', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0.05), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    Total1 = visual.TextStim(win=win, name='Total1',
        text='',
        font='Open Sans',
        pos=(-0.5, -0.06), height=0.035, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    total2 = visual.TextStim(win=win, name='total2',
        text='',
        font='Open Sans',
        pos=(0, 0.19), height=0.035, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    RoundName = visual.TextStim(win=win, name='RoundName',
        text='',
        font='Open Sans',
        pos=(-0.5, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    
    # --- Initialize components for Routine "Decision1" ---
    closeEnvelopeD1 = visual.ImageStim(
        win=win,
        name='closeEnvelopeD1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(0.7, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    resultDecision1 = visual.TextStim(win=win, name='resultDecision1',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "WaitForResponse" ---
    Waiting = visual.ImageStim(
        win=win,
        name='Waiting', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), size=(0.35, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    textWaiting = visual.TextStim(win=win, name='textWaiting',
        text='A aguardar resposta do Participante 2 . . . ',
        font='Open Sans',
        pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "response" ---
    textResponse = visual.TextStim(win=win, name='textResponse',
        text='',
        font='Open Sans',
        pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imagePlayer2Response = visual.ImageStim(
        win=win,
        name='imagePlayer2Response', 
        image='Player2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), size=(0.45, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "Feedback" ---
    Player2Feedback = visual.ImageStim(
        win=win,
        name='Player2Feedback', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.3, 0.1), size=(0.25, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    SacoMoedasFeedback = visual.ImageStim(
        win=win,
        name='SacoMoedasFeedback', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.4, 0.05), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    Total2Feedback = visual.TextStim(win=win, name='Total2Feedback',
        text='',
        font='Open Sans',
        pos=(-0.4, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    SetaAvançar = visual.ImageStim(
        win=win,
        name='SetaAvançar', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=(0.2, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    Avançar1 = visual.TextStim(win=win, name='Avançar1',
        text='',
        font='Open Sans',
        pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-4.0);
    AvançarClick1 = event.Mouse(win=win)
    x, y = [None, None]
    AvançarClick1.mouseClock = core.Clock()
    TotalFeedbackPlayer2 = visual.TextStim(win=win, name='TotalFeedbackPlayer2',
        text='',
        font='Open Sans',
        pos=(0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    
    # --- Initialize components for Routine "EndScreen" ---
    ThanksMessage = visual.TextStim(win=win, name='ThanksMessage',
        text='',
        font='Open Sans',
        pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "CoverGame" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('CoverGame.started', globalClock.getTime())
    Avançar.keys = []
    Avançar.rt = []
    _Avançar_allKeys = []
    # keep track of which components have finished
    CoverGameComponents = [CapaJogo, TítuloJogo, TeclaAvançar, Avançar]
    for thisComponent in CoverGameComponents:
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
    
    # --- Run Routine "CoverGame" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CapaJogo* updates
        
        # if CapaJogo is starting this frame...
        if CapaJogo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CapaJogo.frameNStart = frameN  # exact frame index
            CapaJogo.tStart = t  # local t and not account for scr refresh
            CapaJogo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CapaJogo, 'tStartRefresh')  # time at next scr refresh
            # update status
            CapaJogo.status = STARTED
            CapaJogo.setAutoDraw(True)
        
        # if CapaJogo is active this frame...
        if CapaJogo.status == STARTED:
            # update params
            pass
        
        # *TítuloJogo* updates
        
        # if TítuloJogo is starting this frame...
        if TítuloJogo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            TítuloJogo.frameNStart = frameN  # exact frame index
            TítuloJogo.tStart = t  # local t and not account for scr refresh
            TítuloJogo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TítuloJogo, 'tStartRefresh')  # time at next scr refresh
            # update status
            TítuloJogo.status = STARTED
            TítuloJogo.setAutoDraw(True)
        
        # if TítuloJogo is active this frame...
        if TítuloJogo.status == STARTED:
            # update params
            pass
        
        # *TeclaAvançar* updates
        
        # if TeclaAvançar is starting this frame...
        if TeclaAvançar.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            TeclaAvançar.frameNStart = frameN  # exact frame index
            TeclaAvançar.tStart = t  # local t and not account for scr refresh
            TeclaAvançar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TeclaAvançar, 'tStartRefresh')  # time at next scr refresh
            # update status
            TeclaAvançar.status = STARTED
            TeclaAvançar.setAutoDraw(True)
        
        # if TeclaAvançar is active this frame...
        if TeclaAvançar.status == STARTED:
            # update params
            pass
        
        # *Avançar* updates
        
        # if Avançar is starting this frame...
        if Avançar.status == NOT_STARTED and t >= 5-frameTolerance:
            # keep track of start time/frame for later
            Avançar.frameNStart = frameN  # exact frame index
            Avançar.tStart = t  # local t and not account for scr refresh
            Avançar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Avançar, 'tStartRefresh')  # time at next scr refresh
            # update status
            Avançar.status = STARTED
            # keyboard checking is just starting
            Avançar.clock.reset()  # now t=0
            Avançar.clearEvents(eventType='keyboard')
        if Avançar.status == STARTED:
            theseKeys = Avançar.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Avançar_allKeys.extend(theseKeys)
            if len(_Avançar_allKeys):
                Avançar.keys = _Avançar_allKeys[-1].name  # just the last key pressed
                Avançar.rt = _Avançar_allKeys[-1].rt
                Avançar.duration = _Avançar_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CoverGameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CoverGame" ---
    for thisComponent in CoverGameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('CoverGame.stopped', globalClock.getTime())
    # check responses
    if Avançar.keys in ['', [], None]:  # No response was made
        Avançar.keys = None
    thisExp.addData('Avançar.keys',Avançar.keys)
    if Avançar.keys != None:  # we had a response
        thisExp.addData('Avançar.rt', Avançar.rt)
        thisExp.addData('Avançar.duration', Avançar.duration)
    thisExp.nextEntry()
    # the Routine "CoverGame" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions1.started', globalClock.getTime())
    SetaAvançar_4.setImage('Seta1.png')
    # setup some python lists for storing info about the AvançarClick_3
    AvançarClick_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Instructions1Components = [text1, TeclaAvançar_2, SetaAvançar_4, AvançarClick_3]
    for thisComponent in Instructions1Components:
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
    
    # --- Run Routine "Instructions1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text1* updates
        
        # if text1 is starting this frame...
        if text1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text1.frameNStart = frameN  # exact frame index
            text1.tStart = t  # local t and not account for scr refresh
            text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
            # update status
            text1.status = STARTED
            text1.setAutoDraw(True)
        
        # if text1 is active this frame...
        if text1.status == STARTED:
            # update params
            pass
        
        # *TeclaAvançar_2* updates
        
        # if TeclaAvançar_2 is starting this frame...
        if TeclaAvançar_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            TeclaAvançar_2.frameNStart = frameN  # exact frame index
            TeclaAvançar_2.tStart = t  # local t and not account for scr refresh
            TeclaAvançar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TeclaAvançar_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            TeclaAvançar_2.status = STARTED
            TeclaAvançar_2.setAutoDraw(True)
        
        # if TeclaAvançar_2 is active this frame...
        if TeclaAvançar_2.status == STARTED:
            # update params
            pass
        
        # *SetaAvançar_4* updates
        
        # if SetaAvançar_4 is starting this frame...
        if SetaAvançar_4.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            SetaAvançar_4.frameNStart = frameN  # exact frame index
            SetaAvançar_4.tStart = t  # local t and not account for scr refresh
            SetaAvançar_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SetaAvançar_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            SetaAvançar_4.status = STARTED
            SetaAvançar_4.setAutoDraw(True)
        
        # if SetaAvançar_4 is active this frame...
        if SetaAvançar_4.status == STARTED:
            # update params
            pass
        # *AvançarClick_3* updates
        
        # if AvançarClick_3 is starting this frame...
        if AvançarClick_3.status == NOT_STARTED and t >= 3-frameTolerance:
            # keep track of start time/frame for later
            AvançarClick_3.frameNStart = frameN  # exact frame index
            AvançarClick_3.tStart = t  # local t and not account for scr refresh
            AvançarClick_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AvançarClick_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            AvançarClick_3.status = STARTED
            AvançarClick_3.mouseClock.reset()
            prevButtonState = AvançarClick_3.getPressed()  # if button is down already this ISN'T a new click
        if AvançarClick_3.status == STARTED:  # only update if started and not finished!
            buttons = AvançarClick_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(SetaAvançar_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(AvançarClick_3):
                            gotValidClick = True
                            AvançarClick_3.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions1" ---
    for thisComponent in Instructions1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions1.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "Instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions2.started', globalClock.getTime())
    SetaAvançar_5.setImage('Seta1.png')
    # setup some python lists for storing info about the AvançarClick_4
    AvançarClick_4.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Instructions2Components = [textInstructions2, SetaAvançar_5, AvançarClick_4, imageP2]
    for thisComponent in Instructions2Components:
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
    
    # --- Run Routine "Instructions2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInstructions2* updates
        
        # if textInstructions2 is starting this frame...
        if textInstructions2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            textInstructions2.frameNStart = frameN  # exact frame index
            textInstructions2.tStart = t  # local t and not account for scr refresh
            textInstructions2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructions2, 'tStartRefresh')  # time at next scr refresh
            # update status
            textInstructions2.status = STARTED
            textInstructions2.setAutoDraw(True)
        
        # if textInstructions2 is active this frame...
        if textInstructions2.status == STARTED:
            # update params
            pass
        
        # *SetaAvançar_5* updates
        
        # if SetaAvançar_5 is starting this frame...
        if SetaAvançar_5.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            SetaAvançar_5.frameNStart = frameN  # exact frame index
            SetaAvançar_5.tStart = t  # local t and not account for scr refresh
            SetaAvançar_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SetaAvançar_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            SetaAvançar_5.status = STARTED
            SetaAvançar_5.setAutoDraw(True)
        
        # if SetaAvançar_5 is active this frame...
        if SetaAvançar_5.status == STARTED:
            # update params
            pass
        # *AvançarClick_4* updates
        
        # if AvançarClick_4 is starting this frame...
        if AvançarClick_4.status == NOT_STARTED and t >= 3-frameTolerance:
            # keep track of start time/frame for later
            AvançarClick_4.frameNStart = frameN  # exact frame index
            AvançarClick_4.tStart = t  # local t and not account for scr refresh
            AvançarClick_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AvançarClick_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            AvançarClick_4.status = STARTED
            AvançarClick_4.mouseClock.reset()
            prevButtonState = AvançarClick_4.getPressed()  # if button is down already this ISN'T a new click
        if AvançarClick_4.status == STARTED:  # only update if started and not finished!
            buttons = AvançarClick_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(SetaAvançar_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(AvançarClick_4):
                            gotValidClick = True
                            AvançarClick_4.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *imageP2* updates
        
        # if imageP2 is starting this frame...
        if imageP2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            imageP2.frameNStart = frameN  # exact frame index
            imageP2.tStart = t  # local t and not account for scr refresh
            imageP2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageP2, 'tStartRefresh')  # time at next scr refresh
            # update status
            imageP2.status = STARTED
            imageP2.setAutoDraw(True)
        
        # if imageP2 is active this frame...
        if imageP2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions2" ---
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions2.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions3.started', globalClock.getTime())
    SetaAvançar_6.setImage('Seta1.png')
    # setup some python lists for storing info about the AvançarClick_5
    AvançarClick_5.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Instructions3Components = [textInstructions3, SetaAvançar_6, AvançarClick_5]
    for thisComponent in Instructions3Components:
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
    
    # --- Run Routine "Instructions3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInstructions3* updates
        
        # if textInstructions3 is starting this frame...
        if textInstructions3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            textInstructions3.frameNStart = frameN  # exact frame index
            textInstructions3.tStart = t  # local t and not account for scr refresh
            textInstructions3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructions3, 'tStartRefresh')  # time at next scr refresh
            # update status
            textInstructions3.status = STARTED
            textInstructions3.setAutoDraw(True)
        
        # if textInstructions3 is active this frame...
        if textInstructions3.status == STARTED:
            # update params
            pass
        
        # *SetaAvançar_6* updates
        
        # if SetaAvançar_6 is starting this frame...
        if SetaAvançar_6.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            SetaAvançar_6.frameNStart = frameN  # exact frame index
            SetaAvançar_6.tStart = t  # local t and not account for scr refresh
            SetaAvançar_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SetaAvançar_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            SetaAvançar_6.status = STARTED
            SetaAvançar_6.setAutoDraw(True)
        
        # if SetaAvançar_6 is active this frame...
        if SetaAvançar_6.status == STARTED:
            # update params
            pass
        # *AvançarClick_5* updates
        
        # if AvançarClick_5 is starting this frame...
        if AvançarClick_5.status == NOT_STARTED and t >= 3-frameTolerance:
            # keep track of start time/frame for later
            AvançarClick_5.frameNStart = frameN  # exact frame index
            AvançarClick_5.tStart = t  # local t and not account for scr refresh
            AvançarClick_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AvançarClick_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            AvançarClick_5.status = STARTED
            AvançarClick_5.mouseClock.reset()
            prevButtonState = AvançarClick_5.getPressed()  # if button is down already this ISN'T a new click
        if AvançarClick_5.status == STARTED:  # only update if started and not finished!
            buttons = AvançarClick_5.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(SetaAvançar_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(AvançarClick_5):
                            gotValidClick = True
                            AvançarClick_5.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions3" ---
    for thisComponent in Instructions3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions3.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "Instructions3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions4" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions4.started', globalClock.getTime())
    SetaAvançar_7.setImage('Seta1.png')
    # setup some python lists for storing info about the AvançarClick_6
    AvançarClick_6.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Instructions4Components = [textInstructions4, SetaAvançar_7, AvançarClick_6]
    for thisComponent in Instructions4Components:
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
    
    # --- Run Routine "Instructions4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInstructions4* updates
        
        # if textInstructions4 is starting this frame...
        if textInstructions4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            textInstructions4.frameNStart = frameN  # exact frame index
            textInstructions4.tStart = t  # local t and not account for scr refresh
            textInstructions4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstructions4, 'tStartRefresh')  # time at next scr refresh
            # update status
            textInstructions4.status = STARTED
            textInstructions4.setAutoDraw(True)
        
        # if textInstructions4 is active this frame...
        if textInstructions4.status == STARTED:
            # update params
            pass
        
        # *SetaAvançar_7* updates
        
        # if SetaAvançar_7 is starting this frame...
        if SetaAvançar_7.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            SetaAvançar_7.frameNStart = frameN  # exact frame index
            SetaAvançar_7.tStart = t  # local t and not account for scr refresh
            SetaAvançar_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SetaAvançar_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            SetaAvançar_7.status = STARTED
            SetaAvançar_7.setAutoDraw(True)
        
        # if SetaAvançar_7 is active this frame...
        if SetaAvançar_7.status == STARTED:
            # update params
            pass
        # *AvançarClick_6* updates
        
        # if AvançarClick_6 is starting this frame...
        if AvançarClick_6.status == NOT_STARTED and t >= 3-frameTolerance:
            # keep track of start time/frame for later
            AvançarClick_6.frameNStart = frameN  # exact frame index
            AvançarClick_6.tStart = t  # local t and not account for scr refresh
            AvançarClick_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AvançarClick_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            AvançarClick_6.status = STARTED
            AvançarClick_6.mouseClock.reset()
            prevButtonState = AvançarClick_6.getPressed()  # if button is down already this ISN'T a new click
        if AvançarClick_6.status == STARTED:  # only update if started and not finished!
            buttons = AvançarClick_6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(SetaAvançar_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(AvançarClick_6):
                            gotValidClick = True
                            AvançarClick_6.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions4" ---
    for thisComponent in Instructions4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions4.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "Instructions4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "InstructionEx" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('InstructionEx.started', globalClock.getTime())
    SetaAvançar_8.setImage('Seta1.png')
    # setup some python lists for storing info about the AvançarClick_7
    AvançarClick_7.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    InstructionExComponents = [SetaAvançar_8, AvançarClick_7, textExample]
    for thisComponent in InstructionExComponents:
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
    
    # --- Run Routine "InstructionEx" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *SetaAvançar_8* updates
        
        # if SetaAvançar_8 is starting this frame...
        if SetaAvançar_8.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            SetaAvançar_8.frameNStart = frameN  # exact frame index
            SetaAvançar_8.tStart = t  # local t and not account for scr refresh
            SetaAvançar_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SetaAvançar_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            SetaAvançar_8.status = STARTED
            SetaAvançar_8.setAutoDraw(True)
        
        # if SetaAvançar_8 is active this frame...
        if SetaAvançar_8.status == STARTED:
            # update params
            pass
        # *AvançarClick_7* updates
        
        # if AvançarClick_7 is starting this frame...
        if AvançarClick_7.status == NOT_STARTED and t >= 3-frameTolerance:
            # keep track of start time/frame for later
            AvançarClick_7.frameNStart = frameN  # exact frame index
            AvançarClick_7.tStart = t  # local t and not account for scr refresh
            AvançarClick_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AvançarClick_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            AvançarClick_7.status = STARTED
            AvançarClick_7.mouseClock.reset()
            prevButtonState = AvançarClick_7.getPressed()  # if button is down already this ISN'T a new click
        if AvançarClick_7.status == STARTED:  # only update if started and not finished!
            buttons = AvançarClick_7.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(SetaAvançar_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(AvançarClick_7):
                            gotValidClick = True
                            AvançarClick_7.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *textExample* updates
        
        # if textExample is starting this frame...
        if textExample.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            textExample.frameNStart = frameN  # exact frame index
            textExample.tStart = t  # local t and not account for scr refresh
            textExample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textExample, 'tStartRefresh')  # time at next scr refresh
            # update status
            textExample.status = STARTED
            textExample.setAutoDraw(True)
        
        # if textExample is active this frame...
        if textExample.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionExComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionEx" ---
    for thisComponent in InstructionExComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('InstructionEx.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "InstructionEx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "PracticeBegin" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('PracticeBegin.started', globalClock.getTime())
    SetaAvançar_2.setImage('Seta1.png')
    # setup some python lists for storing info about the AvançarClick_2
    AvançarClick_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    PracticeBeginComponents = [textPracticeBegin, SetaAvançar_2, AvançarClick_2, imageE1]
    for thisComponent in PracticeBeginComponents:
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
    
    # --- Run Routine "PracticeBegin" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textPracticeBegin* updates
        
        # if textPracticeBegin is starting this frame...
        if textPracticeBegin.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            textPracticeBegin.frameNStart = frameN  # exact frame index
            textPracticeBegin.tStart = t  # local t and not account for scr refresh
            textPracticeBegin.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textPracticeBegin, 'tStartRefresh')  # time at next scr refresh
            # update status
            textPracticeBegin.status = STARTED
            textPracticeBegin.setAutoDraw(True)
        
        # if textPracticeBegin is active this frame...
        if textPracticeBegin.status == STARTED:
            # update params
            pass
        
        # *SetaAvançar_2* updates
        
        # if SetaAvançar_2 is starting this frame...
        if SetaAvançar_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            SetaAvançar_2.frameNStart = frameN  # exact frame index
            SetaAvançar_2.tStart = t  # local t and not account for scr refresh
            SetaAvançar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SetaAvançar_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            SetaAvançar_2.status = STARTED
            SetaAvançar_2.setAutoDraw(True)
        
        # if SetaAvançar_2 is active this frame...
        if SetaAvançar_2.status == STARTED:
            # update params
            pass
        # *AvançarClick_2* updates
        
        # if AvançarClick_2 is starting this frame...
        if AvançarClick_2.status == NOT_STARTED and t >= 3-frameTolerance:
            # keep track of start time/frame for later
            AvançarClick_2.frameNStart = frameN  # exact frame index
            AvançarClick_2.tStart = t  # local t and not account for scr refresh
            AvançarClick_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AvançarClick_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            AvançarClick_2.status = STARTED
            AvançarClick_2.mouseClock.reset()
            prevButtonState = AvançarClick_2.getPressed()  # if button is down already this ISN'T a new click
        if AvançarClick_2.status == STARTED:  # only update if started and not finished!
            buttons = AvançarClick_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(SetaAvançar_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(AvançarClick_2):
                            gotValidClick = True
                            AvançarClick_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *imageE1* updates
        
        # if imageE1 is starting this frame...
        if imageE1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            imageE1.frameNStart = frameN  # exact frame index
            imageE1.tStart = t  # local t and not account for scr refresh
            imageE1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageE1, 'tStartRefresh')  # time at next scr refresh
            # update status
            imageE1.status = STARTED
            imageE1.setAutoDraw(True)
        
        # if imageE1 is active this frame...
        if imageE1.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeBeginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PracticeBegin" ---
    for thisComponent in PracticeBeginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('PracticeBegin.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "PracticeBegin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "WaitJogo" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('WaitJogo.started', globalClock.getTime())
    SetaAvançar_3.setImage('Seta1.png')
    # setup some python lists for storing info about the AvançarClick
    AvançarClick.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    WaitJogoComponents = [textJogo, SetaAvançar_3, AvançarClick]
    for thisComponent in WaitJogoComponents:
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
    
    # --- Run Routine "WaitJogo" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textJogo* updates
        
        # if textJogo is starting this frame...
        if textJogo.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            textJogo.frameNStart = frameN  # exact frame index
            textJogo.tStart = t  # local t and not account for scr refresh
            textJogo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textJogo, 'tStartRefresh')  # time at next scr refresh
            # update status
            textJogo.status = STARTED
            textJogo.setAutoDraw(True)
        
        # if textJogo is active this frame...
        if textJogo.status == STARTED:
            # update params
            pass
        
        # *SetaAvançar_3* updates
        
        # if SetaAvançar_3 is starting this frame...
        if SetaAvançar_3.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            SetaAvançar_3.frameNStart = frameN  # exact frame index
            SetaAvançar_3.tStart = t  # local t and not account for scr refresh
            SetaAvançar_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SetaAvançar_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            SetaAvançar_3.status = STARTED
            SetaAvançar_3.setAutoDraw(True)
        
        # if SetaAvançar_3 is active this frame...
        if SetaAvançar_3.status == STARTED:
            # update params
            pass
        # *AvançarClick* updates
        
        # if AvançarClick is starting this frame...
        if AvançarClick.status == NOT_STARTED and t >= 2-frameTolerance:
            # keep track of start time/frame for later
            AvançarClick.frameNStart = frameN  # exact frame index
            AvançarClick.tStart = t  # local t and not account for scr refresh
            AvançarClick.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AvançarClick, 'tStartRefresh')  # time at next scr refresh
            # update status
            AvançarClick.status = STARTED
            AvançarClick.mouseClock.reset()
            prevButtonState = AvançarClick.getPressed()  # if button is down already this ISN'T a new click
        if AvançarClick.status == STARTED:  # only update if started and not finished!
            buttons = AvançarClick.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(SetaAvançar_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(AvançarClick):
                            gotValidClick = True
                            AvançarClick.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WaitJogoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WaitJogo" ---
    for thisComponent in WaitJogoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('WaitJogo.stopped', globalClock.getTime())
    # Run 'End Routine' code from codereset
    SelfScore=0
    Player2Score=0
    nReps=1
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "WaitJogo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials1 = data.TrialHandler(nReps=15.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials1')
    thisExp.addLoop(trials1)  # add the loop to the experiment
    thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            globals()[paramName] = thisTrials1[paramName]
    
    for thisTrials1 in trials1:
        currentLoop = trials1
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
        if thisTrials1 != None:
            for paramName in thisTrials1:
                globals()[paramName] = thisTrials1[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        closeEnvelope.setImage('envelopeFechado.png')
        openEnvelope.setImage('envelopeAberto.png')
        SetaConfiar.setImage('Seta1.png')
        Confiar1.setText('Confiar')
        # setup some python lists for storing info about the ConfiarClick
        ConfiarClick.clicked_name = []
        gotValidClick = False  # until a click is received
        Player3.setImage('Player2.png')
        Question.setText('Você tem 10€ para jogar.\n\n\nQuanto quer enviar ao outro jogador?')
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # Run 'Begin Routine' code from code
        
        
        respDisplay = ""
        maxDigits = 2
        
        #key logger defaults
        last_len = 0
        key_list = []
        
        
        SacoMoedas.setImage('SacoMoedas.png')
        Total1.setText(f"O meu bolso \nTotal " +str(SelfScore) +" €")
        total2.setText(f"Participante 2 \nTotal " + str(Player2Score) +" €"
        
         )
        RoundName.setText(f"Ronda " + str(nReps)
        )
        # keep track of which components have finished
        trialComponents = [closeEnvelope, openEnvelope, SetaConfiar, Confiar1, ConfiarClick, Player3, Response, Question, keyResp, SacoMoedas, Total1, total2, RoundName]
        for thisComponent in trialComponents:
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
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *closeEnvelope* updates
            
            # if closeEnvelope is starting this frame...
            if closeEnvelope.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                closeEnvelope.frameNStart = frameN  # exact frame index
                closeEnvelope.tStart = t  # local t and not account for scr refresh
                closeEnvelope.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(closeEnvelope, 'tStartRefresh')  # time at next scr refresh
                # update status
                closeEnvelope.status = STARTED
                closeEnvelope.setAutoDraw(True)
            
            # if closeEnvelope is active this frame...
            if closeEnvelope.status == STARTED:
                # update params
                pass
            
            # if closeEnvelope is stopping this frame...
            if closeEnvelope.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > closeEnvelope.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    closeEnvelope.tStop = t  # not accounting for scr refresh
                    closeEnvelope.frameNStop = frameN  # exact frame index
                    # update status
                    closeEnvelope.status = FINISHED
                    closeEnvelope.setAutoDraw(False)
            
            # *openEnvelope* updates
            
            # if openEnvelope is starting this frame...
            if openEnvelope.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                openEnvelope.frameNStart = frameN  # exact frame index
                openEnvelope.tStart = t  # local t and not account for scr refresh
                openEnvelope.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(openEnvelope, 'tStartRefresh')  # time at next scr refresh
                # update status
                openEnvelope.status = STARTED
                openEnvelope.setAutoDraw(True)
            
            # if openEnvelope is active this frame...
            if openEnvelope.status == STARTED:
                # update params
                pass
            
            # *SetaConfiar* updates
            
            # if SetaConfiar is starting this frame...
            if SetaConfiar.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                SetaConfiar.frameNStart = frameN  # exact frame index
                SetaConfiar.tStart = t  # local t and not account for scr refresh
                SetaConfiar.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SetaConfiar, 'tStartRefresh')  # time at next scr refresh
                # update status
                SetaConfiar.status = STARTED
                SetaConfiar.setAutoDraw(True)
            
            # if SetaConfiar is active this frame...
            if SetaConfiar.status == STARTED:
                # update params
                pass
            
            # *Confiar1* updates
            
            # if Confiar1 is starting this frame...
            if Confiar1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                Confiar1.frameNStart = frameN  # exact frame index
                Confiar1.tStart = t  # local t and not account for scr refresh
                Confiar1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Confiar1, 'tStartRefresh')  # time at next scr refresh
                # update status
                Confiar1.status = STARTED
                Confiar1.setAutoDraw(True)
            
            # if Confiar1 is active this frame...
            if Confiar1.status == STARTED:
                # update params
                pass
            # *ConfiarClick* updates
            
            # if ConfiarClick is starting this frame...
            if ConfiarClick.status == NOT_STARTED and t >= 2-frameTolerance:
                # keep track of start time/frame for later
                ConfiarClick.frameNStart = frameN  # exact frame index
                ConfiarClick.tStart = t  # local t and not account for scr refresh
                ConfiarClick.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ConfiarClick, 'tStartRefresh')  # time at next scr refresh
                # update status
                ConfiarClick.status = STARTED
                ConfiarClick.mouseClock.reset()
                prevButtonState = ConfiarClick.getPressed()  # if button is down already this ISN'T a new click
            if ConfiarClick.status == STARTED:  # only update if started and not finished!
                buttons = ConfiarClick.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(SetaConfiar, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(ConfiarClick):
                                gotValidClick = True
                                ConfiarClick.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # *Player3* updates
            
            # if Player3 is starting this frame...
            if Player3.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                Player3.frameNStart = frameN  # exact frame index
                Player3.tStart = t  # local t and not account for scr refresh
                Player3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Player3, 'tStartRefresh')  # time at next scr refresh
                # update status
                Player3.status = STARTED
                Player3.setAutoDraw(True)
            
            # if Player3 is active this frame...
            if Player3.status == STARTED:
                # update params
                pass
            
            # *Response* updates
            
            # if Response is starting this frame...
            if Response.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                Response.frameNStart = frameN  # exact frame index
                Response.tStart = t  # local t and not account for scr refresh
                Response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Response.started')
                # update status
                Response.status = STARTED
                Response.setAutoDraw(True)
            
            # if Response is active this frame...
            if Response.status == STARTED:
                # update params
                Response.setText(respDisplay+"€" , log=False)
            
            # *Question* updates
            
            # if Question is starting this frame...
            if Question.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                Question.frameNStart = frameN  # exact frame index
                Question.tStart = t  # local t and not account for scr refresh
                Question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Question, 'tStartRefresh')  # time at next scr refresh
                # update status
                Question.status = STARTED
                Question.setAutoDraw(True)
            
            # if Question is active this frame...
            if Question.status == STARTED:
                # update params
                pass
            
            # *keyResp* updates
            waitOnFlip = False
            
            # if keyResp is starting this frame...
            if keyResp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyResp.started')
                # update status
                keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyResp.status == STARTED and not waitOnFlip:
                theseKeys = keyResp.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'return', 'backspace'], ignoreKeys=["escape"], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = [key.name for key in _keyResp_allKeys]  # storing all keys
                    keyResp.rt = [key.rt for key in _keyResp_allKeys]
                    keyResp.duration = [key.duration for key in _keyResp_allKeys]
            # Run 'Each Frame' code from code
            #if a new key has been pressed since last time
            if(len(keyResp.keys) > last_len):
                
                #increment the key logger length
                last_len = len(keyResp.keys)
                
                #grab the last key added to the keys list
                key_list.append(keyResp.keys.pop())
            
                #check for backspace
                if("backspace" in key_list):
                    key_list.remove("backspace")
            
                    #if we have at least 1 character, remove it
                    if(len(key_list) > 0):
                        key_list.pop()
            
                #if enter is pressed then...
                elif("return" in key_list):
                    #remove the enter key
                    key_list.pop()
            
               
            
            
                #now loop through and remove any extra characters that may exist
                while(len(key_list) > maxDigits):
                    key_list.pop()
                    
                #create a variable to display
                respDisplay = ''.join(key_list)
            
            # *SacoMoedas* updates
            
            # if SacoMoedas is starting this frame...
            if SacoMoedas.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                SacoMoedas.frameNStart = frameN  # exact frame index
                SacoMoedas.tStart = t  # local t and not account for scr refresh
                SacoMoedas.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SacoMoedas, 'tStartRefresh')  # time at next scr refresh
                # update status
                SacoMoedas.status = STARTED
                SacoMoedas.setAutoDraw(True)
            
            # if SacoMoedas is active this frame...
            if SacoMoedas.status == STARTED:
                # update params
                pass
            
            # *Total1* updates
            
            # if Total1 is starting this frame...
            if Total1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                Total1.frameNStart = frameN  # exact frame index
                Total1.tStart = t  # local t and not account for scr refresh
                Total1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Total1, 'tStartRefresh')  # time at next scr refresh
                # update status
                Total1.status = STARTED
                Total1.setAutoDraw(True)
            
            # if Total1 is active this frame...
            if Total1.status == STARTED:
                # update params
                pass
            
            # *total2* updates
            
            # if total2 is starting this frame...
            if total2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                total2.frameNStart = frameN  # exact frame index
                total2.tStart = t  # local t and not account for scr refresh
                total2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(total2, 'tStartRefresh')  # time at next scr refresh
                # update status
                total2.status = STARTED
                total2.setAutoDraw(True)
            
            # if total2 is active this frame...
            if total2.status == STARTED:
                # update params
                pass
            
            # *RoundName* updates
            
            # if RoundName is starting this frame...
            if RoundName.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                RoundName.frameNStart = frameN  # exact frame index
                RoundName.tStart = t  # local t and not account for scr refresh
                RoundName.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RoundName, 'tStartRefresh')  # time at next scr refresh
                # update status
                RoundName.status = STARTED
                RoundName.setAutoDraw(True)
            
            # if RoundName is active this frame...
            if RoundName.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # store data for trials1 (TrialHandler)
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
        trials1.addData('keyResp.keys',keyResp.keys)
        if keyResp.keys != None:  # we had a response
            trials1.addData('keyResp.rt', keyResp.rt)
            trials1.addData('keyResp.duration', keyResp.duration)
        # Run 'End Routine' code from code
        thisExp.addData('subjResponse', respDisplay)
        respDisplayX3=int(respDisplay)*3
        SelfScore=SelfScore+(10-int(respDisplay))
        Player2Score=Player2Score+respDisplayX3
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Decision1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Decision1.started', globalClock.getTime())
        closeEnvelopeD1.setImage('envelopeFechado.png')
        resultDecision1.setText(f"Você enviou " + str(respDisplay) + " € \n\n\n\nO Participante 2 recebe \n\n" + str(respDisplayX3) +" €"
        
        
        
        
        )
        # keep track of which components have finished
        Decision1Components = [closeEnvelopeD1, resultDecision1]
        for thisComponent in Decision1Components:
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
        
        # --- Run Routine "Decision1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 7.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *closeEnvelopeD1* updates
            
            # if closeEnvelopeD1 is starting this frame...
            if closeEnvelopeD1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                closeEnvelopeD1.frameNStart = frameN  # exact frame index
                closeEnvelopeD1.tStart = t  # local t and not account for scr refresh
                closeEnvelopeD1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(closeEnvelopeD1, 'tStartRefresh')  # time at next scr refresh
                # update status
                closeEnvelopeD1.status = STARTED
                closeEnvelopeD1.setAutoDraw(True)
            
            # if closeEnvelopeD1 is active this frame...
            if closeEnvelopeD1.status == STARTED:
                # update params
                pass
            
            # if closeEnvelopeD1 is stopping this frame...
            if closeEnvelopeD1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > closeEnvelopeD1.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    closeEnvelopeD1.tStop = t  # not accounting for scr refresh
                    closeEnvelopeD1.frameNStop = frameN  # exact frame index
                    # update status
                    closeEnvelopeD1.status = FINISHED
                    closeEnvelopeD1.setAutoDraw(False)
            
            # *resultDecision1* updates
            
            # if resultDecision1 is starting this frame...
            if resultDecision1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                resultDecision1.frameNStart = frameN  # exact frame index
                resultDecision1.tStart = t  # local t and not account for scr refresh
                resultDecision1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resultDecision1, 'tStartRefresh')  # time at next scr refresh
                # update status
                resultDecision1.status = STARTED
                resultDecision1.setAutoDraw(True)
            
            # if resultDecision1 is active this frame...
            if resultDecision1.status == STARTED:
                # update params
                pass
            
            # if resultDecision1 is stopping this frame...
            if resultDecision1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resultDecision1.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    resultDecision1.tStop = t  # not accounting for scr refresh
                    resultDecision1.frameNStop = frameN  # exact frame index
                    # update status
                    resultDecision1.status = FINISHED
                    resultDecision1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Decision1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Decision1" ---
        for thisComponent in Decision1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Decision1.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.000000)
        
        # --- Prepare to start Routine "WaitForResponse" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('WaitForResponse.started', globalClock.getTime())
        Waiting.setImage('Waiting.png')
        # Run 'Begin Routine' code from code_2
        import random
        
        nWait = random.randint(3, 11)
        
        if nReps<5:
            respPlayer2 = random.randint(int(respDisplay), int(respDisplayX3))
        elif nReps >=6 and nReps <=10:
            respPlayer2 = random.randint(0, int(respDisplay))
        elif nReps >=11 and nReps <=15:
            respPlayer2 = random.randint(int(respDisplay), int(respDisplayX3))
        else:
            respPlayer2 =0
        
        # keep track of which components have finished
        WaitForResponseComponents = [Waiting, textWaiting]
        for thisComponent in WaitForResponseComponents:
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
        
        # --- Run Routine "WaitForResponse" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > nWait-frameTolerance:
                continueRoutine = False
            
            # *Waiting* updates
            
            # if Waiting is starting this frame...
            if Waiting.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Waiting.frameNStart = frameN  # exact frame index
                Waiting.tStart = t  # local t and not account for scr refresh
                Waiting.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Waiting, 'tStartRefresh')  # time at next scr refresh
                # update status
                Waiting.status = STARTED
                Waiting.setAutoDraw(True)
            
            # if Waiting is active this frame...
            if Waiting.status == STARTED:
                # update params
                pass
            
            # *textWaiting* updates
            
            # if textWaiting is starting this frame...
            if textWaiting.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textWaiting.frameNStart = frameN  # exact frame index
                textWaiting.tStart = t  # local t and not account for scr refresh
                textWaiting.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textWaiting, 'tStartRefresh')  # time at next scr refresh
                # update status
                textWaiting.status = STARTED
                textWaiting.setAutoDraw(True)
            
            # if textWaiting is active this frame...
            if textWaiting.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in WaitForResponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "WaitForResponse" ---
        for thisComponent in WaitForResponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('WaitForResponse.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_2
        SelfScore=SelfScore+respPlayer2
        Player2Score=Player2Score-respPlayer2
        nReps=nReps+1
        thisExp.addData('P2Response', respPlayer2)
        
        # the Routine "WaitForResponse" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "response" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('response.started', globalClock.getTime())
        textResponse.setText(f"O Participante 2 deu-lhe: \n\n + " 
        + str(respPlayer2) + " €"
        )
        # keep track of which components have finished
        responseComponents = [textResponse, imagePlayer2Response]
        for thisComponent in responseComponents:
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
        
        # --- Run Routine "response" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > 6-frameTolerance:
                continueRoutine = False
            
            # *textResponse* updates
            
            # if textResponse is starting this frame...
            if textResponse.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                textResponse.frameNStart = frameN  # exact frame index
                textResponse.tStart = t  # local t and not account for scr refresh
                textResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textResponse, 'tStartRefresh')  # time at next scr refresh
                # update status
                textResponse.status = STARTED
                textResponse.setAutoDraw(True)
            
            # if textResponse is active this frame...
            if textResponse.status == STARTED:
                # update params
                pass
            
            # if textResponse is stopping this frame...
            if textResponse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textResponse.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    textResponse.tStop = t  # not accounting for scr refresh
                    textResponse.frameNStop = frameN  # exact frame index
                    # update status
                    textResponse.status = FINISHED
                    textResponse.setAutoDraw(False)
            
            # *imagePlayer2Response* updates
            
            # if imagePlayer2Response is starting this frame...
            if imagePlayer2Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imagePlayer2Response.frameNStart = frameN  # exact frame index
                imagePlayer2Response.tStart = t  # local t and not account for scr refresh
                imagePlayer2Response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imagePlayer2Response, 'tStartRefresh')  # time at next scr refresh
                # update status
                imagePlayer2Response.status = STARTED
                imagePlayer2Response.setAutoDraw(True)
            
            # if imagePlayer2Response is active this frame...
            if imagePlayer2Response.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response" ---
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('response.stopped', globalClock.getTime())
        # the Routine "response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Feedback.started', globalClock.getTime())
        Player2Feedback.setImage('Player2.png')
        SacoMoedasFeedback.setImage('SacoMoedas.png')
        Total2Feedback.setText(f"O meu bolso \n\nTotal " + str(SelfScore) + " €"
        
        )
        SetaAvançar.setImage('Seta1.png')
        Avançar1.setText('Avançar')
        # setup some python lists for storing info about the AvançarClick1
        AvançarClick1.clicked_name = []
        gotValidClick = False  # until a click is received
        TotalFeedbackPlayer2.setText(f"Participante 2 \n\nTotal " +str(Player2Score) + " €"
         )
        # keep track of which components have finished
        FeedbackComponents = [Player2Feedback, SacoMoedasFeedback, Total2Feedback, SetaAvançar, Avançar1, AvançarClick1, TotalFeedbackPlayer2]
        for thisComponent in FeedbackComponents:
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
        
        # --- Run Routine "Feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Player2Feedback* updates
            
            # if Player2Feedback is starting this frame...
            if Player2Feedback.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                Player2Feedback.frameNStart = frameN  # exact frame index
                Player2Feedback.tStart = t  # local t and not account for scr refresh
                Player2Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Player2Feedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                Player2Feedback.status = STARTED
                Player2Feedback.setAutoDraw(True)
            
            # if Player2Feedback is active this frame...
            if Player2Feedback.status == STARTED:
                # update params
                pass
            
            # *SacoMoedasFeedback* updates
            
            # if SacoMoedasFeedback is starting this frame...
            if SacoMoedasFeedback.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                SacoMoedasFeedback.frameNStart = frameN  # exact frame index
                SacoMoedasFeedback.tStart = t  # local t and not account for scr refresh
                SacoMoedasFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SacoMoedasFeedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                SacoMoedasFeedback.status = STARTED
                SacoMoedasFeedback.setAutoDraw(True)
            
            # if SacoMoedasFeedback is active this frame...
            if SacoMoedasFeedback.status == STARTED:
                # update params
                pass
            
            # *Total2Feedback* updates
            
            # if Total2Feedback is starting this frame...
            if Total2Feedback.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                Total2Feedback.frameNStart = frameN  # exact frame index
                Total2Feedback.tStart = t  # local t and not account for scr refresh
                Total2Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Total2Feedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                Total2Feedback.status = STARTED
                Total2Feedback.setAutoDraw(True)
            
            # if Total2Feedback is active this frame...
            if Total2Feedback.status == STARTED:
                # update params
                pass
            
            # *SetaAvançar* updates
            
            # if SetaAvançar is starting this frame...
            if SetaAvançar.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                SetaAvançar.frameNStart = frameN  # exact frame index
                SetaAvançar.tStart = t  # local t and not account for scr refresh
                SetaAvançar.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SetaAvançar, 'tStartRefresh')  # time at next scr refresh
                # update status
                SetaAvançar.status = STARTED
                SetaAvançar.setAutoDraw(True)
            
            # if SetaAvançar is active this frame...
            if SetaAvançar.status == STARTED:
                # update params
                pass
            
            # *Avançar1* updates
            
            # if Avançar1 is starting this frame...
            if Avançar1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                Avançar1.frameNStart = frameN  # exact frame index
                Avançar1.tStart = t  # local t and not account for scr refresh
                Avançar1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Avançar1, 'tStartRefresh')  # time at next scr refresh
                # update status
                Avançar1.status = STARTED
                Avançar1.setAutoDraw(True)
            
            # if Avançar1 is active this frame...
            if Avançar1.status == STARTED:
                # update params
                pass
            # *AvançarClick1* updates
            
            # if AvançarClick1 is starting this frame...
            if AvançarClick1.status == NOT_STARTED and t >= 2-frameTolerance:
                # keep track of start time/frame for later
                AvançarClick1.frameNStart = frameN  # exact frame index
                AvançarClick1.tStart = t  # local t and not account for scr refresh
                AvançarClick1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AvançarClick1, 'tStartRefresh')  # time at next scr refresh
                # update status
                AvançarClick1.status = STARTED
                AvançarClick1.mouseClock.reset()
                prevButtonState = AvançarClick1.getPressed()  # if button is down already this ISN'T a new click
            if AvançarClick1.status == STARTED:  # only update if started and not finished!
                buttons = AvançarClick1.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(SetaAvançar, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(AvançarClick1):
                                gotValidClick = True
                                AvançarClick1.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # *TotalFeedbackPlayer2* updates
            
            # if TotalFeedbackPlayer2 is starting this frame...
            if TotalFeedbackPlayer2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                TotalFeedbackPlayer2.frameNStart = frameN  # exact frame index
                TotalFeedbackPlayer2.tStart = t  # local t and not account for scr refresh
                TotalFeedbackPlayer2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TotalFeedbackPlayer2, 'tStartRefresh')  # time at next scr refresh
                # update status
                TotalFeedbackPlayer2.status = STARTED
                TotalFeedbackPlayer2.setAutoDraw(True)
            
            # if TotalFeedbackPlayer2 is active this frame...
            if TotalFeedbackPlayer2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback" ---
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Feedback.stopped', globalClock.getTime())
        # store data for trials1 (TrialHandler)
        # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 15.0 repeats of 'trials1'
    
    
    # --- Prepare to start Routine "EndScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('EndScreen.started', globalClock.getTime())
    ThanksMessage.setText(f"Terminou o Jogo \n\n A sua pontuação final é de \n\n" + str(SelfScore) + " € \n\nIrá ser contactado posteriormente, caso seja selecionado no sorteio. \n\nMuito obrigada pela sua participação!"
    )
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    EndScreenComponents = [ThanksMessage, key_resp]
    for thisComponent in EndScreenComponents:
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
    
    # --- Run Routine "EndScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ThanksMessage* updates
        
        # if ThanksMessage is starting this frame...
        if ThanksMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ThanksMessage.frameNStart = frameN  # exact frame index
            ThanksMessage.tStart = t  # local t and not account for scr refresh
            ThanksMessage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ThanksMessage, 'tStartRefresh')  # time at next scr refresh
            # update status
            ThanksMessage.status = STARTED
            ThanksMessage.setAutoDraw(True)
        
        # if ThanksMessage is active this frame...
        if ThanksMessage.status == STARTED:
            # update params
            pass
        
        # if ThanksMessage is stopping this frame...
        if ThanksMessage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ThanksMessage.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                ThanksMessage.tStop = t  # not accounting for scr refresh
                ThanksMessage.frameNStop = frameN  # exact frame index
                # update status
                ThanksMessage.status = FINISHED
                ThanksMessage.setAutoDraw(False)
        
        # *key_resp* updates
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space', 'return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndScreen" ---
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('EndScreen.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # Run 'End Routine' code from code_4
    thisExp.addData('subjTotal', SelfScore)
    thisExp.addData('P2Total', Player2Score)
    # the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


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


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
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
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
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
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
