'''
Constants used across the microservice 
'''

NUM_FACES = 6
NUM_SQUARES_TOTAL = 54
NUM_SQUARES_PER_FACE = 9
MIDDLE_SQUARE_INDEX = 4
NUM_ADJACENT_FACES = 4
NUM_ADJACENT_SQUARES = 36
NUM_SQUARES_PER_ROW = 3

UP_FACE = 4
DOWN_FACE = 5
PETAL_SLOTS = [43, 41, 37, 39]
LEFT_MID_SLOTS = [3, 12, 21, 30]

CW = True
CCW = False

SQUARES_TO_ADJACENT = 7

# Relative front face
XTL = 0
XTM = 1
XTR = 2
XML = 3
XMM = 4
XMR = 5
XBL = 6
XBM = 7
XBR = 8

DIRECTION_MAP = ["F", "R", "B", "L", "U"]
FACE_MAP = ["F", "R", "B", "L", "U", "D"]
ADJ_MAP = ["F", "R", "B", "L"]

MAX_WHILE_LOOPS = 99

#-----------------------------------
#  Mapping of cube element positions to mnemonic names
#  Each mnemonic is a three-character pattern, frc, where
#       f indicates the face and is one of F, R, B, L, U, D
#       r indicates the row and is one of T, M, B (for top, middle, bottom, respectively)
#       c indicates the column and is one of L, M, R (for left, middle, right, repectively)
#  The regex for the pattern is r'[FRBLUD][TMB][LMR]'
#
# Front face
FTL = 0
FTM = 1
FTR = 2
FML = 3
FMM = 4
FMR = 5
FBL = 6
FBM = 7
FBR = 8

# Right face
RTL = 9
RTM = 10
RTR = 11
RML = 12
RMM = 13
RMR = 14
RBL = 15
RBM = 16
RBR = 17

# Back face
BTL = 18
BTM = 19
BTR = 20
BML = 21
BMM = 22
BMR = 23
BBL = 24
BBM = 25
BBR = 26

# Left face
LTL = 27
LTM = 28
LTR = 29
LML = 30
LMM = 31
LMR = 32
LBL = 33
LBM = 34
LBR = 35

# Up face
UTL = 36
UTM = 37
UTR = 38
UML = 39
UMM = 40
UMR = 41
UBL = 42
UBM = 43
UBR = 44

#Down face
DTL = 45
DTM = 46
DTR = 47
DML = 48
DMM = 49
DMR = 50
DBL = 51
DBM = 52
DBR = 53


