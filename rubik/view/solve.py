from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import *
import re
import hashlib
import random

def _getIntegrity(cubeString, solutionString):
    author = "wgr0009"
    itemToTokenize = cubeString + solutionString + author
    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    start = random.randint(0, len(fullToken) - 8)
    return str(fullToken)[start:(start + 8)]

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    result['status'] = 'error: invalid cube' 
    encodedCube = parms.get('cube')
    
    try:
        theCube = Cube(encodedCube)
    except CubeError:
        return result
    
    if re.match("(([a-zA-Z0-9])\2{8}){6}", encodedCube) != None:
        result['solution'] = ''
        result['status'] = 'ok'    
        result['integrity'] = ''
        return result
    
    rotations = ""
    try:
        rotations += solveBottomCross(theCube)      #iteration 2
        rotations += solveBottomLayer(theCube)      #iteration 3
        rotations += solveMiddleLayer(theCube)      #iteration 4
        rotations += solveUpCross(theCube)          #iteration 5
        rotations += solveUpSurface(theCube)        #iteration 5
        rotations += solveUpperLayer(theCube)       #iteration 6
        
        result['solution'] = rotations
        result['status'] = 'ok'    
        result['integrity'] = _getIntegrity(encodedCube, rotations)
    except SolveError:
        result['status'] = 'error: no solution found'    
        result['integrity'] = ''
                     
    return result
