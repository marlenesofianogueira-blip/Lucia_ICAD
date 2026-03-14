/************** 
 * Bart2 *
 **************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'bart2';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(bart_manualRoutineBegin());
flowScheduler.add(bart_manualRoutineEachFrame());
flowScheduler.add(bart_manualRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(instructions_2RoutineBegin());
flowScheduler.add(instructions_2RoutineEachFrame());
flowScheduler.add(instructions_2RoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);



flowScheduler.add(final_scoreRoutineBegin());
flowScheduler.add(final_scoreRoutineEachFrame());
flowScheduler.add(final_scoreRoutineEnd());
flowScheduler.add(farwellRoutineBegin());
flowScheduler.add(farwellRoutineEachFrame());
flowScheduler.add(farwellRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'trialTypes_B1.xlsx', 'path': 'trialTypes_B1.xlsx'},
    {'name': 'branco.jpeg', 'path': 'branco.jpeg'},
    {'name': 'smile', 'path': 'smile'},
    {'name': 'smile_inicial.jpeg', 'path': 'smile_inicial.jpeg'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'redBalloon.png', 'path': 'redBalloon.png'},
    {'name': 'euro.png', 'path': 'euro.png'},
    {'name': 'balao_rebentado.jpeg', 'path': 'balao_rebentado.jpeg'},
    {'name': 'perder_dinheiro.jpeg', 'path': 'perder_dinheiro.jpeg'},
    {'name': 'enter_tecla.jpeg', 'path': 'enter_tecla.jpeg'},
    {'name': 'encher_balao.jpeg', 'path': 'encher_balao.jpeg'},
    {'name': 'guardar_dinheiro.jpeg', 'path': 'guardar_dinheiro.jpeg'},
    {'name': 'molduraRM1e2.png', 'path': 'molduraRM1e2.png'},
    {'name': 'molduraBVM.png', 'path': 'molduraBVM.png'},
    {'name': 'Bau.png', 'path': 'Bau.png'},
    {'name': 'smile_final.jpeg', 'path': 'smile_final.jpeg'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  _fundo_branco_ = new visual.ImageStim({
    win : psychoJS.window,
    name : '_fundo_branco_', units : undefined, 
    image : 'branco.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome',
    text: 'Bem vindo/a!\n\n\nDesde já, obrigada pela sua participação!\n\n\n\n\n\n\n\n\nPressione ENTER quando estiver preparado para começar',
    font: 'Comic Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  resposta = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  smile = new visual.ImageStim({
    win : psychoJS.window,
    name : 'smile', units : 'norm', 
    image : 'smile_inicial.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.1)], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "bart_manual"
  bart_manualClock = new util.Clock();
  fundo_branco = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fundo_branco', units : undefined, 
    image : 'branco.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  fundobranco = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fundobranco', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  balão = new visual.ImageStim({
    win : psychoJS.window,
    name : 'balão', units : 'height', 
    image : 'redBalloon.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.6), 0.3], size : [0.18, 0.18],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  euro = new visual.ImageStim({
    win : psychoJS.window,
    name : 'euro', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.6, 0.3], size : [0.18, 0.18],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  balão_rebentado = new visual.ImageStim({
    win : psychoJS.window,
    name : 'balão_rebentado', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.6), (- 0.1)], size : [0.27, 0.27],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  perder_dinheiro = new visual.ImageStim({
    win : psychoJS.window,
    name : 'perder_dinheiro', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.6, (- 0.1)], size : [0.3, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  instruções1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruções1',
    text: 'Neste jogo tem de ganhar o máximo possível numa competição de encher balões.\n\nCada vez que enche o balão, acumula euros. \nQuando quiser, pode parar de encher o balão e guardar esse valor. \nNo entanto, se encher demasiadas vezes o balão e ele rebentar, perde o o valor acumulado nesse mesmo balão. \n\n\nPressione a tecla ENTER para continuar a ler. ',
    font: 'Comic Sans',
    units: 'norm', 
    pos: [0, 0], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  resposta = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_2"
  instructions_2Clock = new util.Clock();
  fundobranco1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fundobranco1', units : undefined, 
    image : 'branco.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  enter_tecla = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enter_tecla', units : 'height', 
    image : 'enter_tecla.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.63), (- 0.15)], size : [0.33, 0.09],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  instruções2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruções2',
    text: 'Os balões podem rebentar a qualquer momento, desde o início.\nMas, quanto mais encher, maior a probabilidade de ele rebentar.\nIsto significa que os balões podem ocasionalmente alcançar um tamanho em que quase preenchem o ecrã, mas a maioria vai rebentar muito antes disso. \n\n\nDeve pressionar:\n\n ESPAÇO para encher o balão\n\n ENTER para guardar o valor do balão que está a encher e avançar para o próximo balão\n\nSe compreendeu as instruções, prima a tecla ENTER para iniciar a experiência.',
    font: 'Comic Sans',
    units: 'norm', 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  resposta2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  encher_balão = new visual.ImageStim({
    win : psychoJS.window,
    name : 'encher_balão', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.4, 0.01], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  guardar_dinheiro = new visual.ImageStim({
    win : psychoJS.window,
    name : 'guardar_dinheiro', units : 'height', 
    image : 'guardar_dinheiro.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.55, (- 0.15)], size : [0.17, 0.16],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "trial_2"
  trial_2Clock = new util.Clock();
  fundobranco2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fundobranco2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  bankButton = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from updateEarnings
  bankedEarnings = 0.0;
  lastBalloonEarnings = 0.0;
  thisBalloonEarnings = 0.0;
  
  balloonBody = new visual.ImageStim({
    win : psychoJS.window,
    name : 'balloonBody', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 270.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  molduraRM1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'molduraRM1', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.4), (- 0.4)], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  molduraRM2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'molduraRM2', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.4, (- 0.4)], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  molduraBVM = new visual.ImageStim({
    win : psychoJS.window,
    name : 'molduraBVM', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.4], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  molduraBM = new visual.ImageStim({
    win : psychoJS.window,
    name : 'molduraBM', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.65, 0.4], size : [0.1, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  reminderMsg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'reminderMsg1',
    text: 'ESPAÇO para encher o balão',
    font: 'Comic Sans',
    units: 'height', 
    pos: [(- 0.4), (- 0.4)], height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  reminderMsg2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'reminderMsg2',
    text: 'ENTER para guardar o valor deste balão',
    font: 'Comic Sans',
    units: 'height', 
    pos: [0.4, (- 0.4)], height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -9.0 
  });
  
  balloonValMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'balloonValMsg',
    text: '',
    font: 'Comic Sans',
    units: 'height', 
    pos: [0, 0.4], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -10.0 
  });
  
  bankedMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'bankedMsg',
    text: '',
    font: 'Comic Sans',
    units: 'height', 
    pos: [0.5, 0.4], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -11.0 
  });
  
  // Run 'Begin Experiment' code from setBalloonSize
  balloonSize = 0.08;
  balloonMsgHeight = 0.01;
  
  // Initialize components for Routine "feedback_2"
  feedback_2Clock = new util.Clock();
  fundobranco3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fundobranco3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Run 'Begin Experiment' code from checkPopped
  import {sound} from 'psychopy';
  var bang, feedbackText;
  feedbackText = "";
  bang = new sound.Sound("bang.wav");
  
  feedbackMsg22 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbackMsg22',
    text: '',
    font: 'Comic Sans',
    units: undefined, 
    pos: [0, 0], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "final_score"
  final_scoreClock = new util.Clock();
  fundobranco4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fundobranco4', units : undefined, 
    image : 'branco.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  finalScore = new visual.TextStim({
    win: psychoJS.window,
    name: 'finalScore',
    text: '',
    font: 'Comic Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "farwell"
  farwellClock = new util.Clock();
  _fundo_branco_final = new visual.ImageStim({
    win : psychoJS.window,
    name : '_fundo_branco_final', units : undefined, 
    image : 'branco.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  farwell = new visual.TextStim({
    win: psychoJS.window,
    name: 'farwell',
    text: 'A tarefa terminou. \n\n\nA tua participação foi fundamental para a realização deste estudo!\n\nObrigada!\n\n\n\n\n\n\n\nObrigada mais uma vez! ',
    font: 'Comic Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  smile_final = new visual.ImageStim({
    win : psychoJS.window,
    name : 'smile_final', units : undefined, 
    image : 'smile_final.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.1)], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    resposta.keys = undefined;
    resposta.rt = undefined;
    _resposta_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(_fundo_branco_);
    welcomeComponents.push(welcome);
    welcomeComponents.push(resposta);
    welcomeComponents.push(smile);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *_fundo_branco_* updates
    if (t >= 0.0 && _fundo_branco_.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      _fundo_branco_.tStart = t;  // (not accounting for frame time here)
      _fundo_branco_.frameNStart = frameN;  // exact frame index
      
      _fundo_branco_.setAutoDraw(true);
    }
    
    
    // *welcome* updates
    if (t >= 0.0 && welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome.tStart = t;  // (not accounting for frame time here)
      welcome.frameNStart = frameN;  // exact frame index
      
      welcome.setAutoDraw(true);
    }
    
    
    // *resposta* updates
    if (t >= 0.0 && resposta.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resposta.tStart = t;  // (not accounting for frame time here)
      resposta.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resposta.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resposta.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resposta.clearEvents(); });
    }
    
    if (resposta.status === PsychoJS.Status.STARTED) {
      let theseKeys = resposta.getKeys({keyList: ['return'], waitRelease: false});
      _resposta_allKeys = _resposta_allKeys.concat(theseKeys);
      if (_resposta_allKeys.length > 0) {
        resposta.keys = _resposta_allKeys[_resposta_allKeys.length - 1].name;  // just the last key pressed
        resposta.rt = _resposta_allKeys[_resposta_allKeys.length - 1].rt;
        resposta.duration = _resposta_allKeys[_resposta_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *smile* updates
    if (t >= 0.0 && smile.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      smile.tStart = t;  // (not accounting for frame time here)
      smile.frameNStart = frameN;  // exact frame index
      
      smile.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resposta.corr, level);
    }
    psychoJS.experiment.addData('resposta.keys', resposta.keys);
    if (typeof resposta.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resposta.rt', resposta.rt);
        psychoJS.experiment.addData('resposta.duration', resposta.duration);
        routineTimer.reset();
        }
    
    resposta.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function bart_manualRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'bart_manual' ---
    t = 0;
    bart_manualClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('bart_manual.started', globalClock.getTime());
    // keep track of which components have finished
    bart_manualComponents = [];
    bart_manualComponents.push(fundo_branco);
    
    for (const thisComponent of bart_manualComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function bart_manualRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'bart_manual' ---
    // get current time
    t = bart_manualClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fundo_branco* updates
    if (t >= 0.0 && fundo_branco.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fundo_branco.tStart = t;  // (not accounting for frame time here)
      fundo_branco.frameNStart = frameN;  // exact frame index
      
      fundo_branco.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fundo_branco.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fundo_branco.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of bart_manualComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function bart_manualRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'bart_manual' ---
    for (const thisComponent of bart_manualComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('bart_manual.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    fundobranco.setImage('branco.jpeg');
    euro.setImage('euro.png');
    balão_rebentado.setImage('balao_rebentado.jpeg');
    perder_dinheiro.setImage('perder_dinheiro.jpeg');
    resposta.keys = undefined;
    resposta.rt = undefined;
    _resposta_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(fundobranco);
    instructionsComponents.push(balão);
    instructionsComponents.push(euro);
    instructionsComponents.push(balão_rebentado);
    instructionsComponents.push(perder_dinheiro);
    instructionsComponents.push(instruções1);
    instructionsComponents.push(resposta);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fundobranco* updates
    if (t >= 0.0 && fundobranco.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fundobranco.tStart = t;  // (not accounting for frame time here)
      fundobranco.frameNStart = frameN;  // exact frame index
      
      fundobranco.setAutoDraw(true);
    }
    
    
    // *balão* updates
    if (t >= 0.0 && balão.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      balão.tStart = t;  // (not accounting for frame time here)
      balão.frameNStart = frameN;  // exact frame index
      
      balão.setAutoDraw(true);
    }
    
    
    // *euro* updates
    if (t >= 0.0 && euro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      euro.tStart = t;  // (not accounting for frame time here)
      euro.frameNStart = frameN;  // exact frame index
      
      euro.setAutoDraw(true);
    }
    
    
    // *balão_rebentado* updates
    if (t >= 0.0 && balão_rebentado.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      balão_rebentado.tStart = t;  // (not accounting for frame time here)
      balão_rebentado.frameNStart = frameN;  // exact frame index
      
      balão_rebentado.setAutoDraw(true);
    }
    
    
    // *perder_dinheiro* updates
    if (t >= 0.0 && perder_dinheiro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      perder_dinheiro.tStart = t;  // (not accounting for frame time here)
      perder_dinheiro.frameNStart = frameN;  // exact frame index
      
      perder_dinheiro.setAutoDraw(true);
    }
    
    
    // *instruções1* updates
    if (t >= 0.0 && instruções1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruções1.tStart = t;  // (not accounting for frame time here)
      instruções1.frameNStart = frameN;  // exact frame index
      
      instruções1.setAutoDraw(true);
    }
    
    
    // *resposta* updates
    if (t >= 0.0 && resposta.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resposta.tStart = t;  // (not accounting for frame time here)
      resposta.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resposta.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resposta.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resposta.clearEvents(); });
    }
    
    if (resposta.status === PsychoJS.Status.STARTED) {
      let theseKeys = resposta.getKeys({keyList: ['return'], waitRelease: false});
      _resposta_allKeys = _resposta_allKeys.concat(theseKeys);
      if (_resposta_allKeys.length > 0) {
        resposta.keys = _resposta_allKeys[_resposta_allKeys.length - 1].name;  // just the last key pressed
        resposta.rt = _resposta_allKeys[_resposta_allKeys.length - 1].rt;
        resposta.duration = _resposta_allKeys[_resposta_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resposta.corr, level);
    }
    psychoJS.experiment.addData('resposta.keys', resposta.keys);
    if (typeof resposta.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resposta.rt', resposta.rt);
        psychoJS.experiment.addData('resposta.duration', resposta.duration);
        routineTimer.reset();
        }
    
    resposta.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function instructions_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_2' ---
    t = 0;
    instructions_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions_2.started', globalClock.getTime());
    resposta2.keys = undefined;
    resposta2.rt = undefined;
    _resposta2_allKeys = [];
    encher_balão.setImage('encher_balao.jpeg');
    // keep track of which components have finished
    instructions_2Components = [];
    instructions_2Components.push(fundobranco1);
    instructions_2Components.push(enter_tecla);
    instructions_2Components.push(instruções2);
    instructions_2Components.push(resposta2);
    instructions_2Components.push(encher_balão);
    instructions_2Components.push(guardar_dinheiro);
    
    for (const thisComponent of instructions_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instructions_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_2' ---
    // get current time
    t = instructions_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fundobranco1* updates
    if (t >= 0.0 && fundobranco1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fundobranco1.tStart = t;  // (not accounting for frame time here)
      fundobranco1.frameNStart = frameN;  // exact frame index
      
      fundobranco1.setAutoDraw(true);
    }
    
    
    // *enter_tecla* updates
    if (t >= 0.0 && enter_tecla.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enter_tecla.tStart = t;  // (not accounting for frame time here)
      enter_tecla.frameNStart = frameN;  // exact frame index
      
      enter_tecla.setAutoDraw(true);
    }
    
    
    // *instruções2* updates
    if (t >= 0.0 && instruções2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruções2.tStart = t;  // (not accounting for frame time here)
      instruções2.frameNStart = frameN;  // exact frame index
      
      instruções2.setAutoDraw(true);
    }
    
    
    // *resposta2* updates
    if (t >= 0.0 && resposta2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resposta2.tStart = t;  // (not accounting for frame time here)
      resposta2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resposta2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resposta2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resposta2.clearEvents(); });
    }
    
    if (resposta2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resposta2.getKeys({keyList: ['return'], waitRelease: false});
      _resposta2_allKeys = _resposta2_allKeys.concat(theseKeys);
      if (_resposta2_allKeys.length > 0) {
        resposta2.keys = _resposta2_allKeys[_resposta2_allKeys.length - 1].name;  // just the last key pressed
        resposta2.rt = _resposta2_allKeys[_resposta2_allKeys.length - 1].rt;
        resposta2.duration = _resposta2_allKeys[_resposta2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *encher_balão* updates
    if (t >= 0.0 && encher_balão.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      encher_balão.tStart = t;  // (not accounting for frame time here)
      encher_balão.frameNStart = frameN;  // exact frame index
      
      encher_balão.setAutoDraw(true);
    }
    
    
    // *guardar_dinheiro* updates
    if (t >= 0.0 && guardar_dinheiro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      guardar_dinheiro.tStart = t;  // (not accounting for frame time here)
      guardar_dinheiro.frameNStart = frameN;  // exact frame index
      
      guardar_dinheiro.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructions_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_2' ---
    for (const thisComponent of instructions_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instructions_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resposta2.corr, level);
    }
    psychoJS.experiment.addData('resposta2.keys', resposta2.keys);
    if (typeof resposta2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resposta2.rt', resposta2.rt);
        psychoJS.experiment.addData('resposta2.duration', resposta2.duration);
        routineTimer.reset();
        }
    
    resposta2.stop();
    // the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'trialTypes_B1.xlsx',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(trial_2RoutineBegin(snapshot));
      trials_2LoopScheduler.add(trial_2RoutineEachFrame());
      trials_2LoopScheduler.add(trial_2RoutineEnd(snapshot));
      trials_2LoopScheduler.add(feedback_2RoutineBegin(snapshot));
      trials_2LoopScheduler.add(feedback_2RoutineEachFrame());
      trials_2LoopScheduler.add(feedback_2RoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function trial_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_2' ---
    t = 0;
    trial_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial_2.started', globalClock.getTime());
    fundobranco2.setImage('branco.jpeg');
    bankButton.keys = undefined;
    bankButton.rt = undefined;
    _bankButton_allKeys = [];
    balloonBody.setImage('redBalloon.png');
    molduraRM1.setImage('molduraRM1e2.png');
    molduraRM2.setImage('molduraRM1e2.png');
    molduraBVM.setImage('molduraBVM.png');
    molduraBM.setImage('Bau.png');
    // Run 'Begin Routine' code from setBalloonSize
    balloonSize = 0.08;
    popped = false;
    nPumps = 0;
    
    // keep track of which components have finished
    trial_2Components = [];
    trial_2Components.push(fundobranco2);
    trial_2Components.push(bankButton);
    trial_2Components.push(balloonBody);
    trial_2Components.push(molduraRM1);
    trial_2Components.push(molduraRM2);
    trial_2Components.push(molduraBVM);
    trial_2Components.push(molduraBM);
    trial_2Components.push(reminderMsg1);
    trial_2Components.push(reminderMsg2);
    trial_2Components.push(balloonValMsg);
    trial_2Components.push(bankedMsg);
    
    for (const thisComponent of trial_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function trial_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_2' ---
    // get current time
    t = trial_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fundobranco2* updates
    if (t >= 0.0 && fundobranco2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fundobranco2.tStart = t;  // (not accounting for frame time here)
      fundobranco2.frameNStart = frameN;  // exact frame index
      
      fundobranco2.setAutoDraw(true);
    }
    
    
    // *bankButton* updates
    if (t >= 0.0 && bankButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bankButton.tStart = t;  // (not accounting for frame time here)
      bankButton.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { bankButton.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { bankButton.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { bankButton.clearEvents(); });
    }
    
    if (bankButton.status === PsychoJS.Status.STARTED) {
      let theseKeys = bankButton.getKeys({keyList: ['return'], waitRelease: false});
      _bankButton_allKeys = _bankButton_allKeys.concat(theseKeys);
      if (_bankButton_allKeys.length > 0) {
        bankButton.keys = _bankButton_allKeys[_bankButton_allKeys.length - 1].name;  // just the last key pressed
        bankButton.rt = _bankButton_allKeys[_bankButton_allKeys.length - 1].rt;
        bankButton.duration = _bankButton_allKeys[_bankButton_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from updateEarnings
    thisBalloonEarnings = (nPumps * 0.05);
    
    
    if (balloonBody.status === PsychoJS.Status.STARTED){ // only update if being drawn
      balloonBody.setPos([0, ((- 0.35) + (balloonSize / 2))], false);
      balloonBody.setSize(balloonSize, false);
    }
    
    // *balloonBody* updates
    if (t >= 0.0 && balloonBody.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      balloonBody.tStart = t;  // (not accounting for frame time here)
      balloonBody.frameNStart = frameN;  // exact frame index
      
      balloonBody.setAutoDraw(true);
    }
    
    
    // *molduraRM1* updates
    if (t >= 0.0 && molduraRM1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      molduraRM1.tStart = t;  // (not accounting for frame time here)
      molduraRM1.frameNStart = frameN;  // exact frame index
      
      molduraRM1.setAutoDraw(true);
    }
    
    
    // *molduraRM2* updates
    if (t >= 0.0 && molduraRM2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      molduraRM2.tStart = t;  // (not accounting for frame time here)
      molduraRM2.frameNStart = frameN;  // exact frame index
      
      molduraRM2.setAutoDraw(true);
    }
    
    
    // *molduraBVM* updates
    if (t >= 0.0 && molduraBVM.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      molduraBVM.tStart = t;  // (not accounting for frame time here)
      molduraBVM.frameNStart = frameN;  // exact frame index
      
      molduraBVM.setAutoDraw(true);
    }
    
    
    // *molduraBM* updates
    if (t >= 0.0 && molduraBM.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      molduraBM.tStart = t;  // (not accounting for frame time here)
      molduraBM.frameNStart = frameN;  // exact frame index
      
      molduraBM.setAutoDraw(true);
    }
    
    
    // *reminderMsg1* updates
    if (t >= 0.0 && reminderMsg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminderMsg1.tStart = t;  // (not accounting for frame time here)
      reminderMsg1.frameNStart = frameN;  // exact frame index
      
      reminderMsg1.setAutoDraw(true);
    }
    
    
    // *reminderMsg2* updates
    if (t >= 0.0 && reminderMsg2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminderMsg2.tStart = t;  // (not accounting for frame time here)
      reminderMsg2.frameNStart = frameN;  // exact frame index
      
      reminderMsg2.setAutoDraw(true);
    }
    
    
    if (balloonValMsg.status === PsychoJS.Status.STARTED){ // only update if being drawn
      balloonValMsg.setText(f'''Valor deste balão:
      {round(thisBalloonEarnings, 2)}€''', false);
    }
    
    // *balloonValMsg* updates
    if (t >= 0.0 && balloonValMsg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      balloonValMsg.tStart = t;  // (not accounting for frame time here)
      balloonValMsg.frameNStart = frameN;  // exact frame index
      
      balloonValMsg.setAutoDraw(true);
    }
    
    
    if (bankedMsg.status === PsychoJS.Status.STARTED){ // only update if being drawn
      bankedMsg.setText(f'''Já ganhou:
      {round(bankedEarnings, 2)}€''', false);
    }
    
    // *bankedMsg* updates
    if (t >= 0.0 && bankedMsg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bankedMsg.tStart = t;  // (not accounting for frame time here)
      bankedMsg.frameNStart = frameN;  // exact frame index
      
      bankedMsg.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from checkKeys
    if (event.getKeys(["space"])) {
        nPumps = (nPumps + 1);
        if ((nPumps > maxPumps)) {
            popped = true;
            continueRoutine = false;
        }
    }
    
    // Run 'Each Frame' code from setBalloonSize
    balloonSize = (0.1 + (nPumps * 0.015));
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trial_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_2' ---
    for (const thisComponent of trial_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(bankButton.corr, level);
    }
    psychoJS.experiment.addData('bankButton.keys', bankButton.keys);
    if (typeof bankButton.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('bankButton.rt', bankButton.rt);
        psychoJS.experiment.addData('bankButton.duration', bankButton.duration);
        routineTimer.reset();
        }
    
    bankButton.stop();
    // Run 'End Routine' code from updateEarnings
    if (popped) {
        thisBalloonEarnings = 0.0;
        lastBalloonEarnings = 0.0;
    } else {
        lastBalloonEarnings = thisBalloonEarnings;
    }
    bankedEarnings = (bankedEarnings + lastBalloonEarnings);
    
    // Run 'End Routine' code from setBalloonSize
    trials.addData("nPumps", nPumps);
    trials.addData("size", balloonSize);
    trials.addData("earnings", thisBalloonEarnings);
    trials.addData("popped", popped);
    
    // the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function feedback_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_2' ---
    t = 0;
    feedback_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('feedback_2.started', globalClock.getTime());
    fundobranco3.setImage('branco.jpeg');
    // Run 'Begin Routine' code from checkPopped
    /* Syntax Error: Fix Python code */
    feedbackMsg22.setText(feedbackText);
    // keep track of which components have finished
    feedback_2Components = [];
    feedback_2Components.push(fundobranco3);
    feedback_2Components.push(feedbackMsg22);
    
    for (const thisComponent of feedback_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function feedback_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_2' ---
    // get current time
    t = feedback_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fundobranco3* updates
    if (t >= 0.0 && fundobranco3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fundobranco3.tStart = t;  // (not accounting for frame time here)
      fundobranco3.frameNStart = frameN;  // exact frame index
      
      fundobranco3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fundobranco3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fundobranco3.setAutoDraw(false);
    }
    
    // *feedbackMsg22* updates
    if (t >= 0.0 && feedbackMsg22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbackMsg22.tStart = t;  // (not accounting for frame time here)
      feedbackMsg22.frameNStart = frameN;  // exact frame index
      
      feedbackMsg22.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedbackMsg22.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbackMsg22.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedback_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_2' ---
    for (const thisComponent of feedback_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback_2.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function final_scoreRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'final_score' ---
    t = 0;
    final_scoreClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('final_score.started', globalClock.getTime());
    finalScore.setText(`Muito bem! Amealhou um total de ${util.round(bankedEarnings, 2)}€`);
    // keep track of which components have finished
    final_scoreComponents = [];
    final_scoreComponents.push(fundobranco4);
    final_scoreComponents.push(finalScore);
    
    for (const thisComponent of final_scoreComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function final_scoreRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'final_score' ---
    // get current time
    t = final_scoreClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fundobranco4* updates
    if (t >= 0.0 && fundobranco4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fundobranco4.tStart = t;  // (not accounting for frame time here)
      fundobranco4.frameNStart = frameN;  // exact frame index
      
      fundobranco4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fundobranco4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fundobranco4.setAutoDraw(false);
    }
    
    // *finalScore* updates
    if (t >= 0.0 && finalScore.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      finalScore.tStart = t;  // (not accounting for frame time here)
      finalScore.frameNStart = frameN;  // exact frame index
      
      finalScore.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (finalScore.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      finalScore.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of final_scoreComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function final_scoreRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'final_score' ---
    for (const thisComponent of final_scoreComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('final_score.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function farwellRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'farwell' ---
    t = 0;
    farwellClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(8.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('farwell.started', globalClock.getTime());
    // keep track of which components have finished
    farwellComponents = [];
    farwellComponents.push(_fundo_branco_final);
    farwellComponents.push(farwell);
    farwellComponents.push(smile_final);
    
    for (const thisComponent of farwellComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function farwellRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'farwell' ---
    // get current time
    t = farwellClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *_fundo_branco_final* updates
    if (t >= 0.0 && _fundo_branco_final.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      _fundo_branco_final.tStart = t;  // (not accounting for frame time here)
      _fundo_branco_final.frameNStart = frameN;  // exact frame index
      
      _fundo_branco_final.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (_fundo_branco_final.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      _fundo_branco_final.setAutoDraw(false);
    }
    
    // *farwell* updates
    if (t >= 0.0 && farwell.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      farwell.tStart = t;  // (not accounting for frame time here)
      farwell.frameNStart = frameN;  // exact frame index
      
      farwell.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (farwell.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      farwell.setAutoDraw(false);
    }
    
    // *smile_final* updates
    if (t >= 0.0 && smile_final.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      smile_final.tStart = t;  // (not accounting for frame time here)
      smile_final.frameNStart = frameN;  // exact frame index
      
      smile_final.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (smile_final.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      smile_final.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of farwellComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function farwellRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'farwell' ---
    for (const thisComponent of farwellComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('farwell.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
