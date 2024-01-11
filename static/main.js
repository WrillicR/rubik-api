// https://jsfiddle.net/WrillicR/Lacsjh3p/182/
import * as THREE from "three";
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import * as TWEEN from "tween";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 7, window.innerWidth / window.innerHeight, 0.1, 500 );
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, });
renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );
const controls = new OrbitControls( camera, renderer.domElement );

controls.minDistance = 50;
controls.maxDistance = 200;
controls.enablePan = false;
controls.enableDamping = true;
controls.dampingFactor = 0.2;
camera.position.x = 50;
camera.position.y = 50;
camera.position.z = 75;
document.body.style.backgroundColor = "#010a0d";
scene.background = new THREE.Color( 0x010a0d );

var darkMode = true;

var cubes = [];
const colorCodes = [0xcc2200, 0xee6600, 0xffdd00, 0xffffff, 0x1144cc, 0x008844];
var colors = toThreeColors(colorCodes);
const FACEARR = ["F","R","L","U","B","f","r","l","u","b"];
const FACEMAP = {
"F" : [new THREE.Vector3(0, 0, -1), 2, 1],
"f" : [new THREE.Vector3(0, 0, 1), 2, 1],
"R" : [new THREE.Vector3(-1, 0, 0), 0, 1],
"r" : [new THREE.Vector3(1, 0, 0), 0, 1],
"L" : [new THREE.Vector3(1, 0, 0), 0, -1],
"l" : [new THREE.Vector3(-1, 0, 0), 0, -1],
"U" : [new THREE.Vector3(0, -1, 0), 1, 1],
"u" : [new THREE.Vector3(0, 1, 0), 1, 1],
"B" : [new THREE.Vector3(0, 0, 1), 2, -1],
"b" : [new THREE.Vector3(0, 0, -1), 2, -1]
};
var cubeQueue = [];
const CubeState = Object.freeze({
  ROTATING: 0,
  STOP: 3,
  CALC: 1,
  SOLVING: 4,
  RESET: 2
});
const DIVISIONS = [300,160,110,90,70,50,37,32,25,19,16,14,10,9,8,7,5,4,3,2,1];
const MAXANGLE = Math.PI / 2; // 90 degrees
const SPEED = 7;
const SOLVE_SPEED = 10;
const SINGLE_SPEED = 11;
const CENTER = new THREE.Vector3(0, 0, 0);
const doughnut = new THREE.Mesh(
  new THREE.TorusGeometry(3,0.05,16,64,0),
  new THREE.MeshBasicMaterial());

let pastTurns = "";
let futureTurns = [];
let interval = calcInterval(SPEED);
var currentFace = "";
var currentAngle = MAXANGLE;
var TIMEOUTMAX = 2;
var timeout = 0;
let arc = {x: 0.0};
let donutSpeed = 0.24;
var lastTween = new TWEEN.Tween();
var arcTweenClose = new TWEEN.Tween(arc)
    .to( { x:0}, 800)
    .easing(TWEEN.Easing.Quadratic.Out);
var arcTweenOpen = new TWEEN.Tween(arc)
    .to( { x:Math.PI * 3/2}, 1000)
    .onComplete(() => {
    	donutSpeed *= 2;
    	arcTweenClose.start();
    })
    .easing(TWEEN.Easing.Quadratic.In);

function init() {

  for (var i = 0; i < 27; i++) {
    var x = (i % 3) - 1;
    var y = Math.floor((i / 9) - 1);
    var z = Math.floor((i % 9) / 3) - 1;
    const geometry = new THREE.BoxGeometry( 0.9,0.9,0.9 ).toNonIndexed();
    geometry.setAttribute( 'color', new THREE.Float32BufferAttribute( colors, 3 ) );
    var cubeMaterial = new THREE.MeshBasicMaterial( { vertexColors: true } );
    cubeMaterial.transparent = true;
    const cube = new THREE.Mesh( geometry, cubeMaterial);
    cube.position.x = x;
    cube.position.y = y;
    cube.position.z = z;
    scene.add( cube );
    cubes.push( cube );
  }
  scene.add(doughnut);
  doughnut.rotation.x = Math.PI / 2;
  doughnut.visible = false;
  currentAngle = MAXANGLE;
  interval = calcInterval(SPEED);
  timeout = TIMEOUTMAX;
  pastTurns = "";
  currentFace = "";
  futureTurns = [];
  colorMatch();
  floatUp();
  console.log("Initializing...");
}

init();

function animate() {

  if (cubeQueue.length > 2) cubeQueue = [cubeQueue[0], cubeQueue[1]]; // keep the queue to two items
  doughnut.rotation.z += donutSpeed;
	doughnut.geometry.dispose(); 
	doughnut.geometry = new THREE.TorusGeometry(3,0.05,16,64, arc.x );
	if (!lastTween._isPlaying) {
    if (cubeQueue[0] == CubeState.RESET) {
      handleReset();
    } else if (cubeQueue[0] == CubeState.STOP) {
      cubeQueue.shift();
    } else if (cubeQueue[0] == CubeState.ROTATING || cubeQueue[0] == CubeState.SOLVING) {
      if (currentAngle < MAXANGLE) {
        currentAngle += interval;
        if (currentAngle > MAXANGLE) currentAngle = MAXANGLE;
        rotateFace(currentFace, interval);
      } else if (gateKeep()) {
          pastTurns += currentFace;
          if (cubeQueue[0] == CubeState.SOLVING) pastTurns = "";
          if (cubeQueue.length > 1) cubeQueue.shift();
          if (cubeQueue[0] == CubeState.CALC) initSolve();
          postRotation();
          handleNextFace();
      }
    } else if (cubeQueue[0] == CubeState.CALC) {
      if (!arcTweenOpen._isPlaying) {
        if (cubeQueue[1] == CubeState.STOP) {
          cubeQueue.shift();
        } else {
          if (futureTurns.length > 0) {
            interval = calcInterval(SOLVE_SPEED);
            cubeQueue = [CubeState.SOLVING];
            handleNextFace();
          } else {
            doughnut.visible = true;
            donutSpeed /= 2;
            arcTweenOpen.start();
            sweepDarken();
          }
        }
      }
    }
  }

	TWEEN.update();
  controls.update();
	renderer.render( scene, camera );
	requestAnimationFrame( animate );

}

animate();

window.onresize = function () {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize( window.innerWidth, window.innerHeight );
};

document.body.onkeyup = function(e) {
  if (e.key == " ") {
    initShuffle();
  } else if (e.keyCode == 13 && !lastTween._isPlaying) {
  	initCalc();
  } else if (e.keyCode == 27) {
    cubeQueue.push(CubeState.RESET);
  } else if (FACEARR.indexOf(e.key) != -1) {
    handleKeyControls(e.key);
  } else if (e.keyCode == 190) {
    setTheme();
  }
}

document.getElementById("shuffle").onclick = function() {initShuffle()};
document.getElementById("solve").onclick = function() {initCalc()};

/* HANDLING METHODS */

function setTheme(dark) {
  if (dark !== undefined) darkMode = dark;
  else darkMode = !darkMode;
  if (darkMode) {
    scene.background = new THREE.Color( 0x010a0d );
    doughnut.material.color.setRGB(1,1,1);
  } else {
    scene.background = new THREE.Color( 1,1,1 );
    doughnut.material.color.setRGB(1,10,13);
  }
  
}

function handleReset() {
  cubes = [];
  cubeQueue = [];
  scene.clear();
  init();
}

function handleKeyControls(key) {
  if (cubeQueue.length == 0) {
    currentAngle = 0;
    interval = calcInterval(SINGLE_SPEED);
    cubeQueue.push(CubeState.ROTATING);
    handleNextFace(key);
  } else if (cubeQueue[0] == CubeState.ROTATING && futureTurns.length < 3) {
    futureTurns.push(key);
    cubeQueue[1] = CubeState.ROTATING;
  }
}

function initShuffle() {
  if (cubeQueue[0] == CubeState.ROTATING)
    cubeQueue.push(CubeState.STOP);
  else
	  cubeQueue.push(CubeState.ROTATING);
  timeout = 0; 
}

function initCalc() {
  if (cubeQueue[0] != CubeState.SOLVING && futureTurns.length == 0) {
    cubeQueue.push(CubeState.CALC);
    if (cubeQueue[0] == CubeState.CALC) initSolve();
  } else if (cubeQueue.length == 0) {
    cubeQueue.push(CubeState.SOLVING);
  } else {
    cubeQueue.push(CubeState.STOP);
  }
}

function initSolve() {
  console.log("Solving initiatied...");
  futureTurns = [];
  cubeQueue.push(CubeState.CALC);
  console.log("Past turns:\t" + pastTurns);
  fetch('/rubik/rotate?cube=bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww&dir=' + pastTurns, {
    method: 'GET'
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      return response.text();
  })
  .then(data => {
      data = JSON.parse(data.replace(/'/g, '"'));
      //console.log(data.cube);
      fetch('/rubik/solve?cube=' + data["cube"], {
        method: 'GET'
      })
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          return response.text();
      })
      .then(data => {
          data = JSON.parse(data.replace(/'/g, '"'));
          console.log("Solution:\t" + data.solution);
          console.log("Removed " + (data.solution.length - removeCharPairs(data.solution).length) + " unnecessary rotations");
          console.log("Improved Solution:\t" + removeCharPairs(data.solution));
          pastTurns = "";
          futureTurns = removeCharPairs(data.solution).split('');
          if (futureTurns.length == 0 || futureTurns == "") cubeQueue = [CubeState.STOP];
      })
      .catch(error => {
          console.error('Error:', error);
      });
  })
  .catch(error => {
      console.error('Error:', error);
  });
}

function handleNextFace(nextFace) {
  if (nextFace !== undefined) futureTurns.push(nextFace);
  if (futureTurns.length > 0) {
    currentFace = futureTurns[0];
    futureTurns.shift();
    if (futureTurns.length == 0) cubeQueue.push(CubeState.STOP);
    return currentFace;
  } else {
    let tempFace = currentFace;
    do {
      currentFace = FACEARR[Math.floor(Math.random() * FACEARR.length)];
    } while (tempFace == invertCase(currentFace))
    interval = calcInterval(SPEED);
    return currentFace;
   }
}

/* ROTATION METHODS */

function postRotation() {
  currentAngle = 0;
	for (var i = 0; i < cubes.length; i++) {
  	cubes[i].position.round();
    var roundRot = new THREE.Vector3(cubes[i].rotation.x,cubes[i].rotation.y,cubes[i].rotation.z);
    roundRot.normalize();
    roundRot.multiplyScalar(MAXANGLE);
  }
}

function rotateFace(face, angle) {
  let dirVector = FACEMAP[face][0];
	for (var i = 0; i < cubes.length; i++) {
  	let cubeAxes = cubes[i].position.toArray();
    let axis = cubeAxes[FACEMAP[face][1]];
  	if (axis == FACEMAP[face][2]) {
    	//cubes[i].rotation.x = angle;
      //console.log(THREE.Math.degToRad(MAXANGLE / DIVISIONS));
      rotateAboutPoint(cubes[i], dirVector, dirVector, angle);
    }
  }
}

function rotateAboutPoint(obj, point, axis, theta){
		obj.position.sub(point); // remove the offset
    obj.position.applyAxisAngle(axis, theta); // rotate the POSITION
    obj.position.add(point); // re-add the offset
    obj.rotateOnWorldAxis(axis, theta);
}

/* UTILITY METHODS */

function calcInterval(speed) {
  return MAXANGLE / DIVISIONS[speed];
}

function gateKeep() {
	if (timeout > 0) {
  	timeout -= 1;
  	return false;
  } else {
  	timeout = TIMEOUTMAX;
    return true;
  }
}

const lettersToRemove = ['Ff', 'Uu', 'Rr', 'Ll', 'Bb'];
function removeCharPairs(inputString) {
  let modifiedString = inputString;

  for (const letterPair of lettersToRemove) {
    const regex = new RegExp(`(${letterPair}|${letterPair[1]}${letterPair[0]})`, 'g');
    modifiedString = modifiedString.replace(regex, '');
  }

  modifiedString = modifiedString.replace(/(.)\1{3}/g, '');

  modifiedString = modifiedString.replace(/(.)\1{2}/g, (match, char) => {
    // Invert the case of the matched character
    const invertedChar = invertCase(char);
    return invertedChar;
  });

  if (modifiedString !== inputString) {
    return removeCharPairs(modifiedString);
  } else {
    return modifiedString;
  }
}

function invertCase(char) {
  return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
}

/* ANIMATION METHODS */

function sweepDarken() {
	for (var i = cubes.length-1; i >= 0; i--) {
  	lastTween = new TWEEN.Tween(cubes[i].material)
    .to( { opacity:0.2}, 300)
    .yoyo(true)
    .repeat(1)
    .easing(TWEEN.Easing.Cubic.Out);
    lastTween.delay((cubes.length-i)*24);
    lastTween.start();
  }
}

function floatUp() {
  for (var i = 0; i < cubes.length; i++) {
    cubes[i].position.y -= 1;
    cubes[i].material.opacity = 0;
    let currentTween = new TWEEN.Tween(cubes[i].position)
      .to( { y:cubes[i].position.y+1}, 1000)
      .easing(TWEEN.Easing.Cubic.InOut);  
    currentTween.start((cubes.length - i)*30+260);
    new TWEEN.Tween(cubes[i].material)
      .to( { opacity:1}, 400)
      .easing(TWEEN.Easing.Cubic.InOut)
      .start((cubes.length - i)*30 + 660);
      if (i == 0) lastTween = currentTween;
  }
}

/* INITALIZATION METHODS */

function colorMatch() {
	for (var i = 0; i < 3; i++) {
    for (var j = 0; j < 3; j++) {
      for (var k = 0; k < 3; k++) {
				var newColors = Array.from(colorCodes);
        if (k <= 1) newColors[0] = new THREE.Color(0x010a0d);
        if (k >= 1) newColors[1] = new THREE.Color(0x010a0d);
        if (j <= 1) newColors[4] = new THREE.Color(0x010a0d);
        if (j >= 1) newColors[5] = new THREE.Color(0x010a0d);
        if (i <= 1) newColors[2] = new THREE.Color(0x010a0d);
        if (i >= 1) newColors[3] = new THREE.Color(0x010a0d);
        newColors = toThreeColors(newColors);
        cubes[9*i + 3*j + k].geometry.setAttribute( 'color', new THREE.Float32BufferAttribute( newColors, 3 ) );
      }

    }
  
  }
}

function toThreeColors(colorArr) {
	var colors = [];
  var color = new THREE.Color();
  	for ( let i = 0; i < colorArr.length; i += 1 ) {
      color.set( colorArr[i] );
      colors.push( color.r, color.g, color.b );
      colors.push( color.r, color.g, color.b );
      colors.push( color.r, color.g, color.b );
      colors.push(color.r, color.g, color.b);
      colors.push(color.r, color.g, color.b);
      colors.push(color.r, color.g, color.b);
    }
  return colors;
}


/*

Cube Object

RESET (instant)
  > none
STOP
  > init SHUFFLE or CALC or RESET or TURN
CALC
  > init SOLVE or RESET
ROTATE
  SOLVE
    > init STOP or RESET or RESET
  SHUFFLE
    > init STOP or CALC or RESET
  TURN
    > init SHUFFLE or CALC

Cube.doNext()
  queue.shift()

Cube.setNext(action)
  if action == RESET
    queue = RESET
  if Cube.getState() != CALC
    queue.
    elif action == CALC
      queue.push(CALC)
    elif action == STOP
      queue.push == STOP ???
  if Cube.getState() == STOP
    Cube.doNext()

Cube.getState()
  return queue[0]

Cube.trackTurn(turn)
  pastTurns += turn

Cube.resetTracking()

Cube.setTurn()

Cube.getTurn()

animate()
  state = Cube.getState()
  if state == RESET
    doReset() // everything, include Cube object, is reset
  elif state == CALC
    // it should calculate three times MAX
    if doCalc() // returns true IF animation done and SOLVE or STOP next in queue
      Cube.doNext()
  elif state == SOLVE or SHUFFLE or TURN
    rotation = Cube.getTurn()
    doRotate(rotation, face)
    if state != SOLVE
      Cube.trackTurn(rotation)



// when the cube is idle, i can do anything to it
// reseting at any point will immediately reset the cube
// when rotating, i can always STOP/resume, but the cube will finish its rotation before so
  // when shuffling, i can do anything
  // when turning, i can do anything
  // when solving, i cannot calculate the next solution
// when calculating, i cannot do anything
*/