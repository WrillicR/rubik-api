from rubik.model.constants import *
from rubik.model.cube import *

'''
# TODO: make getPetal() a method in Cube 
eventually add optimizations
'''

def _isSolved(theCube):
    indexArray = [DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, DMM, FMM, FMM, FMM, RMM, RMM, RMM, BMM, BMM, BMM, LMM, LMM, LMM]
    valueArray = [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR, FBL, FBM, FBR, RBL, RBM, RBR, BBL, BBM, BBR, LBL, LBM, LBR] 
    booleArray = [theCube.get()[valueArray[x]] == theCube.get()[indexArray[x]] for x in range(len(indexArray))]
    return all(booleArray)

def _getTopRowPetals(theCube, petal): # assumes all petals are in place
    topRow = []
    for faceIndex in range(NUM_ADJACENT_FACES):
        for squareIndex in range(NUM_SQUARES_PER_ROW):
            topIndex = faceIndex * NUM_SQUARES_PER_FACE + squareIndex
            if theCube.get()[topIndex] == petal:
                topRow.append(topIndex)
    return topRow

def _getBottomRowPetals(theCube, petal): # assumes all petals are in place
    bottomRow = []
    for faceIndex in range(NUM_ADJACENT_FACES):
        for squareIndex in range(NUM_SQUARES_PER_ROW):
            bottomIndex = faceIndex * NUM_SQUARES_PER_FACE + squareIndex + XBL
            if theCube.get()[bottomIndex] == petal:
                bottomRow.append(bottomIndex)
    return bottomRow

def _getUpFacePetals(theCube, petal): # assumes all petals are in place
    upFace = []
    for squareIndex in range(NUM_SQUARES_PER_FACE):
        upIndex = squareIndex + UTL
        if theCube.get()[upIndex] == petal:
            upFace.append(upIndex)
    return upFace

def _swapCase(string):
    if string.isupper():
        return string.lower()
    else:
        return string.upper()

def _isRightSide(index):
    relativeIndex = index % NUM_SQUARES_PER_FACE
    if relativeIndex == XTR or relativeIndex == XBR:
        return True
    return False

def _getAdjacentSquare(index):
    adjIndex = (index - SQUARES_TO_ADJACENT) % NUM_ADJACENT_SQUARES
    if _isRightSide(index):
        adjIndex = (index + SQUARES_TO_ADJACENT) % NUM_ADJACENT_SQUARES
    return adjIndex

def _getAlignmentRotations(theCube, index):
    rotations = ""
    adjIndex = _getAdjacentSquare(index)
    color = theCube.get()[adjIndex]
    toFace = theCube.getFaceFromColor(color)
    fromFace = theCube.getFaceFromIndex(adjIndex)
    numRotations = ADJ_MAP.index(toFace) - ADJ_MAP.index(fromFace)
    for _ in range(abs(numRotations)):
        if numRotations < 0:
            rotations += "U"
        else:
            rotations += "u"
    return rotations

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

def getTrigger(theCube, index):
    direction = CW
    face = theCube.getFaceFromIndex(index)
    
    relativeIndex = index % NUM_SQUARES_PER_FACE
    if (relativeIndex) + UTL in PETAL_SLOTS or relativeIndex == MIDDLE_SQUARE_INDEX or face == "D": # middle, petal, or down-face slots
        return ""
    elif face == "U":
        squareMap = [0,2,8,6]
        faceMap = ["B","R","F","L"]
        face = faceMap[squareMap.index(relativeIndex)]
        direction = CCW
        return _getTriggerString(face, direction)
      
    if _isRightSide(index): # on right side
        direction = not(direction)
    
    if relativeIndex in range(FBL,FBR+1): # on bottom row
        direction = not(direction)
        adjDirection = (2) * direction - 1
        face = ADJ_MAP[ (ADJ_MAP.index(face) + adjDirection ) % NUM_ADJACENT_FACES ]
    
    return _getTriggerString(face, direction)



def _handleTopRow(theCube, topRowPetals):
    sequence = ""
    index = topRowPetals[0]
    # get rotations until lined up
    rotations = _getAlignmentRotations(theCube, index)
    theCube.rotate(rotations)
    sequence += rotations
    # rotate getTrigger newIndex
    index = index + NUM_SQUARES_PER_FACE * len(rotations) * pow(-1, rotations.isupper()) + NUM_ADJACENT_SQUARES
    index = index % NUM_ADJACENT_SQUARES
    trigger = getTrigger(theCube, index)
    
    theCube.rotate(trigger)
    sequence += trigger
    return sequence
    
def _handleUpFace(theCube, upFacePetals):
    sequence = ""
    index = upFacePetals[0]
    trigger = getTrigger(theCube, index)
    theCube.rotate(trigger)
    sequence += trigger
    theCube.rotate(trigger)
    sequence += trigger
    return sequence

def _handleBottomRow(theCube, bottomFacePetals):
    sequence = ""
    index = bottomFacePetals[0]
    trigger = getTrigger(theCube, index)
    theCube.rotate(trigger)
    sequence += trigger
    return sequence

# if we've reached this point, we have the bottom surface solved but the bottom layer unsolved
def _handleSpecialCase(theCube): 
    sequence = ""
    for faceIndex in range(NUM_ADJACENT_FACES):
        colorMatchIndex = faceIndex * NUM_SQUARES_PER_FACE + XMM # center square in respective side
        for squareIndex in range(NUM_SQUARES_PER_ROW):
            bottomLayerIndex = colorMatchIndex + squareIndex
            if theCube.get()[bottomLayerIndex] != theCube.get()[colorMatchIndex]:
                trigger = getTrigger(theCube, bottomLayerIndex)
                theCube.rotate(trigger)
                sequence += trigger
    return sequence

'''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer
        
        Solution Process:
            
            START WITH TOP ROW
                align with adjacent color
                do trigger of opposite side hand
            ON UP
                two consecutive triggers on hand
            ON BOTTOM
                move to UP with trigger adjacent cell
        
        Test Analysis:
            Happy Path:
                test 000 - "solves" already solved cube for this step
                test 001 - solves random color assortment
            Sad Path:
                not applicable?
'''

def solveBottomLayer(theCube: Cube) -> str:
    sequence = ""
    petal = theCube.get()[DMM]
    loopCount = 0
    while not(_isSolved(theCube)):
        if not(theCube.petalsInPlace()):
            raise SolveError
        loopCount += 1
        if loopCount > MAX_WHILE_LOOPS:
            raise SolveError
        # check top row
        topRowPetals = []
        while len(topRowPetals := _getTopRowPetals(theCube, petal)) > 0:
            sequence += _handleTopRow(theCube, topRowPetals)
        # check up face
        upFacePetals = []
        if len(upFacePetals := _getUpFacePetals(theCube, petal)) > 0:
            sequence += _handleUpFace(theCube, upFacePetals)
            continue
        # check bottom row
        bottomFacePetals = []
        if len(bottomFacePetals := _getBottomRowPetals(theCube, petal)) > 0:
            sequence += _handleBottomRow(theCube, bottomFacePetals)
            continue
        sequence += _handleSpecialCase(theCube)
    return sequence