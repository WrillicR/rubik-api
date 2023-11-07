from rubik.model.constants import *
import re

class Cube:

    def __init__(self, encodedCube):
        
        if encodedCube == None or encodedCube == "":
            raise CubeError
        
        ## check middle values
        middles = []
        for face in range(NUM_FACES):
            middleIndex = face * NUM_SQUARES_PER_FACE + MIDDLE_SQUARE_INDEX
            middles.append(encodedCube[middleIndex:middleIndex+1])
        
        if len(set(middles)) != 6:
            raise CubeError
        
        ## check alphanumeric values
        if re.search("[^a-zA-Z0-9]", encodedCube) != None:
            raise CubeError
            
        ## check 6 unique colors
        if len(set(encodedCube)) != NUM_FACES:
            raise CubeError
        
        ## check number of colors
        for color in set(encodedCube):
            if encodedCube.count(color) != 9:
                raise CubeError
        
        ## check for complete cube
        if len(encodedCube) != NUM_SQUARES_TOTAL:
            raise CubeError
        
        self.cube = encodedCube
        
    def getFaceFromIndex(self, index):
        faceIndex = 0
        while index >= NUM_SQUARES_PER_FACE:
            index -= NUM_SQUARES_PER_FACE
            faceIndex += 1
        face = FACE_MAP[faceIndex]
        
        return face
    
    def getFaceFromColor(self, color):
        colorIndices = [FMM, RMM, BMM, LMM]
        colorValues = [self.cube[x] for x in colorIndices]
        colorIndex = colorIndices[colorValues.index(color)]
        return self.getFaceFromIndex(colorIndex)
           
    def petalsInPlace(self):
        indexArray = [DMM, DMM, DMM, DMM, DMM, FMM, RMM, BMM, LMM]
        valueArray = [DTM, DML, DMM, DMR, DBM, FBM, RBM, BBM, LBM] 
        booleArray = [self.get()[valueArray[x]] == self.get()[indexArray[x]] for x in range(len(indexArray))]
        return all(booleArray)
    
    def _rotateSingleFace(self, initialIndex, cubeList):
        newCube = cubeList[:]
        newCube[initialIndex+FTR] = cubeList[initialIndex+FTL]
        newCube[initialIndex+FMR] = cubeList[initialIndex+FTM]
        newCube[initialIndex+FBR] = cubeList[initialIndex+FTR]
        newCube[initialIndex+FTM] = cubeList[initialIndex+FML]
        newCube[initialIndex+FBM] = cubeList[initialIndex+FMR]
        newCube[initialIndex+FTL] = cubeList[initialIndex+FBL]
        newCube[initialIndex+FML] = cubeList[initialIndex+FBM]
        newCube[initialIndex+FBL] = cubeList[initialIndex+FBR]
        return newCube
    
    def _rotateSideF(self, rotatedCube, cubeArray):
        rotatedCube[UBL] = cubeArray[LBR]
        rotatedCube[UBM] = cubeArray[LMR]
        rotatedCube[UBR] = cubeArray[LTR]
        
        rotatedCube[RTL] = cubeArray[UBL]
        rotatedCube[RML] = cubeArray[UBM]
        rotatedCube[RBL] = cubeArray[UBR]
        
        rotatedCube[DTL] = cubeArray[RBL]
        rotatedCube[DTM] = cubeArray[RML]
        rotatedCube[DTR] = cubeArray[RTL]
        
        rotatedCube[LTR] = cubeArray[DTL]
        rotatedCube[LMR] = cubeArray[DTM]
        rotatedCube[LBR] = cubeArray[DTR]
        
        return rotatedCube
    
    def _rotateSideR(self, rotatedCube, cubeArray):
        rotatedCube[UTR] = cubeArray[FTR]
        rotatedCube[UMR] = cubeArray[FMR]
        rotatedCube[UBR] = cubeArray[FBR]
        
        rotatedCube[BTL] = cubeArray[UBR]
        rotatedCube[BML] = cubeArray[UMR]
        rotatedCube[BBL] = cubeArray[UTR]
        
        rotatedCube[DTR] = cubeArray[BBL]
        rotatedCube[DMR] = cubeArray[BML]
        rotatedCube[DBR] = cubeArray[BTL]
        
        rotatedCube[FTR] = cubeArray[DTR]
        rotatedCube[FMR] = cubeArray[DMR]
        rotatedCube[FBR] = cubeArray[DBR]
        
        return rotatedCube
    
    def _rotateSideB(self, rotatedCube, cubeArray):
        rotatedCube[UTL] = cubeArray[RTR]
        rotatedCube[UTM] = cubeArray[RMR]
        rotatedCube[UTR] = cubeArray[RBR]

        rotatedCube[LTL] = cubeArray[UTR]
        rotatedCube[LML] = cubeArray[UTM]
        rotatedCube[LBL] = cubeArray[UTL]

        rotatedCube[DBL] = cubeArray[LTL]
        rotatedCube[DBM] = cubeArray[LML]
        rotatedCube[DBR] = cubeArray[LBL]

        rotatedCube[RTR] = cubeArray[DBR]
        rotatedCube[RMR] = cubeArray[DBM]
        rotatedCube[RBR] = cubeArray[DBL]
        
        return rotatedCube
    
    def _rotateSideL(self, rotatedCube, cubeArray):
        rotatedCube[UTL] = cubeArray[BBR]
        rotatedCube[UML] = cubeArray[BMR]
        rotatedCube[UBL] = cubeArray[BTR]
        
        rotatedCube[FTL] = cubeArray[UTL]
        rotatedCube[FML] = cubeArray[UML]
        rotatedCube[FBL] = cubeArray[UBL]
        
        rotatedCube[DTL] = cubeArray[FTL]
        rotatedCube[DML] = cubeArray[FML]
        rotatedCube[DBL] = cubeArray[FBL]
        
        rotatedCube[BBR] = cubeArray[DTL]
        rotatedCube[BMR] = cubeArray[DML]
        rotatedCube[BTR] = cubeArray[DBL]
        
        return rotatedCube
    
    def _rotateSideU(self, rotatedCube, cubeArray):
        rotatedCube[FTL] = cubeArray[RTL]
        rotatedCube[FTM] = cubeArray[RTM]
        rotatedCube[FTR] = cubeArray[RTR]
        
        rotatedCube[RTL] = cubeArray[BTL]
        rotatedCube[RTM] = cubeArray[BTM]
        rotatedCube[RTR] = cubeArray[BTR]
        
        rotatedCube[BTL] = cubeArray[LTL]
        rotatedCube[BTM] = cubeArray[LTM]
        rotatedCube[BTR] = cubeArray[LTR]
        
        rotatedCube[LTL] = cubeArray[FTL]
        rotatedCube[LTM] = cubeArray[FTM]
        rotatedCube[LTR] = cubeArray[FTR]
        
        return rotatedCube
    
    
    def rotate(self, directions):
        
        for direction in list(directions):
            
            if not direction.upper() in DIRECTION_MAP:
                raise DirectionError
            
            cubeArray = list(self.cube)
            rotatedCube = cubeArray[:]
            clockwise = not(direction.isupper())
            rotations = 1 + (clockwise * 2)
            direction = direction.upper()
            
            for _ in range(rotations):
                rotatedCube = self._rotateSingleFace(DIRECTION_MAP.index(direction.upper()) * NUM_SQUARES_PER_FACE, rotatedCube)
                
                if direction == "F":
                    rotatedCube = self._rotateSideF(rotatedCube, cubeArray)
                elif direction == "R":
                    rotatedCube = self._rotateSideR(rotatedCube, cubeArray)
                elif direction == "B":
                    rotatedCube = self._rotateSideB(rotatedCube, cubeArray)
                elif direction == "L":
                    rotatedCube = self._rotateSideL(rotatedCube, cubeArray)
                elif direction == "U":
                    rotatedCube = self._rotateSideU(rotatedCube, cubeArray)
                    
                cubeArray = rotatedCube
                    
            self.cube = ''.join(rotatedCube)
        
        
    def get(self):
        return self.cube
        
        
class DirectionError(Exception):
    pass

class CubeError(Exception):
    pass

class SolveError(Exception):
    pass