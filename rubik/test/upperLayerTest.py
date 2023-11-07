from unittest import TestCase
from rubik.model.cube import Cube
from rubik.view.solve import solve
from rubik.model.constants import *
from rubik.controller.upperLayer import *
 

class upFaceSurfaceTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    
    def test_000_shouldSolvePreSolvedCube(self):
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpperLayer(theCube)
        self.assertEqual("", solution)
    
    
    #def test_010_shouldRotateToFirstStep(self):
    #    encodedCube = "grbbbbbbbrggrrrrrroboggggggborooooooyyyyyyyyywwwwwwwww"
    #    theCube = Cube(encodedCube)
    #    solution = solveUpperLayer(theCube)
    #    self.assertEqual("u", solution)
        
    #def test_020_shouldDoFirstStep(self):
    #    encodedCube = "bgrbbbbbbgbbrrrrrrrogggggggoroooooooyyyyyyyyywwwwwwwww"
    #    theCube = Cube(encodedCube)
    #    solution = solveUpperLayer(theCube)
    #    self.assertEqual("lURuLUrRUrURUUr", solution)
        
    #def test_030_shouldDoFirstStep(self):
    #    encodedCube = "rgrbbbbbbgborrrrrrbrgggggggoobooooooyyyyyyyyywwwwwwwww"
    #    theCube = Cube(encodedCube)
    #    solution = solveUpperLayer(theCube)
    #    self.assertEqual("UlURuLUrRUrURUUruu", solution)
        
    #def test_040_shouldDoFirstStep(self):
    #    encodedCube = "goobbbbbbbbgrrrrrrorbggggggrgrooooooyyyyyyyyywwwwwwwww"
    #    theCube = Cube(encodedCube)
    #    solution = solveUpperLayer(theCube)
    #    self.assertEqual("lURuLUrRUrURUUruu", solution)
        
    def test_050_shouldSolveAllSteps(self):
        encodedCube = "brbbbbbbbrgrrrrrrrgbgggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpperLayer(theCube)
        self.assertEqual("uuuFFULrFFlRUFFFFULrFFlRUFFu", solution)
        
    def test_060_shouldSolveAllSteps(self):
        encodedCube = "bgbbbbbbbrorrrrrrrgbgggggggoroooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpperLayer(theCube)
        self.assertEqual("bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww", theCube.get())
        
    def test_070_shouldSolveAllStepsMedium(self):
        encodedCube = "gggbbbbbboborrrrrrbrbggggggrorooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpperLayer(theCube)
        self.assertEqual("bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww", theCube.get())
        
    def test_075_shouldSolveAllStepsMedium(self):
        encodedCube = "rrgbbbbbboorrrrrrrggoggggggbbbooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpperLayer(theCube)
        self.assertEqual("bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww", theCube.get())
        
    def test_080_shouldSolveAllStepsHard(self):
        encodedCube = "obobbbbbbborrrrrrrgrbggggggrggooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpperLayer(theCube)
        self.assertEqual("bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww", theCube.get())
        
    def test_090_shouldSolveAllStepsHard(self):
        encodedCube = "oorbbbbbbgbbrrrrrrrgoggggggbrgooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpperLayer(theCube)
        self.assertEqual("bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww", theCube.get())
        