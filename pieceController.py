"""
controls pieces in an 8x8 board
top left coord is (x, y) = (0, 0) internally, A1 externally, found at board[y][x]
top right coord is (x, y) = (0, 7) internally, A8 externally
bottom left coord is (x, y) = (7, 0) internally, H1 externally
bottom right coord is (x, y) = (7, 7) internally, H8 externally
"""

from pieceMove import canPieceMoveThere
from moveValidator import validCoord, getNumCoord, Coordinate
from grid import p1, p2, blankPiece, pieceAt, assignToPieceAt, removePieceAt#, board

currentPlayer = p1
turnCount = 1
gameOver = False

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
    return pieceAt(pos.x, pos.y)

def isEmptyCell(pos):
    """checks if the cell at x = pos[0], y = pos[1] is empty"""
    return getPieceAtPos(pos) == 0

def isYourTurn(piece):
    return piece[0] == currentPlayer

def isValidMove(piece, fromPos, toPos):
    print(f'isEmpty: {isEmptyCell(toPos)}, {toPos.y != fromPos.y}, canMove: {canPieceMoveThere(piece, fromPos, toPos)}')
    return ((not isEmptyCell(fromPos)) or toPos.y != fromPos.y) \
        and canPieceMoveThere(piece, fromPos, toPos)

def moveMyPiece(piece, fromPos, toPos):
    """if the piece being taken over is a kind, the game is over
    regardless, move the piece"""
    print(f'frompos is {fromPos}, topos is {toPos}')
    toBeCaptured = pieceAt(toPos.x, toPos.y)
    gameOver = isKingPiece(toBeCaptured)

    assignToPieceAt(toPos.x, toPos.y, piece)
    removePieceAt(fromPos.x, fromPos.y)

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