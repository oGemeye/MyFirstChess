def canPieceMoveThere(board, piece, fromPos, toPos):
    """takes in an 8x8 board, a (Player, Type) piece, a (num, num) fromPos and toPos
    we assume that the toPos is empty on the board, and fromPos has our piece
    we could find this all out ourselves but look who cares"""
    pieceType = piece[1]
    pieceOrientation = getPieceOrientation(piece)
    legalMovesFunc = pieceMoveTypes(pieceType)

    legalMoves = legalMovesFunc(fromPos, toPos, pieceOrientation)
    return toPos in legalMoves

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
    curX = fromPos[0]
    curY = fromPos[1]
    tempY = 0
    while curX >= 0 and tempY < 8:
        legalMoves.append([curX, tempY])
        tempY += 1

    tempX = 0
    while curY >= 0 and tempX < 8:
        legalMoves.append([tempX, curY])
        tempX += 1

    return getMovesOnBoard(legalMoves)

def calculateKnightMoves(fromPos, toPos, direction):
    """TODO: write this algo to be intelligent instead of just listing the 8 possible transforms"""
    legalMoves = []
    curX = fromPos[0]
    curY = fromPos[1]

    legalMoves.append([curX+1, curY-2])
    legalMoves.append([curX+2, curY-1])

    legalMoves.append([curX+2, curY+1])
    legalMoves.append([curX+1, curY+2])

    legalMoves.append([curX-1, curY+2])
    legalMoves.append([curX-2, curY+1])

    legalMoves.append([curX-2, curY-1])
    legalMoves.append([curX-1, curY-2])

    return getMovesOnBoard(legalMoves)

def calculateBishopMoves(fromPos, toPos, direction):
    legalMoves = []
    curX = fromPos[0]
    curY = fromPos[1]
    for x in range(start=1, stop=7):
        legalMoves.append([curX+x, curY+x])
        legalMoves.append([curX+x, curY-x])
        legalMoves.append([curX-x, curY+x])
        legalMoves.append([curX-x, curY-x])

    return getMovesOnBoard(legalMoves)

def calculateQueenMoves(fromPos, toPos, direction):
    legalMoves = calculateRookMoves(fromPos, toPos, direction)
    legalMoves.append(calculateBishopMoves(fromPos, toPos, direction))
    return getMovesOnBoard(legalMoves)

def calculateKingMoves(fromPos, toPos, direction):
    legalMoves = calculateQueenMoves(fromPos, toPos, direction)
    kinglyMoves = [move for move in legalMoves if isOneAway(fromPos, move)]
    return getMovesOnBoard(kinglyMoves)

def calculatePrawnMoves(fromPos, toPos, direction):
    """TODO: include en passant and special diagonal pawn capture, and excluse pawn frontways capture"""
    legalMoves = []
    legalMoves.append([fromPos[0] + direction, fromPos[1]])
    return legalMoves

def getMovesOnBoard(moveSet):
    return [move for move in legalMoves if posIsOnBoard(move)]

def posIsOnBoard(pos):
    return pos[0] <= 0 and pos[1] <= 0 and pos[0] < 8 and pos[1] < 8

def isOneAway(fro, to):
    toX = to[0]
    toY = to[1]
    fromX = fro[0]
    fromY = fro[1]
    return toX == fromX and toY == fromY+1 \
        or toX == fromX and toY == fromY-1 \
        or toY == fromY and toX == fromX+1 \
        or toY == fromY and toX == fromX-1