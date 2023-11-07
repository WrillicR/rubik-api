from rubik.model.cube import Cube
from rubik.model.cube import DirectionError
from rubik.model.cube import CubeError
from rubik.model.constants import *

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    result['status'] = 'error: invalid cube' 
    
    encodedCube = parms.get('cube')
    
    try:
        theCube = Cube(encodedCube)
    except CubeError:
        return result
    
    directions = parms.get('dir')
    
    if directions is None or len(directions) == 0:
            directions = "F"
        
    ## check for extra passed parameters
    keys = list(parms.keys())
    for key in keys:
        if key != "dir" and key !="cube":
            return result
    
    try:
        theCube.rotate(directions)
        result['cube'] = theCube.get()
        result['status'] = 'ok'
    except DirectionError:
        result['status'] = 'error: invalid rotation' 
    
    return result