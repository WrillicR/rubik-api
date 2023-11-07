from rubik.model.constants import *
from rubik.model.cube import *

def _checkUpperLayer(theCube):
    valueArray = [DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, FMM, FMM, FMM, RMM, RMM, RMM, BMM, BMM, BMM, LMM, LMM, LMM, FMM, FMM, RMM, RMM, BMM, BMM, LMM, LMM, UMM, UMM, UMM, UMM, UMM, UMM, UMM, UMM, FMM, FMM, FMM, RMM, RMM, RMM, BMM, BMM, BMM, LMM, LMM, LMM]
    indexArray = [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR, FBL, FBM, FBR, RBL, RBM, RBR, BBL, BBM, BBR, LBL, LBM, LBR, FMR, FML, RMR, RML, BMR, BML, LMR, LML, UTM, UML, UMR, UBM, UTL, UTR, UBL, UBR, FTL, FTM, FTR, RTL, RTM, RTR, BTL, BTM, BTR, LTL, LTM, LTR] 
    booleArray = [theCube.get()[valueArray[x]] == theCube.get()[indexArray[x]] for x in range(len(indexArray))]
    return all(booleArray)

def _getCornerMismatches(theCube):
    mismatches = 0
    for face in range(NUM_ADJACENT_FACES):
        faceIndex = face * NUM_SQUARES_PER_FACE
        if theCube.get()[faceIndex + XTL] != theCube.get()[faceIndex + XTR]:
            mismatches += 1
    return mismatches

def _getCenterMismatches(theCube):
    mismatches = 0
    for face in range(NUM_ADJACENT_FACES):
        faceIndex = face * NUM_SQUARES_PER_FACE
        if theCube.get()[faceIndex + XTM] != theCube.get()[faceIndex + XTR]:
            mismatches += 1
    return mismatches

def _getIdealCornerRotation(theCube):
    minMismatches = 4
    minRotation = 0
    for rotationIndex in range(NUM_ADJACENT_FACES):
        mismatches = 4
        for faceIndex in range(NUM_ADJACENT_FACES):
            matchIndex = faceIndex * NUM_SQUARES_PER_FACE + XMM # center square in respective side
            cornerIndex = faceIndex * NUM_SQUARES_PER_FACE + XTR # corner square in respective side
            if theCube.get()[matchIndex] == theCube.get()[cornerIndex]:
                mismatches -= 1
        if mismatches < minMismatches:
            minMismatches = mismatches
            minRotation = rotationIndex
        theCube.rotate("u") # this is always performed 4x, so we don't need to track it
    return [minRotation, minMismatches]

def _handleCorners(theCube):
    rotations = ""
    while _getCornerMismatches(theCube) > 0:
        for _ in range(NUM_ADJACENT_FACES):
            if theCube.get()[LTL] == theCube.get()[LTR]:
                break
            rotations += "U"
            theCube.rotate("U")
        rotations += "lURuLUrRUrURUUr"
        theCube.rotate("lURuLUrRUrURUUr")
    return rotations

def _handleCenters(theCube):
    rotations = ""
    while _getCenterMismatches(theCube) > 0:
        for _ in range(NUM_ADJACENT_FACES):
            if theCube.get()[BTM] == theCube.get()[BTR]:
                break
            rotations += "u"
            theCube.rotate("u")
        rotations += "FFULrFFlRUFF"
        theCube.rotate("FFULrFFlRUFF")
    for _ in range(NUM_ADJACENT_FACES):
        if theCube.get()[BMM] == theCube.get()[BTM]:
            break
        rotations += "u"
        theCube.rotate("u")
    return rotations

'''
    This is the top-level function  for rotating
    a cube so that the entire upper layer is solved.
    
    input:  an instance of the cube class with up-face surface solved
    output: the rotations required to solve the upper layer  
'''

def solveUpperLayer(theCube: Cube) -> str:
    sequence = ""
    rotations = ""
    cornerRotations = _handleCorners(theCube)
    sequence += cornerRotations
    idealRot = _getIdealCornerRotation(theCube)
    for _ in range(idealRot[0]):
        rotations += "u"
    theCube.rotate(rotations)
    sequence += rotations
    
    centerRotations = _handleCenters(theCube)
    sequence += centerRotations
    
    if not(_checkUpperLayer(theCube)):
        raise SolveError
    return sequence
