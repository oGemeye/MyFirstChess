from moveValidator import addInBoundsCoord
from grid import pieceAt, positionInGrid

from math import sqrt

def canPieceMoveThere(piece, fromPos, toPos):
    """takes in an 8x8 board, a (Player, Type) piece, a (num, num) fromPos and toPos
    we assume that the toPos is empty on the board, and fromPos has our piece
    we could find this all out ourselves but look who cares"""
    pieceType = piece[1]
    pieceOrientation = getPieceOrientation(piece)
    legalMovesFunc = pieceMoveTypes(pieceType)
    legalMoves = legalMovesFunc(fromPos, toPos, pieceOrientation)
    return posInMoveset(toPos, legalMoves)

def posInMoveset(pos, moveset):
    return any(move.x == pos.x and move.y == pos.y for move in moveset)

def getPieceOrientation(piece):
    """declares what we add to a piece's X coord to create legal moves
    changes based on player"""
    if (piece[0] == "B"):
        return -1
    return 1

def pieceMoveTypes(pieceType):
    return {
        "R": calculateRookMoves,
        "Kn": calculateKnightMoves,
        "B": calculateBishopMoves,
        "Q": calculateQueenMoves,
        "K": calculateKingMoves,
        "P": calculatePrawnMoves
    }[pieceType]

def calculateRookMoves(fromPos, toPos, direction):
    legalMoves = []
    curX = fromPos.x
    curY = fromPos.y
    tempY = 0
    while curX >= 0 and tempY < 8:
        addInBoundsCoord(legalMoves, curX, tempY)
        tempY += 1

    tempX = 0
    while curY >= 0 and tempX < 8:
        addInBoundsCoord(legalMoves, tempX, curY)
        tempX += 1
    return legalMoves

def calculateKnightMoves(fromPos, toPos, direction):
    '''use the definition of a circle,
    with the knight's current position as the circle origin.
    If the potential position is on the perimeter
    of a radius sqrt(5) circle, then it's a valid knight move'''
    legalMoves = []
    curX = fromPos.x
    curY = fromPos.y

    for x in [curX-2, curX-1, curX+1, curX+2]:
        for y in [curY-2, curY-1, curY+1, curY+2]:
            originX = x-curX
            originY = y-curY
            if (originX**2) + (originY**2) == 5:
                addInBoundsCoord(legalMoves, x, y)

    return legalMoves

def calculateBishopMoves(fromPos, toPos, direction):
    legalMoves = []
    curX = fromPos.x
    curY = fromPos.y
    for i in range(1, 7):
        addInBoundsCoord(legalMoves, curX+i, curY+i)
        addInBoundsCoord(legalMoves, curX+i, curY-i)
        addInBoundsCoord(legalMoves, curX-i, curY+i)
        addInBoundsCoord(legalMoves, curX-i, curY-i)
    return legalMoves

def calculateQueenMoves(fromPos, toPos, direction):
    legalMoves = calculateRookMoves(fromPos, toPos, direction)
    legalMoves.extend(calculateBishopMoves(fromPos, toPos, direction))
    return legalMoves

def calculateKingMoves(fromPos, toPos, direction):
    legalMoves = calculateQueenMoves(fromPos, toPos, direction)
    kinglyMoves = [move for move in legalMoves if isOneAway(fromPos, move)]
    return kinglyMoves

def isOneAway(fro, to):
    toX = to[0]
    toY = to[1]
    fromX = fro[0]
    fromY = fro[1]
    return toX == fromX and toY == fromY+1 \
        or toX == fromX and toY == fromY-1 \
        or toY == fromY and toX == fromX+1 \
        or toY == fromY and toX == fromX-1

def calculatePrawnMoves(fromPos, toPos, direction):
    """TODO: include en passant and special diagonal pawn capture, and excluse pawn frontways capture"""
    legalMoves = []
    addInBoundsCoord(legalMoves, fromPos.x, fromPos.y + direction)
    return legalMoves