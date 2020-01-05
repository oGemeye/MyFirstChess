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
