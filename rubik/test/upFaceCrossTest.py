from unittest import TestCase
from rubik.model.cube import Cube
from rubik.view.solve import solve
from rubik.model.constants import *
from rubik.controller.upFaceCross import *
 

class upFaceCrossTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    
    def test_000_shouldSolvePreSolvedCube(self):
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpCross(theCube)
        self.assertEqual("", solution)
    
    def test_001_shouldSolveSimpleCube(self):
        encodedCube = "gybbbbbbbryyrrrrrrgbbggggggyrroooooooyoyyoygywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpCross(theCube)
        self.assertEqual("FURurf", solution)
        
    def test_002_shouldSolveSimpleCubePlusRotation(self):
        encodedCube = "rbybbbbbbgyrrrrrrrgybggggggyobooooooogyyyryyowwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpCross(theCube)
        self.assertEqual("UFURurf", solution)
        
    def test_003_shouldSolveMildCube(self):
        encodedCube = "ryybbbbbbggrrrrrrrgybggggggyobooooooobyyyyyrowwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpCross(theCube)
        self.assertEqual("UFURurfUUFURurf", solution)
        
    def test_004_shouldSolveWorstCaseCube(self):
        encodedCube = "yyobbbbbbyyyrrrrrrryyggggggoyroooooobrgoybbggwwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpCross(theCube)
        self.assertEqual("FURurfFURurfUUFURurf", solution)