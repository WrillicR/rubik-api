from unittest import TestCase
from rubik.model.cube import Cube
from rubik.view.solve import solve
from rubik.model.constants import *
from rubik.controller.upFaceSurface import *
 

class upFaceSurfaceTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    
    def test_000_shouldSolvePreSolvedCube(self):
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpSurface(theCube)
        self.assertEqual("", solution)
        
    def test_001_shouldSolveSimpleCube(self):
        encodedCube = "ogybbbbbbbbyrrrrrrroyggggggorgoooooobygyyyyyrwwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpSurface(theCube)
        self.assertEqual("RUrURUUr", solution)
        
    def test_002_shouldSolveSimpleCubePlusRotation(self):
        encodedCube = "orgbbbbbbogyrrrrrrbbyggggggroyoooooogyryyybyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpSurface(theCube)
        self.assertEqual("URUrURUUr", solution)
        
    def test_003_shouldSolveMildCubePlusRotation(self):
        encodedCube = "ygybbbbbborrrrrrrryoygggggggbgoooooooybyyyrybwwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpSurface(theCube)
        self.assertEqual("URUrURUUrRUrURUUr", solution)
        
    def test_004_shouldSolveHardCube(self):
        encodedCube = "ogrbbbbbbybrrrrrrrgoyggggggorgoooooobyyyyyyybwwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveUpSurface(theCube)
        self.assertEqual("UUURUrURUUrRUrURUUrRUrURUUr", solution)
        