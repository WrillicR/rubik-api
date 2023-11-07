from unittest import TestCase
from rubik.view.rotate import rotate
 

'''
Analysis:

    Goal:
        Cube needs to rotate, in sequence, the faces specified by each given direction and store the result
    
    Methods:
        __init__    assigns cube variable from a given string
        rotate      take the cube variable and rotate in the given directions
        get         return the cube variable
        
    Analysis - rotate:
        Inputs/Outputs:
            Inputs:
                parms : python dictionary
                    cube : string, length == 54, [a-zA-Z0-9], 5th 14th 23rd 32nd 41st and 50th characters must be unique
                    direction : string, to be validated by Cube
            Outputs:
                Side-effects:
                    not applicable
                Nominal:
                    return the rotated cube string and status
                Abnormal:
                    return an error message
                
        Tests:
            Happy Path:
                test 000:    F rotation
                test 010:    DirectionException
            Sad Path:
                test 910:    cube expression with non alphanumeric characters
                test 920:    cube expression with more than six unique character
                test 930:    incomplete cube expression
                test 940:    extra keys passed
                test 950:    missing cube expression
                test 960:    cube expression with middle cubes non-unique
                test 970:    cube expression has too many colors
            Evil Path:
                not applicable
'''
 
 
class RotateTest(TestCase):
        
# Happy path
#    Test that the stubbed rotate returns the correct result
    def test_000_ShouldReturnF_Rotation(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        resultCube = 'bbbbbbbbbyrryrryrroooooooooggwggwggwyyyyyygggrrrwwwwww' 
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(resultCube, result.get('cube'))
        
    def test_010_ShouldReturnDirectionError(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'z'
        result = rotate(parms)
        self.assertEqual('error: invalid rotation', result['status'])
        
    def test_910_Alphanumeric_ShouldReturnCubeError(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwww!#'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'f'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_920_Too_Many_Uniques_ShouldReturnCubeError(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwcc'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'f'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_930_Incomplete_ShouldReturnCubeError(self):
        encodedCube = 'bacgft'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'f'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result['status'])

    def test_940_Extra_Keys_ShouldReturnCubeError(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['play'] = True
        parms['dir'] = 'f'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_950_Missing_Cube_ShouldReturnCubeError(self):
        parms = {}
        parms['dir'] = 'f'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_960_Middle_Cubes_Not_Unique_ShouldReturnCubeError(self):
        encodedCube = 'bbrbbbbbbrrrrbrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'f'
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_970_ShouldDetectTooManyColors(self):
        cubeString = "bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb";
        parms = {}
        parms['cube'] = cubeString
        result = rotate(parms)
        self.assertEqual('error: invalid cube', result['status'])
        