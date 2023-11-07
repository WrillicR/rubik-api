from unittest import TestCase
from rubik.model.cube import Cube
from rubik.view.solve import solve
from rubik.model.constants import *
from rubik.controller.bottomLayer import *
 

class bottomLayerSolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    
    def test_000_shouldSolvePreSolvedCube(self):
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveBottomLayer(theCube)
        self.assertEqual("", solution)
        
    def test_001_shouldSolveSimpleCube(self):
        encodedCube = "orrybobbyyobbrrorrwbgygygggyoygobooorrryygbgbwwgwwwwww"
        theCube = Cube(encodedCube)
        solution = solveBottomLayer(theCube)
        self.assertEqual("URUr", solution)
        
    def test_002_shouldSolveLessSimpleCube(self):
        encodedCube = "bowybobbrgybgrbbrgwggogyyggyrogobooorrrbyryyrwwywwwwwo"
        theCube = Cube(encodedCube)
        solution = solveBottomLayer(theCube)
        self.assertEqual("uruRUUURUr", solution)
        
    def test_003_shouldSolveTopRowCube(self):
        encodedCube = "ybbybbybroybrrgyrrwggogygggobbgoooobyrryyroowrwgwwwwww"
        theCube = Cube(encodedCube)
        solution = solveBottomLayer(theCube)
        self.assertEqual("URUrbuBbuBuuLUlUluL", solution)
        
    def test_004_shouldSolveMediumCube(self):
        encodedCube = "rbwobyybbbrogrgyrryyrogrggggowboboooyrgyygbyobwrwwwwww"
        theCube = Cube(encodedCube)
        solution = solveBottomLayer(theCube)
        self.assertIn("U", solution)
        
    def test_005_shouldSolveBottomRowCube(self):
        encodedCube = "byyybrobbbbggrgrrrybyogrggggyoboroowoorgyyyorbwwwwwwww"
        theCube = Cube(encodedCube)
        solution = solveBottomLayer(theCube)
        self.assertIn("U", solution)
        
    # gboybyybwbyrrrrorobgrbgywgywgyoobrorgowrygooygwbwwwbwg
    # yrybbyobygrrorggrwwbbyggogowrrooowobryggyybboywrwwwgwb
    def test_006_shouldSolveHardCube(self):
        encodedCube = "grbybgybgybbrrywrbrgboggrgyobooorgogwyyoyywboowrwwwrww"
        theCube = Cube(encodedCube)
        solution = solveBottomLayer(theCube)
        self.assertIn("U", solution)
        
    def test_007_shouldSolveHarderCube(self):
        encodedCube = "ryggbbbbwoygyryorbwbwrggrgygbboorgoyrooryoygyowbwwwrww"
        theCube = Cube(encodedCube)
        solution = solveBottomLayer(theCube)
        self.assertIn("U", solution)
        
    # method getTrigger(index)
    
    def test_200_ShouldReturnFTL_Trigger(self):
        index = FTL
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        trigger = getTrigger(theCube, index)
        self.assertEquals("FUf", trigger)
    
    def test_201_ShouldReturnRBL_Trigger(self):
        index = RBL
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        trigger = getTrigger(theCube, index)
        self.assertEquals("fuF", trigger)
        
    def test_202_ShouldReturnLBL_Trigger(self):
        index = LBL
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        trigger = getTrigger(theCube, index)
        self.assertEquals("buB", trigger)
        
    def test_203_ShouldReturnBTR_Trigger(self):
        index = BTR
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        trigger = getTrigger(theCube, index)
        self.assertEquals("buB", trigger)
        
    def test_204_ShouldReturnBBR_Trigger(self):
        index = BBR
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        trigger = getTrigger(theCube, index)
        self.assertEquals("LUl", trigger)
        
    def test_205_ShouldReturnDTREmpty_Trigger(self):
        index = DTR
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        trigger = getTrigger(theCube, index)
        self.assertEquals("", trigger)
        
    # add test for sad path (down face or middle bits)
    
    def test_310_ShouldReturnEmpty_Trigger(self):
        index = FMM
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww"
        theCube = Cube(encodedCube)
        trigger = getTrigger(theCube, index)
        self.assertEqual("", trigger)
        
    