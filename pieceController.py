"""
controls pieces in an 8x8 board
top left coord is (x, y) = (0, 0) internally, A1 externally
top right coord is (x, y) = (0, 7) internally, A8 externally
bottom left coord is (x, y) = (7, 0) internally, H1 externally
bottom right coord is (x, y) = (7, 7) internally, H8 externally
"""

from pieceMove import canPieceMoveThere

p1 = "B"
p2 = "R"
currentPlayer = p1
board = [
        [[p2, "R"], [p2, "Kn"], [p2, "B"], [p2, "K"], [p2, "Q"], [p2, "B"], [p2, "Kn"], [p2, "R"]],
        [[p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"], [p2, "P"]],
        [0, 0, 0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0, 0, 0]
        [[p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], [p1, "P"], ]
        [[p1, "R"], [p1, "Kn"], [p1, "B"], [p1, "Q"], [p1, "K"], [p1, "B"], [p1, "Kn"], [p1, "R"]]
        ]

def movePiece(fromPosExternal, toPosExternal):
    """ fromPosExternal: (Letter, Number) coord where piece to move currently is
        toPos: (Letter, NUmber) coord where piece should be moved to
        returns false if fromPos doesnt have a piece, or it can't move to toPos"""

    if (!validCoord(fromPosExternal)
        or !validCoord(toPosExternal)
        or isSameCoord(fromPosExternal, toPosExternal)):
        return False
    
    fromPos = getNumCoord(fromPosExternal)
    toPos = getNumCoord(toPosExternal)

    if (isEmptyCell(fromPos)):
        return False
    
    moveMe = getPieceAtPos(fromPos)
    if (!isYourTurn(moveMe)):
        return False
    """at this point we know that a valid piece was chosen to be moved, now we find out if we can"""

    if (!isValidMove(moveMe, fromPos, toPos)):
        return False
    
    """we now know that the move is a valid one! Time to execute it"""
    

def validCoord(pos):
    if (pos[0] in ["A", "B", "C", "D", "E", "F", "G", "H"]
        and
        pos[1] in [1, 2, 3, 4, 5, 6, 7, 8]):
        return True
    return False

def isSameCoord(extPos1, extPos2):
    return extPos1[0] == extPos2[0]
            and extPos1[1] == extPos2[1]

def getNumCoord(pos):
    """converts (Letter, Number) pos into (num, num) coord
    A = 0, ..., H = 7"""
    x = ord(pos[0]) - 65
    y = pos[1] - 1
    return [x, y]

def getPieceAtPos(pos):
    return board[pos[0]][pos[1]]

def isEmptyCell(pos):
    """checks if the cell at x = pos[0], y = pos[1] is empty"""
    return getPieceAtPos(pos) == 0

def isYourTurn(piece):
    return piece[0] == currentPlayer

def isValidMove(piece, fromPos, toPos):
    return (isEmptyCell(toPos) or toPos[0] != fromPos[0])
        and canPieceMoveThere(board, piece, fromPos, toPos)