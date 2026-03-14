#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Wed Apr 24 16:05:26 2024
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

# Run 'Before Experiment' code from checkKeys
nPumps=0
# Run 'Before Experiment' code from checkKeys
nPumps=0
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'bart2'  # from the Builder filename that created this script
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
        originPath='/Volumes/Transcend/BART/bart_merged_3.py',
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
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units=None
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = None
    win.mouseVisible = False
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
        text='Bem vind@!\n\n\nDesde já, obrigada pela sua participação!\n\n\n\n\n\n\n\n\nPressione ENTER quando estiver preparado para começar',
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
        ori=0.0, pos=(0, -0.1), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "bart_manual" ---
    fundo_branco = visual.ImageStim(
        win=win,
        name='fundo_branco', 
        image='branco.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    Aguarde = visual.TextStim(win=win, name='Aguarde',
        text='Aguarde um pouco, por favor…\n\nDe seguida aparecerão as instruções da primeira tarefa!',
        font='Comic Sans',
        pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from code_6
    bart_manual_count = 0
    bart_manual_resp = {}
    
    # --- Initialize components for Routine "instructions" ---
    fundobranco = visual.ImageStim(
        win=win,
        name='fundobranco', 
        image='default.png', mask=None, anchor='center',
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0.3), size=(0.18, 0.18),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    balão_rebentado = visual.ImageStim(
        win=win,
        name='balão_rebentado', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.6, -0.1), size=(0.27, 0.27),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    perder_dinheiro = visual.ImageStim(
        win=win,
        name='perder_dinheiro', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, -0.1), size=(0.30, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    instruções1 = visual.TextStim(win=win, name='instruções1',
        text='Este é um jogo em que tem de optimizar os seus ganhos numa competição de encher balões.\n\nCada vez que enche o balão, acumula uma certa quantia em euros num “banco temporário”. Quando quiser, pode parar de encher o balão e guardar definitivamente esse valor. Contudo, se encher demasiadas vezes o balão e ele rebentar, perde o direito à quantia acumulada nesse mesmo balão. \n\n\nPressione a tecla ENTER para continuar a ler. ',
        font='Comic Sans',
        units='norm', pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    resposta = keyboard.Keyboard()
    
    # --- Initialize components for Routine "instructions_2" ---
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
        text='Os balões diferem entre si no seu ponto de explosão, que varia entre o primeiro pump e o 128º pump. Isto significa que os balões podem ocasionalmente alcançar um tamanho em que quase preenchem o ecrã, mas a maioria vai rebentar muito antes disso. \n\n\nDeve pressionar:\n\n ESPAÇO para encher o balão\n\n ENTER para guardar o valor do balão que está a encher e avançar para o próximo balão\n\nSe compreendeu as instruções, prima a tecla ENTER para iniciar a experiência.',
        font='Comic Sans',
        units='norm', pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    resposta2 = keyboard.Keyboard()
    encher_balão = visual.ImageStim(
        win=win,
        name='encher_balão', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.40, 0.01), size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    guardar_dinheiro = visual.ImageStim(
        win=win,
        name='guardar_dinheiro', units='height', 
        image='guardar_dinheiro.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0.55, -0.15), size=(0.17, 0.16),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "ITI" ---
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "trial_2" ---
    fundobranco2 = visual.ImageStim(
        win=win,
        name='fundobranco2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    bankButton = keyboard.Keyboard()
    # Run 'Begin Experiment' code from updateEarnings
    bankedEarnings=0.0
    lastBalloonEarnings=0.0
    thisBalloonEarnings=0.0
    balloonBody = visual.ImageStim(
        win=win,
        name='balloonBody', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=270.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    molduraRM1 = visual.ImageStim(
        win=win,
        name='molduraRM1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.4, -0.4), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    molduraRM2 = visual.ImageStim(
        win=win,
        name='molduraRM2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    molduraBVM = visual.ImageStim(
        win=win,
        name='molduraBVM', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.4), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    molduraBM = visual.ImageStim(
        win=win,
        name='molduraBM', units='height', 
        image='default.png', mask=None, anchor='center',
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
        image='default.png', mask=None, anchor='center',
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
    
    # --- Initialize components for Routine "bart_auto" ---
    fundo_branco_ = visual.ImageStim(
        win=win,
        name='fundo_branco_', 
        image='branco.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    nova_tarefa = visual.TextStim(win=win, name='nova_tarefa',
        text='Agora passaremos a uma outra tarefa, parecida com a anterior! \n\nPressione ENTER para começar a ler as instruções',
        font='Comic Sans',
        pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    resposta3 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from code_3
    bart_auto_count = 0
    bart_auto_resp = {}
    
    # --- Initialize components for Routine "instructions_3" ---
    fundobranco5 = visual.ImageStim(
        win=win,
        name='fundobranco5', 
        image='branco.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    balão_1 = visual.ImageStim(
        win=win,
        name='balão_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.7, 0), size=(0.18, 0.20),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    euro_1 = visual.ImageStim(
        win=win,
        name='euro_1', 
        image='euro.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, 0), size=(0.18, 0.195),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    instruções3 = visual.TextStim(win=win, name='instruções3',
        text='Este é um jogo em que tem de optimizar os seus ganhos numa competição de encher balões.\n\nPara cada balão que aparecer no ecrã, deverá definir um número de enchimentos. Cada enchimento acrescenta uma certa quantia em euros à sua conta fictícia. \nOs balões têm diferentes pontos de explosão, que variam entre o primeiro pump e o 128º pump (ou seja, uns explodirão com poucos enchimentos, enquanto outros quase preencherão o ecrã).\n\nPressione a tecla ENTER para continuar a ler.  ',
        font='Comic Sans',
        units='norm', pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    resposta_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "instructions_4" ---
    fundobranco6 = visual.ImageStim(
        win=win,
        name='fundobranco6', 
        image='branco.jpeg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    instruções4 = visual.TextStim(win=win, name='instruções4',
        text='No ecrã aparecerá uma caixa de texto em que deverá registar o número de enchimentos que pretende usar para o balão a aparecer de seguida. \n\nDepois de clicar para avançar, o balão aparece e encherá automaticamente até ao número definido, ou, se esse número for igual ou superior ao ponto de explosão desse balão específico, o balão explode. \n\nSe encher até ao número definido, arrecada o valor dos enchimentos desse balão; se, pelo contrário, o balão explodir, não ganha nada.\n\nSe compreendeu as instruções, prima a tecla ENTER para iniciar a experiência.',
        font='Comic Sans',
        units='norm', pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    resposta_3 = keyboard.Keyboard()
    encher_balão_1 = visual.ImageStim(
        win=win,
        name='encher_balão_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.7, 0.1), size=(0.17, 0.19),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    guardar_dinheiro_1 = visual.ImageStim(
        win=win,
        name='guardar_dinheiro_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.8, -0.4), size=(0.18, 0.20),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    balão_rebentado_ = visual.ImageStim(
        win=win,
        name='balão_rebentado_', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.8, 0.1), size=(0.29, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    perder_dinheiro_ = visual.ImageStim(
        win=win,
        name='perder_dinheiro_', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.8, -0.4), size=(0.32, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    
    # --- Initialize components for Routine "ITI" ---
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "trial_2" ---
    fundobranco2 = visual.ImageStim(
        win=win,
        name='fundobranco2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    bankButton = keyboard.Keyboard()
    # Run 'Begin Experiment' code from updateEarnings
    bankedEarnings=0.0
    lastBalloonEarnings=0.0
    thisBalloonEarnings=0.0
    balloonBody = visual.ImageStim(
        win=win,
        name='balloonBody', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=270.0, pos=[0,0], size=1.0,
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    molduraRM1 = visual.ImageStim(
        win=win,
        name='molduraRM1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.4, -0.4), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    molduraRM2 = visual.ImageStim(
        win=win,
        name='molduraRM2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, -0.4), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    molduraBVM = visual.ImageStim(
        win=win,
        name='molduraBVM', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.4), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    molduraBM = visual.ImageStim(
        win=win,
        name='molduraBM', units='height', 
        image='default.png', mask=None, anchor='center',
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
        image='default.png', mask=None, anchor='center',
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
    
    # --- Initialize components for Routine "final_score_2" ---
    fundobranco10 = visual.ImageStim(
        win=win,
        name='fundobranco10', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    finalScoref = visual.TextStim(win=win, name='finalScoref',
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
        text='A tarefa terminou. \nEstamos quase a acabar! Falta apenas mais uma tarefa, mais curta! \n\nA tua participação foi fundamental para a realização deste estudo no âmbito da minha tese de mestrado!\nObrigada!\n\n\n\n\n\n\n\nObrigada mais uma vez! ',
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
    
    # --- Prepare to start Routine "welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('welcome.started', globalClock.getTime())
    resposta_.keys = []
    resposta_.rt = []
    _resposta__allKeys = []
    # keep track of which components have finished
    welcomeComponents = [_fundo_branco_, welcome_, resposta_, smile]
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
    routineForceEnded = not continueRoutine
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, '_fundo_branco_.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resposta_.started')
            # update status
            resposta_.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resposta_.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resposta_.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resposta_.status == STARTED and not waitOnFlip:
            theseKeys = resposta_.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smile.started')
            # update status
            smile.status = STARTED
            smile.setAutoDraw(True)
        
        # if smile is active this frame...
        if smile.status == STARTED:
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
    thisExp.addData('welcome.stopped', globalClock.getTime())
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
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('bart_manual.started', globalClock.getTime())
    # keep track of which components have finished
    bart_manualComponents = [fundo_branco, Aguarde]
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
    routineForceEnded = not continueRoutine
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fundo_branco.started')
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
                fundo_branco.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fundo_branco.stopped')
                # update status
                fundo_branco.status = FINISHED
                fundo_branco.setAutoDraw(False)
        
        # *Aguarde* updates
        
        # if Aguarde is starting this frame...
        if Aguarde.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Aguarde.frameNStart = frameN  # exact frame index
            Aguarde.tStart = t  # local t and not account for scr refresh
            Aguarde.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Aguarde, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Aguarde.started')
            # update status
            Aguarde.status = STARTED
            Aguarde.setAutoDraw(True)
        
        # if Aguarde is active this frame...
        if Aguarde.status == STARTED:
            # update params
            pass
        
        # if Aguarde is stopping this frame...
        if Aguarde.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Aguarde.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Aguarde.tStop = t  # not accounting for scr refresh
                Aguarde.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Aguarde.stopped')
                # update status
                Aguarde.status = FINISHED
                Aguarde.setAutoDraw(False)
        
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
    thisExp.addData('bart_manual.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions.started', globalClock.getTime())
    fundobranco.setImage('branco.jpeg')
    euro.setImage('euro.png')
    balão_rebentado.setImage('balao_rebentado.jpeg')
    perder_dinheiro.setImage('perder_dinheiro.jpeg')
    resposta.keys = []
    resposta.rt = []
    _resposta_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [fundobranco, balão, euro, balão_rebentado, perder_dinheiro, instruções1, resposta]
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
    routineForceEnded = not continueRoutine
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fundobranco.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'balão.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'euro.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'balão_rebentado.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'perder_dinheiro.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruções1.started')
            # update status
            instruções1.status = STARTED
            instruções1.setAutoDraw(True)
        
        # if instruções1 is active this frame...
        if instruções1.status == STARTED:
            # update params
            pass
        
        # *resposta* updates
        waitOnFlip = False
        
        # if resposta is starting this frame...
        if resposta.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resposta.frameNStart = frameN  # exact frame index
            resposta.tStart = t  # local t and not account for scr refresh
            resposta.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resposta, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resposta.started')
            # update status
            resposta.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resposta.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resposta.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resposta.status == STARTED and not waitOnFlip:
            theseKeys = resposta.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _resposta_allKeys.extend(theseKeys)
            if len(_resposta_allKeys):
                resposta.keys = _resposta_allKeys[-1].name  # just the last key pressed
                resposta.rt = _resposta_allKeys[-1].rt
                resposta.duration = _resposta_allKeys[-1].duration
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
    thisExp.addData('instructions.stopped', globalClock.getTime())
    # check responses
    if resposta.keys in ['', [], None]:  # No response was made
        resposta.keys = None
    thisExp.addData('resposta.keys',resposta.keys)
    if resposta.keys != None:  # we had a response
        thisExp.addData('resposta.rt', resposta.rt)
        thisExp.addData('resposta.duration', resposta.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions_2.started', globalClock.getTime())
    resposta2.keys = []
    resposta2.rt = []
    _resposta2_allKeys = []
    encher_balão.setImage('encher_balao.jpeg')
    # keep track of which components have finished
    instructions_2Components = [fundobranco1, enter_tecla, instruções2, resposta2, encher_balão, guardar_dinheiro]
    for thisComponent in instructions_2Components:
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
    routineForceEnded = not continueRoutine
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fundobranco1.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'enter_tecla.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruções2.started')
            # update status
            instruções2.status = STARTED
            instruções2.setAutoDraw(True)
        
        # if instruções2 is active this frame...
        if instruções2.status == STARTED:
            # update params
            pass
        
        # *resposta2* updates
        waitOnFlip = False
        
        # if resposta2 is starting this frame...
        if resposta2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resposta2.frameNStart = frameN  # exact frame index
            resposta2.tStart = t  # local t and not account for scr refresh
            resposta2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resposta2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resposta2.started')
            # update status
            resposta2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resposta2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resposta2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resposta2.status == STARTED and not waitOnFlip:
            theseKeys = resposta2.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _resposta2_allKeys.extend(theseKeys)
            if len(_resposta2_allKeys):
                resposta2.keys = _resposta2_allKeys[-1].name  # just the last key pressed
                resposta2.rt = _resposta2_allKeys[-1].rt
                resposta2.duration = _resposta2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *encher_balão* updates
        
        # if encher_balão is starting this frame...
        if encher_balão.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encher_balão.frameNStart = frameN  # exact frame index
            encher_balão.tStart = t  # local t and not account for scr refresh
            encher_balão.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encher_balão, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'encher_balão.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'guardar_dinheiro.started')
            # update status
            guardar_dinheiro.status = STARTED
            guardar_dinheiro.setAutoDraw(True)
        
        # if guardar_dinheiro is active this frame...
        if guardar_dinheiro.status == STARTED:
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
        for thisComponent in instructions_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_2" ---
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions_2.stopped', globalClock.getTime())
    # check responses
    if resposta2.keys in ['', [], None]:  # No response was made
        resposta2.keys = None
    thisExp.addData('resposta2.keys',resposta2.keys)
    if resposta2.keys != None:  # we had a response
        thisExp.addData('resposta2.rt', resposta2.rt)
        thisExp.addData('resposta2.duration', resposta2.duration)
    thisExp.nextEntry()
    # the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trialTypes_B1.xlsx', selection='0:2'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        image.setImage('branco.jpeg')
        # keep track of which components have finished
        ITIComponents = [image]
        for thisComponent in ITIComponents:
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
        
        # --- Run Routine "ITI" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # if image is stopping this frame...
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + ITI_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    # update status
                    image.status = FINISHED
                    image.setAutoDraw(False)
            
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
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('ITI.stopped', globalClock.getTime())
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial_2.started', globalClock.getTime())
        fundobranco2.setImage('branco.jpeg')
        bankButton.keys = []
        bankButton.rt = []
        _bankButton_allKeys = []
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
        routineForceEnded = not continueRoutine
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fundobranco2.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bankButton.started')
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
            thisBalloonEarnings=nPumps*0.05
            
            # *balloonBody* updates
            
            # if balloonBody is starting this frame...
            if balloonBody.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                balloonBody.frameNStart = frameN  # exact frame index
                balloonBody.tStart = t  # local t and not account for scr refresh
                balloonBody.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(balloonBody, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'balloonBody.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'molduraRM1.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'molduraRM2.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'molduraBVM.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'molduraBM.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reminderMsg1.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reminderMsg2.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'balloonValMsg.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bankedMsg.started')
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
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
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
        thisExp.addData('trial_2.stopped', globalClock.getTime())
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
          thisBalloonEarnings=0.0
          lastBalloonEarnings=0.0
        else:   lastBalloonEarnings=thisBalloonEarnings
        bankedEarnings = bankedEarnings+lastBalloonEarnings
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
        # update component parameters for each repeat
        thisExp.addData('feedback_2.started', globalClock.getTime())
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
        routineForceEnded = not continueRoutine
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fundobranco3.started')
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
                    fundobranco3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fundobranco3.stopped')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackMsg22.started')
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
                    feedbackMsg22.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbackMsg22.stopped')
                    # update status
                    feedbackMsg22.status = FINISHED
                    feedbackMsg22.setAutoDraw(False)
            
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
        thisExp.addData('feedback_2.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_7
        bart_manual_count = bart_manual_count + 1 
        bart_manual_resp[bart_manual_count] = {}
        bart_manual_resp[bart_manual_count]['user_pumps'] = nPumps
        bart_manual_resp[bart_manual_count]['max_pumps'] = maxPumps
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_2'
    
    
    # --- Prepare to start Routine "final_score" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('final_score.started', globalClock.getTime())
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
    routineForceEnded = not continueRoutine
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fundobranco4.started')
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
                fundobranco4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fundobranco4.stopped')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finalScore.started')
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
                finalScore.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'finalScore.stopped')
                # update status
                finalScore.status = FINISHED
                finalScore.setAutoDraw(False)
        
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
    thisExp.addData('final_score.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "bart_auto" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('bart_auto.started', globalClock.getTime())
    resposta3.keys = []
    resposta3.rt = []
    _resposta3_allKeys = []
    # keep track of which components have finished
    bart_autoComponents = [fundo_branco_, nova_tarefa, resposta3]
    for thisComponent in bart_autoComponents:
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
    
    # --- Run Routine "bart_auto" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundo_branco_* updates
        
        # if fundo_branco_ is starting this frame...
        if fundo_branco_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundo_branco_.frameNStart = frameN  # exact frame index
            fundo_branco_.tStart = t  # local t and not account for scr refresh
            fundo_branco_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundo_branco_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fundo_branco_.started')
            # update status
            fundo_branco_.status = STARTED
            fundo_branco_.setAutoDraw(True)
        
        # if fundo_branco_ is active this frame...
        if fundo_branco_.status == STARTED:
            # update params
            pass
        
        # *nova_tarefa* updates
        
        # if nova_tarefa is starting this frame...
        if nova_tarefa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nova_tarefa.frameNStart = frameN  # exact frame index
            nova_tarefa.tStart = t  # local t and not account for scr refresh
            nova_tarefa.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nova_tarefa, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nova_tarefa.started')
            # update status
            nova_tarefa.status = STARTED
            nova_tarefa.setAutoDraw(True)
        
        # if nova_tarefa is active this frame...
        if nova_tarefa.status == STARTED:
            # update params
            pass
        
        # *resposta3* updates
        waitOnFlip = False
        
        # if resposta3 is starting this frame...
        if resposta3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resposta3.frameNStart = frameN  # exact frame index
            resposta3.tStart = t  # local t and not account for scr refresh
            resposta3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resposta3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resposta3.started')
            # update status
            resposta3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resposta3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resposta3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resposta3.status == STARTED and not waitOnFlip:
            theseKeys = resposta3.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _resposta3_allKeys.extend(theseKeys)
            if len(_resposta3_allKeys):
                resposta3.keys = _resposta3_allKeys[-1].name  # just the last key pressed
                resposta3.rt = _resposta3_allKeys[-1].rt
                resposta3.duration = _resposta3_allKeys[-1].duration
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
        for thisComponent in bart_autoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "bart_auto" ---
    for thisComponent in bart_autoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('bart_auto.stopped', globalClock.getTime())
    # check responses
    if resposta3.keys in ['', [], None]:  # No response was made
        resposta3.keys = None
    thisExp.addData('resposta3.keys',resposta3.keys)
    if resposta3.keys != None:  # we had a response
        thisExp.addData('resposta3.rt', resposta3.rt)
        thisExp.addData('resposta3.duration', resposta3.duration)
    thisExp.nextEntry()
    # the Routine "bart_auto" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions_3.started', globalClock.getTime())
    balão_1.setImage('balao_vermelho.jpeg')
    resposta_2.keys = []
    resposta_2.rt = []
    _resposta_2_allKeys = []
    # keep track of which components have finished
    instructions_3Components = [fundobranco5, balão_1, euro_1, instruções3, resposta_2]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundobranco5* updates
        
        # if fundobranco5 is starting this frame...
        if fundobranco5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundobranco5.frameNStart = frameN  # exact frame index
            fundobranco5.tStart = t  # local t and not account for scr refresh
            fundobranco5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundobranco5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fundobranco5.started')
            # update status
            fundobranco5.status = STARTED
            fundobranco5.setAutoDraw(True)
        
        # if fundobranco5 is active this frame...
        if fundobranco5.status == STARTED:
            # update params
            pass
        
        # *balão_1* updates
        
        # if balão_1 is starting this frame...
        if balão_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            balão_1.frameNStart = frameN  # exact frame index
            balão_1.tStart = t  # local t and not account for scr refresh
            balão_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(balão_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'balão_1.started')
            # update status
            balão_1.status = STARTED
            balão_1.setAutoDraw(True)
        
        # if balão_1 is active this frame...
        if balão_1.status == STARTED:
            # update params
            pass
        
        # *euro_1* updates
        
        # if euro_1 is starting this frame...
        if euro_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            euro_1.frameNStart = frameN  # exact frame index
            euro_1.tStart = t  # local t and not account for scr refresh
            euro_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(euro_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'euro_1.started')
            # update status
            euro_1.status = STARTED
            euro_1.setAutoDraw(True)
        
        # if euro_1 is active this frame...
        if euro_1.status == STARTED:
            # update params
            pass
        
        # *instruções3* updates
        
        # if instruções3 is starting this frame...
        if instruções3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruções3.frameNStart = frameN  # exact frame index
            instruções3.tStart = t  # local t and not account for scr refresh
            instruções3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruções3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruções3.started')
            # update status
            instruções3.status = STARTED
            instruções3.setAutoDraw(True)
        
        # if instruções3 is active this frame...
        if instruções3.status == STARTED:
            # update params
            pass
        
        # *resposta_2* updates
        waitOnFlip = False
        
        # if resposta_2 is starting this frame...
        if resposta_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resposta_2.frameNStart = frameN  # exact frame index
            resposta_2.tStart = t  # local t and not account for scr refresh
            resposta_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resposta_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resposta_2.started')
            # update status
            resposta_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resposta_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resposta_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resposta_2.status == STARTED and not waitOnFlip:
            theseKeys = resposta_2.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _resposta_2_allKeys.extend(theseKeys)
            if len(_resposta_2_allKeys):
                resposta_2.keys = _resposta_2_allKeys[-1].name  # just the last key pressed
                resposta_2.rt = _resposta_2_allKeys[-1].rt
                resposta_2.duration = _resposta_2_allKeys[-1].duration
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
    thisExp.addData('instructions_3.stopped', globalClock.getTime())
    # the Routine "instructions_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions_4.started', globalClock.getTime())
    resposta_3.keys = []
    resposta_3.rt = []
    _resposta_3_allKeys = []
    encher_balão_1.setImage('encher_balao.jpeg')
    guardar_dinheiro_1.setImage('guardar_dinheiro.jpeg')
    balão_rebentado_.setImage('balao_rebentado.jpeg')
    perder_dinheiro_.setImage('perder_dinheiro.jpeg')
    # keep track of which components have finished
    instructions_4Components = [fundobranco6, instruções4, resposta_3, encher_balão_1, guardar_dinheiro_1, balão_rebentado_, perder_dinheiro_]
    for thisComponent in instructions_4Components:
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
    
    # --- Run Routine "instructions_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundobranco6* updates
        
        # if fundobranco6 is starting this frame...
        if fundobranco6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundobranco6.frameNStart = frameN  # exact frame index
            fundobranco6.tStart = t  # local t and not account for scr refresh
            fundobranco6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundobranco6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fundobranco6.started')
            # update status
            fundobranco6.status = STARTED
            fundobranco6.setAutoDraw(True)
        
        # if fundobranco6 is active this frame...
        if fundobranco6.status == STARTED:
            # update params
            pass
        
        # *instruções4* updates
        
        # if instruções4 is starting this frame...
        if instruções4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruções4.frameNStart = frameN  # exact frame index
            instruções4.tStart = t  # local t and not account for scr refresh
            instruções4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruções4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruções4.started')
            # update status
            instruções4.status = STARTED
            instruções4.setAutoDraw(True)
        
        # if instruções4 is active this frame...
        if instruções4.status == STARTED:
            # update params
            pass
        
        # *resposta_3* updates
        waitOnFlip = False
        
        # if resposta_3 is starting this frame...
        if resposta_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resposta_3.frameNStart = frameN  # exact frame index
            resposta_3.tStart = t  # local t and not account for scr refresh
            resposta_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resposta_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resposta_3.started')
            # update status
            resposta_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resposta_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resposta_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resposta_3.status == STARTED and not waitOnFlip:
            theseKeys = resposta_3.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _resposta_3_allKeys.extend(theseKeys)
            if len(_resposta_3_allKeys):
                resposta_3.keys = _resposta_3_allKeys[-1].name  # just the last key pressed
                resposta_3.rt = _resposta_3_allKeys[-1].rt
                resposta_3.duration = _resposta_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *encher_balão_1* updates
        
        # if encher_balão_1 is starting this frame...
        if encher_balão_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encher_balão_1.frameNStart = frameN  # exact frame index
            encher_balão_1.tStart = t  # local t and not account for scr refresh
            encher_balão_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encher_balão_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'encher_balão_1.started')
            # update status
            encher_balão_1.status = STARTED
            encher_balão_1.setAutoDraw(True)
        
        # if encher_balão_1 is active this frame...
        if encher_balão_1.status == STARTED:
            # update params
            pass
        
        # *guardar_dinheiro_1* updates
        
        # if guardar_dinheiro_1 is starting this frame...
        if guardar_dinheiro_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            guardar_dinheiro_1.frameNStart = frameN  # exact frame index
            guardar_dinheiro_1.tStart = t  # local t and not account for scr refresh
            guardar_dinheiro_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(guardar_dinheiro_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'guardar_dinheiro_1.started')
            # update status
            guardar_dinheiro_1.status = STARTED
            guardar_dinheiro_1.setAutoDraw(True)
        
        # if guardar_dinheiro_1 is active this frame...
        if guardar_dinheiro_1.status == STARTED:
            # update params
            pass
        
        # *balão_rebentado_* updates
        
        # if balão_rebentado_ is starting this frame...
        if balão_rebentado_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            balão_rebentado_.frameNStart = frameN  # exact frame index
            balão_rebentado_.tStart = t  # local t and not account for scr refresh
            balão_rebentado_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(balão_rebentado_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'balão_rebentado_.started')
            # update status
            balão_rebentado_.status = STARTED
            balão_rebentado_.setAutoDraw(True)
        
        # if balão_rebentado_ is active this frame...
        if balão_rebentado_.status == STARTED:
            # update params
            pass
        
        # *perder_dinheiro_* updates
        
        # if perder_dinheiro_ is starting this frame...
        if perder_dinheiro_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            perder_dinheiro_.frameNStart = frameN  # exact frame index
            perder_dinheiro_.tStart = t  # local t and not account for scr refresh
            perder_dinheiro_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(perder_dinheiro_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'perder_dinheiro_.started')
            # update status
            perder_dinheiro_.status = STARTED
            perder_dinheiro_.setAutoDraw(True)
        
        # if perder_dinheiro_ is active this frame...
        if perder_dinheiro_.status == STARTED:
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
        for thisComponent in instructions_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_4" ---
    for thisComponent in instructions_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions_4.stopped', globalClock.getTime())
    # the Routine "instructions_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trialTypes_B2.xlsx', selection='0:2'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        image.setImage('branco.jpeg')
        # keep track of which components have finished
        ITIComponents = [image]
        for thisComponent in ITIComponents:
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
        
        # --- Run Routine "ITI" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # if image is stopping this frame...
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + ITI_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    # update status
                    image.status = FINISHED
                    image.setAutoDraw(False)
            
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
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('ITI.stopped', globalClock.getTime())
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial_2.started', globalClock.getTime())
        fundobranco2.setImage('branco.jpeg')
        bankButton.keys = []
        bankButton.rt = []
        _bankButton_allKeys = []
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
        routineForceEnded = not continueRoutine
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fundobranco2.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bankButton.started')
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
            thisBalloonEarnings=nPumps*0.05
            
            # *balloonBody* updates
            
            # if balloonBody is starting this frame...
            if balloonBody.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                balloonBody.frameNStart = frameN  # exact frame index
                balloonBody.tStart = t  # local t and not account for scr refresh
                balloonBody.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(balloonBody, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'balloonBody.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'molduraRM1.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'molduraRM2.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'molduraBVM.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'molduraBM.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reminderMsg1.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reminderMsg2.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'balloonValMsg.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bankedMsg.started')
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
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
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
        thisExp.addData('trial_2.stopped', globalClock.getTime())
        # check responses
        if bankButton.keys in ['', [], None]:  # No response was made
            bankButton.keys = None
        trials.addData('bankButton.keys',bankButton.keys)
        if bankButton.keys != None:  # we had a response
            trials.addData('bankButton.rt', bankButton.rt)
            trials.addData('bankButton.duration', bankButton.duration)
        # Run 'End Routine' code from updateEarnings
        #calculate cash 'earned'
        if popped:
          thisBalloonEarnings=0.0
          lastBalloonEarnings=0.0
        else:   lastBalloonEarnings=thisBalloonEarnings
        bankedEarnings = bankedEarnings+lastBalloonEarnings
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
        # update component parameters for each repeat
        thisExp.addData('feedback_2.started', globalClock.getTime())
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
        routineForceEnded = not continueRoutine
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fundobranco3.started')
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
                    fundobranco3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fundobranco3.stopped')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackMsg22.started')
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
                    feedbackMsg22.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbackMsg22.stopped')
                    # update status
                    feedbackMsg22.status = FINISHED
                    feedbackMsg22.setAutoDraw(False)
            
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
        thisExp.addData('feedback_2.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_7
        bart_manual_count = bart_manual_count + 1 
        bart_manual_resp[bart_manual_count] = {}
        bart_manual_resp[bart_manual_count]['user_pumps'] = nPumps
        bart_manual_resp[bart_manual_count]['max_pumps'] = maxPumps
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "final_score_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('final_score_2.started', globalClock.getTime())
    fundobranco10.setImage('branco.jpeg')
    finalScoref.setText(f"Muito bem! Amealhou um total de {round(bankedEarnings2, 2)}€")
    # keep track of which components have finished
    final_score_2Components = [fundobranco10, finalScoref]
    for thisComponent in final_score_2Components:
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
    
    # --- Run Routine "final_score_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fundobranco10* updates
        
        # if fundobranco10 is starting this frame...
        if fundobranco10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fundobranco10.frameNStart = frameN  # exact frame index
            fundobranco10.tStart = t  # local t and not account for scr refresh
            fundobranco10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fundobranco10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fundobranco10.started')
            # update status
            fundobranco10.status = STARTED
            fundobranco10.setAutoDraw(True)
        
        # if fundobranco10 is active this frame...
        if fundobranco10.status == STARTED:
            # update params
            pass
        
        # if fundobranco10 is stopping this frame...
        if fundobranco10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fundobranco10.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                fundobranco10.tStop = t  # not accounting for scr refresh
                fundobranco10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fundobranco10.stopped')
                # update status
                fundobranco10.status = FINISHED
                fundobranco10.setAutoDraw(False)
        
        # *finalScoref* updates
        
        # if finalScoref is starting this frame...
        if finalScoref.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finalScoref.frameNStart = frameN  # exact frame index
            finalScoref.tStart = t  # local t and not account for scr refresh
            finalScoref.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finalScoref, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'finalScoref.started')
            # update status
            finalScoref.status = STARTED
            finalScoref.setAutoDraw(True)
        
        # if finalScoref is active this frame...
        if finalScoref.status == STARTED:
            # update params
            pass
        
        # if finalScoref is stopping this frame...
        if finalScoref.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finalScoref.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                finalScoref.tStop = t  # not accounting for scr refresh
                finalScoref.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'finalScoref.stopped')
                # update status
                finalScoref.status = FINISHED
                finalScoref.setAutoDraw(False)
        
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
        for thisComponent in final_score_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "final_score_2" ---
    for thisComponent in final_score_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('final_score_2.stopped', globalClock.getTime())
    # Run 'End Routine' code from code_5
    import pandas as pd
    from datetime import datetime
    
    df_auto = pd.DataFrame(bart_auto_resp).T.reset_index()
    df_auto = df_auto.rename(columns = {'index': 'trial'})
    
    df_manual = pd.DataFrame(bart_manual_resp).T.reset_index()
    df_manual = df_manual.rename(columns = {'index': 'trial'})
    
    now = datetime.now()
    current_time = now.strftime('%Y%m%d_%H:%M:%S')
    
    nome_do_individuo = expInfo['participant']
    df_auto.to_csv(f'auto_bart_{nome_do_individuo}_{current_time}.csv')
    df_manual.to_csv(f'manual_bart_{nome_do_individuo}_{current_time}.csv')
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "farwell" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('farwell.started', globalClock.getTime())
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
    routineForceEnded = not continueRoutine
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, '_fundo_branco_final.started')
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
                _fundo_branco_final.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, '_fundo_branco_final.stopped')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'farwell_.started')
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
                farwell_.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'farwell_.stopped')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smile_final.started')
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
                smile_final.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'smile_final.stopped')
                # update status
                smile_final.status = FINISHED
                smile_final.setAutoDraw(False)
        
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
    thisExp.addData('farwell.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    
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
