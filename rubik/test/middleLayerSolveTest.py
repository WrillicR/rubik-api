from unittest import TestCase
from rubik.model.cube import Cube
from rubik.view.solve import solve
from rubik.model.constants import *
from rubik.controller.middleLayer import *
 

class middleLayerSolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    
    def test_000_shouldSolvePreSolvedCube(self):
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveMiddleLayer(theCube)
        self.assertEqual("", solution)
        
    def test_001_shouldSolveSuperSimpleCube(self):
        encodedCube = "byrybbybbyybrrrrrryorggggggggwooroogyboyyoobbowwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveMiddleLayer(theCube)
        self.assertEqual("luL", solution)
        
    def test_002_shouldSolveSimpleCube(self):
        encodedCube = "oggbbybbbybybrrrrrbyoggggggbrgooooooyoryyryyrwwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveMiddleLayer(theCube)
        self.assertEqual("UURUrufuF", solution)
        
    def test_003_shouldSolveStrayMiddleCube(self):
        encodedCube = "ggyobbbbboygrrrrrryyrggggggyyyoobooobbrryooybwwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveMiddleLayer(theCube)
        self.assertEqual("luLuuuFUfUUuluLuuuFUf", solution)
        
    def test_003_shouldSolveComplexCube(self):
        encodedCube = "yrrgbybbbyyybrorrroyyggbgggrgoooyooogrbryogbbwwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveMiddleLayer(theCube)
        self.assertIn("U", solution)
        
    def test_004_shouldSolveMoreComplexCube(self):
        encodedCube = "goygbybbboyoororrryrbggggggrbrroyoooybgyyrybbwwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveMiddleLayer(theCube)
        self.assertIn("U", solution)