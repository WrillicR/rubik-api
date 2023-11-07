from rubik.model.constants import *
from rubik.model.cube import Cube, SolveError

def _checkUpCross(theCube):
    valueArray = [DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, FMM, FMM, FMM, RMM, RMM, RMM, BMM, BMM, BMM, LMM, LMM, LMM, FMM, FMM, RMM, RMM, BMM, BMM, LMM, LMM, UMM, UMM, UMM, UMM]
    indexArray = [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR, FBL, FBM, FBR, RBL, RBM, RBR, BBL, BBM, BBR, LBL, LBM, LBR, FMR, FML, RMR, RML, BMR, BML, LMR, LML, UTM, UML, UMR, UBM] 
    booleArray = [theCube.get()[valueArray[x]] == theCube.get()[indexArray[x]] for x in range(len(indexArray))]
    return all(booleArray)

def _handleCross(theCube):
    rotations = ""
    petal = theCube.get()[UMM]
    petalSlots = [UTM, UML, UBM, UMR]
    for slotIndex in range(len(petalSlots)):
        if (theCube.get()[petalSlots[slotIndex]] == petal and theCube.get()[petalSlots[((slotIndex+1) % len(petalSlots))]] == petal):
            for _ in range(slotIndex):
                rotations += "U" 
            break
        if (theCube.get()[UML] == petal and theCube.get()[UMR] == petal):
            rotations += "U"
            break
    rotations += "FURurf"
    theCube.rotate(rotations)
    return rotations

'''
    This is the top-level function  for rotating
    a cube into the up-face cross configuration.
    
    input:  an instance of the cube class with the middle layer solved
    output: the rotations required to solve the up-face cross
    
    # NO YELLOWS -> do front
    # VERTICAL YELLOWS -> do front
    # 9:00 & 12:00 -> do front
      
'''

def solveUpCross(theCube: Cube) -> str:
    solution = ""
    loopCount = 0
    while(not(_checkUpCross(theCube))):
        loopCount += 1
        if loopCount > MAX_WHILE_LOOPS:
            raise SolveError
        solution += _handleCross(theCube)
    return solution
