"""
controls pieces in an 8x8 board
top left coord is (x, y) = (0, 0) internally, A1 externally, found at board[y][x]
top right coord is (x, y) = (0, 7) internally, A8 externally
bottom left coord is (x, y) = (7, 0) internally, H1 externally
bottom right coord is (x, y) = (7, 7) internally, H8 externally
"""

from pieceMove import canPieceMoveThere
from moveValidator import validCoord, getNumCoord

p1 = "B"
p2 = "R"
currentPlayer = p1
turnCount = 1
gameOver = False
blankPiece = ["", ""]
board = [
        [[p2, "R"], [p2, "Kn"], [p2, "B"], [p2, "K"], [p2, "Q"], [p2, "B"], [p2, "Kn"], [p2, "R"]],
        [[p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"]],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [[p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], ],
        [[p1, "R"], [p1, "Kn"], [p1, "B"], [p1, "Q"], [p1, "K"], [p1, "B"], [p1, "Kn"], [p1, "R"]]
        ]

def movePiece(fromPosExternal, toPosExternal):
    """ fromPosExternal: (CHAR, INT) coord where piece to move currently is
        toPos: (CHAR, INT) coord where piece should be moved to
        returns false if fromPos doesnt have a piece, or it can't move to toPos"""
    
    if (not validCoord(fromPosExternal)
        or not validCoord(toPosExternal)
        or isSameCoord(fromPosExternal, toPosExternal)):
        print("weird cells provided")
        return False
    
    fromCoord = getNumCoord(fromPosExternal)
    toCoord = getNumCoord(toPosExternal)
    if (isEmptyCell(fromCoord)):
        print("trying to move empty cell")
        return False
    
    moveMe = getPieceAtPos(fromCoord)
    print(moveMe)
    if (not isYourTurn(moveMe)):
        print("not your turn")
        return False
    """at this point we know that a valid piece was chosen to be moved, now we find out if we can"""

    if (not isValidMove(moveMe, fromCoord, toCoord)):
        print("move wont work")
        return False
    
    """at this point, we know we're looking at a piece to move,
    we know we have a valid place it can move,
    we know it's able to move there
    so, we move it"""

    moveMyPiece(moveMe, fromCoord, toCoord)

    cleanUpTurn();   

    return True


def isSameCoord(extPos1, extPos2):
    return extPos1[0] == extPos2[0] \
        and extPos1[1] == extPos2[1]

def getPieceAtPos(pos):
    '''Checks if a piece exists at the Coordinate provided'''
    return board[pos.y][pos.x]

def isEmptyCell(pos):
    """checks if the cell at x = pos[0], y = pos[1] is empty"""
    return getPieceAtPos(pos) == 0

def isYourTurn(piece):
    return piece[0] == currentPlayer

def isValidMove(piece, fromPos, toPos):
    print(f'isEmpty: {isEmptyCell(toPos)}, {toPos[0] != fromPos[0]}, canMove: {canPieceMoveThere(board, piece, fromPos, toPos)}')
    return ((not isEmptyCell(fromPos)) or toPos[0] != fromPos[0]) \
        and canPieceMoveThere(board, piece, fromPos, toPos)

def moveMyPiece(piece, fromPos, toPos):
    """if the piece being taken over is a kind, the game is over
    regardless, move the piece"""
    toBeCaptured = board[toPos[1]][toPos[0]]
    gameOver = isKingPiece(toBeCaptured)

    board[toPos[1]][toPos[0]] = piece
    board[fromPos[1]][fromPos[0]] = blankPiece

def isKingPiece(piece):
    return piece[1] == "K"

def cleanUpTurn():
    global turnCount
    turnCount += 1
    swapPlayer();

def swapPlayer():
    global currentPlayer
    if currentPlayer is p1:
        currentPlayer = p2
    else:
        currentPlayer = p1

def getCurrentPlayerString():
    if currentPlayer is p1:
        return "Blue"
    else:
        return "Red"

def getCurrentTurn():
    return turnCount

def isGameOver():
    return gameOver