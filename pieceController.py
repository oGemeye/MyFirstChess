
class Board:
    redPieces_Back = ["R1", "Kn1", "B1", "Q", "K", "B2", "Kn2", "R2"]
    redPieces_Pawn = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
    bluePieces_Back = ["R1", "Kn1", "B1", "Q", "K", "B2", "Kn2", "R2"]
    bluePieces_Pawn = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
    vert = 8
    hori = 8
    
    __init__(self):
        redPos = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], 
                [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]
        bluePos = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], 
                [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]


blank = ["" for x in range(8)]
horizontal = blank
vertical = [blank for x in range(8)]

def initBoard(board):
    for y in range(8):
        for x in range(8):
            if y in [0, 7]:
                board[x][y] = " o "
            elif y in [1, 6]:
                board[x][y] = " p "
            elif y in [2, 3, 4, 5]:
                board[x][y] = " _ "
    return board

def printBoard(board):
    for y in range(8):
        for x in range(8):
            print(board[x][y], end="")
        print("")
    print("")

board = initBoard(vertical)
#printBoard(board)