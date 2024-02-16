import unittest
import rubik.model.cube as cube
from rubik.model.constants import *


'''
Analysis:

    Goal:
        Cube needs to rotate, in sequence, the faces specified by each given direction and store the result
    
    Methods:
        __init__    assigns cube variable from a given string
        rotate      takes the cube variable and rotate in the given directions
        get         return the cube variable
        
    Analysis - Cube.rotate:
        Inputs/Outputs:
            Inputs:
                directions : string, length >=0, [FfRrBbLlUu] 
            Outputs:
                Side-effects:
                    not applicable
                Nominal:
                    return the rotated cube variable            
                Abnormal:
                    throw a DirectionException
                
        Tests:
            Happy Path:
                test 000:    F rotation
                test 005:    f rotation
                test 010:    R rotation
                test 015:    r rotation
                test 020:    B rotation
                test 025:    b rotation
                test 030:    L rotation
                test 035:    l rotation
                test 040:    U rotation
                test 045:    u rotation
                test 050:    D rotation
                test 055:    d rotation
                ...
                test 110:    empty direction  ->  default to "F"
                test 120:    multiple directions
                test 130:    no direction
            Sad Path:
                test 900:    invalid direction
            Evil Path:
                not applicable
'''

class CubeTest(unittest.TestCase):

    '''
    def test_999_ShouldDoNothing(self):
        cubeString = "ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg";
        myCube = cube.Cube(cubeString)
        myCube.rotate("F")
        self.assertEqual(myCube.get(), "ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg")
    '''
    
    def test_000_ShouldReturnCorrectF_Rotation(self):
        cubeString = "ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg";
        myCube = cube.Cube(cubeString)
        myCube.rotate("F")
        self.assertEqual(myCube.get(), "brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg")
    
    def test_005_ShouldReturnCorrectf_Rotation(self):
        cubeString = "ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg";
        myCube = cube.Cube(cubeString)
        myCube.rotate("f")
        self.assertEqual(myCube.get(), "ywwobborbgyoyroybowbrggwwrybwogobgobwwbryggorygrywrryg")
        
    def test_010_ShouldReturnCorrectR_Rotation(self):
        cubeString = "ZDDDZZDLZXZQXQXLZZDZDLDQXXLQXnnXnZLLLnnnnLQQnXDXQLQQDn";
        myCube = cube.Cube(cubeString)
        myCube.rotate("R")              
        self.assertEqual(myCube.get(), "ZDXDZQDLnLXXZQZZXQnZDLDQnXLQXnnXnZLLLnDnnZQQZXDXQLLQDD")
        
    def test_015_ShouldReturnCorrectr_Rotation(self):
        cubeString = "MjM66jZZZJMhMZh6ZMMJZJhhJ6hJjjMMZZJ6hMjZj66h6JJj6Jhjjh";
        myCube = cube.Cube(cubeString)
        myCube.rotate("r")              
        self.assertEqual(myCube.get(), "Mjj666ZZ6hhMMZZJM6hJZhhhj6hJjjMMZZJ6hMJZjJ6hMJJM6JjjjZ")
        
    def test_020_ShouldReturnCorrectB_Rotation(self):
        cubeString = "UwGUwGwwUynyqGUnGqGGUyqqnGynnyyUqUwnwwqqyUwywGUqnnnqyG";
        myCube = cube.Cube(cubeString)
        myCube.rotate("B")              
        self.assertEqual(myCube.get(), "UwGUwGwwUynGqGynGqnyGGqGyqUqnywUqwwnyUqqyUwywGUqnnnnyU")
        
    def test_025_ShouldReturnCorrectb_Rotation(self):
        cubeString = "ooySDDDSoKD9yy99SSDDDKKy9S9yyyK99o9oSoSoS9KKSyKDooDKyK";
        myCube = cube.Cube(cubeString)
        myCube.rotate("b")              
        self.assertEqual(myCube.get(), "ooySDDDSoKDSyyo9SSDy9DKSDK9Kyyy99K9ooKyoS9KKSyKDooDS99")
        
    def test_030_ShouldReturnCorrectL_Rotation(self):
        cubeString = "KddddCK7C799KC97C9C99KKdL7dLL77LL7LCKLdK7dLCL9KK799CCd";
        myCube = cube.Cube(cubeString)
        myCube.rotate("L")              
        self.assertEqual(myCube.get(), "KddKdCL7C799KC97C9C9CKK7L7977LLLLCL7dLdd7d9CLKKKd99KCd")
        
    def test_035_ShouldReturnCorrectl_Rotation(self):
        cubeString = "yslyyhs3hsl3lhh3y3yT3slTyyylssyThh3lTlhl33TTThhlTs3ssT";
        myCube = cube.Cube(cubeString)
        myCube.rotate("l")              
        self.assertEqual(myCube.get(), "hslTyhs3hsl3lhh3y3yTTsllyyTshlsT3lyhylhy33sTTyhlTs33sT")
        
    def test_040_ShouldReturnCorrectU_Rotation(self):
        cubeString = "TTxETZxTuZEuGZuETEEuEGuEGZuxTGuExZuuTxGxGGZGTZExZxZGxT";
        myCube = cube.Cube(cubeString)
        myCube.rotate("U")              
        self.assertEqual(myCube.get(), "ZEuETZxTuEuEGZuETExTGGuEGZuTTxuExZuuZxTGGxTGGZExZxZGxT")
        
    def test_045_ShouldReturnCorrectu_Rotation(self):
        cubeString = "TrpTTprprLWTWrTLTyrrpWpypyWrrLpyrTTpLWWpWyyLyWLTLLyyLW";
        myCube = cube.Cube(cubeString)
        myCube.rotate("u")              
        self.assertEqual(myCube.get(), "rrLTTprprTrpWrTLTyLWTWpypyWrrppyrTTpWyyWWLLpyWLTLLyyLW")
    
    
    def test_110_ShouldNotRotate(self):
        cubeString = "ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg";
        myCube = cube.Cube(cubeString)
        myCube.rotate("")              
        self.assertEqual(myCube.get(), "ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg")
        
    def test_120_ShouldDoMultipleRotations(self):
        cubeString = "RuCuCRWWvWC5CRWu5WCv5vuCuuuvC5vvvW5CC5RW55uRRvR5RWuRWv";
        myCube = cube.Cube(cubeString)
        myCube.rotate("lubRFrfBLU")              
        self.assertEqual(myCube.get(), "5u55CuvWCuC55RWRuWvCCvuCuuuRRuvvvW5W5WCC55RRvCRWRWvRWv")
        
    def test_130_ShouldDefaultMissingDirection(self):
        cubeString = "dhhhhrr0drdg0r00hhdgSd00SrSrShggg0gShd0hdrgrd0SrSSdgSg";
        myCube = cube.Cube(cubeString)
        myCube.rotate(None)
        self.assertEqual(myCube.get(), "dhhhhrr0drdg0r00hhdgSd00SrSrShggg0gShd0hdrgrd0SrSSdgSg")
    
    def test_900_ShouldThrowDirectionError(self):
        cubeString = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww";
        myCube = cube.Cube(cubeString)
        self.assertRaises(cube.DirectionError, myCube.rotate, "z")
    
