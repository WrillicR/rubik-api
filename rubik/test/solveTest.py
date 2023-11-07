from unittest import TestCase
from rubik.model.cube import Cube
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.model.constants import *
from rubik.controller.bottomCross import solveBottomCross
import hashlib
 

class SolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    
    def test_000_solve_returnSolvedSolution(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertNotEqual("", result['integrity'])
        self.assertEqual('', result.get('solution'))
    
    def test_101_solveNominalCube(self):
        parms = {}
        parms['cube'] = 'rgybbbbbbogwrryrrroorogyyggwbbrooyoogggyyyyrbwwwwwwowg'
        result = solve(parms)
        self.assertNotEqual("", result['integrity'])
        self.assertEqual('ok', result['status'])
    
    def test_102_solveNominalCube(self):
        parms = {}
        parms['cube'] = 'l6hlNL4NL6lh446lLhNlNNlhlLNLhhN6hL4L4446hL6lNl46hLN664'
        result = solve(parms)
        self.assertEqual('ok', result['status'])
    
    def test_103_solveNominalCube(self):
        parms = {}
        parms['cube'] = 'tYv0tvCtv0tvY00Y00tttYYYYvYCCCCNtC00NNNNCC0NtYvNCvvNNv'
        result = solve(parms)
        self.assertEqual('ok', result['status'])
    
    def test_104_solveNominalCube(self):
        parms = {}
        parms['cube'] = 'dSGGyGdSDyWGSDWGddWyWSSWSGGdyyyWWWdSyGyDGdDdDDDSDdySDW'
        result = solve(parms)
        self.assertEqual('ok', result['status'])
    
    def test_105_solveNominalCube(self):
        parms = {}
        parms['cube'] = '353RVVVVRRRTgR3g35gVTR5gggR55TTT5V33gTVT3V5g5T3V5gT3RR'
        result = solve(parms)
        self.assertEqual('ok', result['status'])
    
    def test_106_solveNominalCube(self):
        parms = {}
        parms['cube'] = 'r66Lr6Lr6SarkaLarLk6kr6r66LrkLkSaaSaaaSSkkSLkrSkLLa6SS'
        result = solve(parms)
        self.assertEqual('ok', result['status'])
    
    def test_107_solveNominalCube(self):
        parms = {}
        parms['cube'] = 'cazaocAzpaazAAAaazcoapppczzAcpczpazcoApocAAzoopAoaopco'
        result = solve(parms)
        self.assertEqual('ok', result['status'])
    
    def test_022_solve_returnFullRotations(self):
        encodedCube = "obybbygrbgwogrrygbgogggrryyyrbyoybgrrwwbybwoowwrowwoow"
        theCube = Cube(encodedCube)
        solution = solveBottomCross(theCube)
        newCube = Cube(encodedCube)
        newCube.rotate(solution)
        actual = newCube.get()
        self.assertEqual("w", actual[DTM])
        self.assertEqual("w", actual[DML])
        self.assertEqual("w", actual[DMR])
        self.assertEqual("w", actual[DBM])
        self.assertEqual("b", actual[FBM])
        self.assertEqual("r", actual[RBM])
        self.assertEqual("g", actual[BBM])
        self.assertEqual("o", actual[LBM])
    
    def test_032_solve_returnFullRotations(self):
        encodedCube = "gwbrbrwygrbobrywbbygwrgoorobbrgogwwroygwyoygyborowygwy"
        theCube = Cube(encodedCube)
        solution = solveBottomCross(theCube)
        newCube = Cube(encodedCube)
        newCube.rotate(solution)
        actual = newCube.get()
        self.assertEqual("w", actual[DTM])
        self.assertEqual("w", actual[DML])
        self.assertEqual("w", actual[DMR])
        self.assertEqual("w", actual[DBM])
        self.assertEqual("b", actual[FBM])
        self.assertEqual("r", actual[RBM])
        self.assertEqual("g", actual[BBM])
        self.assertEqual("o", actual[LBM])
        
    def test_042_solve_returnFullRotations(self):
        encodedCube = "rbgobwwoooowbrgyrygbgygwrrbywwgoywboryrrywboyggbrwyogb"
        theCube = Cube(encodedCube)
        solution = solveBottomCross(theCube)
        newCube = Cube(encodedCube)
        newCube.rotate(solution)
        actual = newCube.get()
        self.assertEqual("w", actual[DTM])
        self.assertEqual("w", actual[DML])
        self.assertEqual("w", actual[DMR])
        self.assertEqual("w", actual[DBM])
        self.assertEqual("b", actual[FBM])
        self.assertEqual("r", actual[RBM])
        self.assertEqual("g", actual[BBM])
        self.assertEqual("o", actual[LBM])
        
        
        
        
    def test_055_solve_shouldSolveEntireCube(self):
        encodedCube = "rbgobwwoooowbrgyrygbgygwrrbywwgoywboryrrywboyggbrwyogb"
        parms = {'cube' : encodedCube}
        solution = solve(parms)
        self.assertIn("ok", solution.get('status'))
        resultingCube = Cube(encodedCube)
        resultingCube.rotate(solution.get('solution'))
        self.assertEqual('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', resultingCube.get())
    
        
    def test_065_solve_shouldSolveEntireCube(self):
        encodedCube = "tU9EEUEEytttttUMtU99MEy9MyE9tyMM9MyUyyEE9yUMytMUMU99UE"
        parms = {'cube' : encodedCube}
        solution = solve(parms)
        self.assertIn("ok", solution.get('status'))
        resultingCube = Cube(encodedCube)
        resultingCube.rotate(solution.get('solution'))
        self.assertEqual('EEEEEEEEEtttttttttyyyyyyyyyMMMMMMMMM999999999UUUUUUUUU', resultingCube.get())
    
    
    
    def test_100_solve_bottomLayerFromBottomCross(self):
        encodedCube = "ryggbbbbwoygyryorbwbwrggrgygbboorgoyrooryoygyowbwwwrww"
        parms = {'cube' : encodedCube}
        solution = solve(parms)
        self.assertIn("ok", solution.get('status'))
        resultingCube = Cube(encodedCube)
        resultingCube.rotate(solution.get('solution'))
        self.assertEqual('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', resultingCube.get())
        
    def test_101_solve_bottomLayerFromScratch(self):
        encodedCube = "bygyborygwrbbrrywrrorggwwgygbwooobrwygyyyworoggobwbowb"
        parms = {'cube' : encodedCube}
        solution = solve(parms)
        newCube = Cube(encodedCube)
        newCube.rotate(solution.get('solution'))
        self.assertIn("ok", solution.get('status'))
        resultingCube = Cube(encodedCube)
        resultingCube.rotate(solution.get('solution'))
        self.assertEqual('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', resultingCube.get())
        
    def test_200_solve_nominalBottomCross(self):
        encodedCube = "l6hlNL4NL6lh446lLhNlNNlhlLNLhhN6hL4L4446hL6lNl46hLN664"
        parms = {'cube' : encodedCube}
        solution = solve(parms)
        self.assertIn("ok", solution.get('status'))

    def test_910_solve_shouldErrMissingCube(self):
        parms = {}
        solution = solve(parms)
        self.assertIn('error', solution.get('status'))
        
    def test_920_solve_shouldErrShortCube(self):
        encodedCube = "OOl3mdlld13Ol3dO3"
        parms = {'cube' : encodedCube}
        solution = solve(parms)
        self.assertIn('error', solution.get('status'))
        
    def test_930_solve_shouldErrIllegalCharCube(self):
        encodedCube = "bbbbbbbbb*********rrrrrrrrroooooooooyyyyyyyyywwwwwwwww"
        parms = {'cube' : encodedCube}
        solution = solve(parms)
        self.assertIn('error', solution.get('status'))
        
    def test_940_solve_shouldErrTooManyCharCube(self):
        encodedCube = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb"
        parms = {'cube' : encodedCube}
        solution = solve(parms)
        self.assertIn('error', solution.get('status'))
        
    def test_950_integrity_test(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        author = "wgr0009"
        itemToTokenize = parms['cube'] + result.get('solution') + author
        sha256Hash = hashlib.sha256()
        sha256Hash.update(itemToTokenize.encode())
        fullToken = sha256Hash.hexdigest()
        self.assertIn(result['integrity'], fullToken)
        
    
        