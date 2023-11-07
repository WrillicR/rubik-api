from rubik.model.constants import *
from rubik.model.cube import *
from rubik.controller.bottomLayer import solveBottomLayer

def _checkMiddleLayer(theCube):
    indexArray = [DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, FMM, FMM, FMM, RMM, RMM, RMM, BMM, BMM, BMM, LMM, LMM, LMM, FMM, FMM, RMM, RMM, BMM, BMM, LMM, LMM]
    valueArray = [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR, FBL, FBM, FBR, RBL, RBM, RBR, BBL, BBM, BBR, LBL, LBM, LBR, FMR, FML, RMR, RML, BMR, BML, LMR, LML] 
    booleArray = [theCube.get()[valueArray[x]] == theCube.get()[indexArray[x]] for x in range(len(indexArray))]
    return all(booleArray)

def _getAdjSquare(index):
    adjSquare = ""
    if index == UBM:
        adjSquare = FTM
    elif index == UMR:
        adjSquare = RTM
    elif index == UTM:
        adjSquare = BTM
    elif index == UML:
        adjSquare = LTM
    return adjSquare

def _isMiddleSquare(theCube, index):
    petal = theCube.get()[UMM]
    if theCube.get()[index] == petal:
        return False
    adjSquare = theCube.get()[_getAdjSquare(index)]
    if adjSquare == petal:
        return False
    return True

def _getAlignmentRotations(theCube, toFace, index):
    rotations = ""
    fromFace = theCube.getFaceFromIndex(index)
    numRotations = ADJ_MAP.index(toFace) - ADJ_MAP.index(fromFace)
    for _ in range(abs(numRotations)):
        if numRotations < 0:
            rotations += "U"
        else:
            rotations += "u"
    if rotations == "uuu":
        rotations = "U"
    elif rotations == "UUU":
        rotations = "u"
    return rotations

def _swapCase(string):
    if string.isupper():
        return string.lower()
    else:
        return string.upper()

def _getTriggerString(face, direction):
    trigger = ""
    upDir= "U"
    if direction == CCW:
        face = face.lower()
        upDir = upDir.lower()
    trigger += face
    trigger += upDir
    trigger += _swapCase(face)
    return trigger

def _getTriggerPlus(theCube, index):
    # get top square's target face
    toFace = theCube.getFaceFromColor(theCube.get()[index])
    triggerFaceIndex = ADJ_MAP.index(toFace) + 2
    triggerFaceIndex %= len(ADJ_MAP)
    triggerFace = ADJ_MAP[triggerFaceIndex]
    # rotate upper accordingly
    alignments = _getAlignmentRotations(theCube, triggerFace, _getAdjSquare(index))
    rotations = alignments
    # trigger face accordingly
    rotations += _getTriggerString(toFace, rotations.isupper())
    return rotations


    # look for top layer middle cubes that don't have yellow on itself or adjacent
        # rotate top to align to side face
        # rotate top corresponding to top color [left -> left]
        # trigger
        # solve bottom
    # if no top layer middle cubes & still not solved...
        # trigger according to the side it's facing
        
def _handleMiddle(theCube):
    sequence = ""
    topSolved = False
    targetSquares = PETAL_SLOTS
    for targetSquareIndex in range(len(targetSquares)):
        targetSquare = targetSquares[targetSquareIndex]
        if _isMiddleSquare(theCube, targetSquare):
            toFace = theCube.getFaceFromColor(theCube.get()[_getAdjSquare(targetSquare)])
            rotations = _getAlignmentRotations(theCube, toFace, _getAdjSquare(targetSquare))
            targetSquareIndex = targetSquareIndex + len(rotations) * pow(-1, rotations.isupper()) + len(targetSquares)
            targetSquareIndex = targetSquareIndex % len(targetSquares)
            targetSquare = targetSquares[targetSquareIndex]
            theCube.rotate(rotations) # update the cube
            sequence += rotations
            rotations = _getTriggerPlus(theCube, targetSquare)
            theCube.rotate(rotations) # update the cube
            sequence += rotations
            topSolved = False
            break
        topSolved = True
    if topSolved:
        targetSquares = LEFT_MID_SLOTS
        for targetSquare in targetSquares:
            if theCube.get()[targetSquare] != theCube.get()[targetSquare + 1]: # mismatch
                triggerFace = theCube.getFaceFromIndex((targetSquare - NUM_SQUARES_PER_FACE + NUM_ADJACENT_SQUARES) % NUM_ADJACENT_SQUARES)
                rotations = _getTriggerString(triggerFace, False)
                theCube.rotate(rotations) # update the cube
                sequence += rotations
                break
    return sequence

'''
    This is the top-level function  for rotating
    a cube so that the middle layer is solved.
    
    input:  an instance of the cube class with the bottom layer solved
    output: the rotations required to solve the middle layer  
'''  


def solveMiddleLayer(theCube: Cube) -> str:
    sequence = ""
    loopCount = 0
    while not(_checkMiddleLayer(theCube)):
        loopCount += 1
        if loopCount > MAX_WHILE_LOOPS:
            raise SolveError
        rotations = solveBottomLayer(theCube)
        sequence += rotations
        sequence += _handleMiddle(theCube)
    return sequence
