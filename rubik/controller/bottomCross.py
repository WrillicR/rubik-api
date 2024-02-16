from rubik.model.constants import *
from rubik.model.cube import *


def _getTopDirection(movingFace, emptySlots):
    direction = ""
    currSlot = emptySlots[0]
    num1 = PETAL_SLOTS.index(currSlot)
    num2 = FACE_MAP.index(movingFace[0].upper())
    # if we already have the top in the right location
    if num2 < 4 and PETAL_SLOTS[num2] in emptySlots:
        return ""
                    
    rotations = abs(num1 - num2)
    if rotations == 3:
        direction = "u"
    else:
        for _ in range(rotations):
            direction += "U"
    return direction


def _getEdgeFaceFromIndex(index):
    if index == FMR:
        return "R"
    elif index == FML:
        return "l"
    elif index == RMR:
        return "B"
    elif index == RML:
        return "f"
    elif index == BMR:
        return "L"
    elif index == BML:
        return "r"
    elif index == LMR:
        return "F"
    elif index == LML:
        return "b"
    elif index == DML:
        return "ll"
    elif index == DMR:
        return "RR"
    elif index == DTM:
        return "FF"
    elif index == DBM:
        return "bb"


def _getOpenPetalSlots(cubeString, petal):
    openSlots = []
    
    for slot in PETAL_SLOTS:
        if cubeString[slot] != petal:
            openSlots.append(slot)
    
    return openSlots

def _petalPlacement(theCube: Cube, petal):
    rotations = ""
    loopCount = 0
    while len(_getOpenPetalSlots(theCube.get(), petal)) > 0:
        if loopCount > MAX_WHILE_LOOPS:
            raise SolveError
        loopCount += 1
        for face in range(NUM_FACES):
            if face == UP_FACE:
                continue
            for square in range(NUM_SQUARES_PER_FACE):
                currStringIndex = face * NUM_SQUARES_PER_FACE + square
                if square % 2 == 1 and theCube.get()[currStringIndex] == petal: # rotate relative front face until able to be slid into open slot
                    if face != DOWN_FACE and (square == XTM or square == XBM): # prepare top face
                        topDirection = _getTopDirection(FACE_MAP[face], _getOpenPetalSlots(theCube.get(), petal))
                        if topDirection != "":
                            theCube.rotate(topDirection)
                            rotations += topDirection
                        theCube.rotate(FACE_MAP[face]) # rotate relative front face
                        rotations += FACE_MAP[face]
                        if square == XTM:
                            currStringIndex += 4
                        elif square == XBM:
                            currStringIndex -= 4
                    edgeFace = _getEdgeFaceFromIndex(currStringIndex)
                    topDirection = _getTopDirection(edgeFace, _getOpenPetalSlots(theCube.get(), petal))
                    if topDirection != "":
                        theCube.rotate(topDirection)
                        rotations += topDirection
                    
                    theCube.rotate(edgeFace)
                    rotations += edgeFace
    return rotations

def _colorAlignments(theCube: Cube, petal):
    rotations = ""
    # color alignment
    # continue until all petals are on the down face
    unmatchedColors = [FMM, RMM, BMM, LMM]
    loopCount = 0
    while len(unmatchedColors) > 0:
        if loopCount > MAX_WHILE_LOOPS:
            raise SolveError
        match = None
        for color in unmatchedColors:
            matchedFace = theCube.getFaceFromIndex(color)
            if theCube.get()[color - 3] == theCube.get()[color] and theCube.get()[PETAL_SLOTS[FACE_MAP.index(matchedFace)]] == petal:
                match = color
                theCube.rotate(matchedFace)
                theCube.rotate(matchedFace)
                rotations += matchedFace
                rotations += matchedFace
                unmatchedColors.remove(color)
                break
        if match == None:
            matchedFace = "U"
            theCube.rotate("U")
            rotations += "U"
            
    return rotations


'''
    This is the top-level function  for rotating
    a cube into the down-face cross configuration.
    
    input:  an instance of the cube class
    output: the rotations required to transform the input cube into the down-face cross
    
    Solution Process:
    PETAL PLACING:
        find a (any?arbitrary?) petal -> a cube at position 1,3,5,or 7 (on any face) that is not aligned to up face yet
        rotate until petal is in position
        repeat until all four petals are in place
    
    COLOR ALIGNMENT:
        for each edge of the petals...
        rotate until aligned with matching center color
        rotate face twice
        repeat until all four colors are in place
        
    Assuming cube instance is already validated
    
    Test Analysis:
        Happy path:
            test 001 - "solves" already solved cube
            test 011 - solves random color assortment
            test 021 - solves random color assortment
        Sad path:
            not applicable?... cube has already been validated
'''  
def solveBottomCross(theCube: Cube) -> str:
    
    rotations = ""
    petal = theCube.get()[DMM]
    if not(theCube.petalsInPlace()):
        rotations += _petalPlacement(theCube, petal)    
        rotations += _colorAlignments(theCube, petal)
            
    return rotations

