from rubik.model.constants import *
from rubik.model.cube import Cube, SolveError

def _checkUpSurface(theCube):
    valueArray = [DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, FMM, FMM, FMM, RMM, RMM, RMM, BMM, BMM, BMM, LMM, LMM, LMM, FMM, FMM, RMM, RMM, BMM, BMM, LMM, LMM, UMM, UMM, UMM, UMM, UMM, UMM, UMM, UMM]
    indexArray = [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR, FBL, FBM, FBR, RBL, RBM, RBR, BBL, BBM, BBR, LBL, LBM, LBR, FMR, FML, RMR, RML, BMR, BML, LMR, LML, UTM, UML, UMR, UBM, UTL, UTR, UBL, UBR] 
    booleArray = [theCube.get()[valueArray[x]] == theCube.get()[indexArray[x]] for x in range(len(indexArray))]
    return all(booleArray)

def _handleUpSurface(theCube):
    rotations = ""
    petal = theCube.get()[UMM]
    cornerSlots = [UBL, UBR, UTR, UTR]
    sideSlots = [LTR, FTR, RTR, BTR]
    emptySlots = []
    for cornerIndex in range(len(cornerSlots)):
        if theCube.get()[cornerSlots[cornerIndex]] == petal:
            emptySlots.append(cornerIndex)
    if len(emptySlots) == 1:
        for _ in range(emptySlots[0]):
            rotations += "U"
    else:
        for sideIndex in range(len(sideSlots)):
            if theCube.get()[sideSlots[sideIndex]] == petal:
                for _ in range(sideIndex):
                    rotations += "U"
                break
    rotations += "RUrURUUr"
    theCube.rotate(rotations)
    return rotations

'''
    This is the top-level function  for rotating
    a cube so that the up face is solved.
    
    input:  an instance of the cube class with up-face cross solved
    output: the rotations required to solve the up surface  
'''  

def solveUpSurface(theCube: Cube) -> str:
    solution = ""
    loopCount = 0
    while(not(_checkUpSurface(theCube))):
        loopCount += 1
        if loopCount > MAX_WHILE_LOOPS:
            raise SolveError
        solution += _handleUpSurface(theCube)
    return solution
