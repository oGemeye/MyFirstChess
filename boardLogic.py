from pieceLogic import Piece, Coordinate

p1 = "B"
p2 = "R"
blankPiece = [None]
backRowArray = ['R', 'Kn', 'B', 'Q', 'K', 'B', 'Kn', 'R']

'''
p1 starts with pieces at [0, Y], that change by +1 X for each new piece
p1's backrow is at [X, 7], and its frontrow is at [X, 6]
'''
initPlayerPieces(p1, 0, 1, 7, 6)

'''
p2 starts with pieces at [7, Y], that change by -1 X for each new piece
p2's backrow is at [X, 0], and its frontrow is at [X, 1]
'''
initPlayerPieces(p2, 7, -1, 1, 2)

board = [
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        [blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece, blankPiece],
        ]

def initPlayerPieces(player, startingX, deltaX, backRowY, frontRowY):
    '''Initialises pieces for a player
    Requires Y rows to allow decoupled piece initialisation
    Also requires startingX and delta to move from that X'''
    x = startingX
    pawnMovesFunc = pieceMoveTypes('P')

    for i in range(8):
        pieceID = backRowArray[i]
        newBackrow = Piece(pieceID, player, Coordinate(x, backRowY), pieceMoveTypes(pieceID))
        newPawn = Piece('P', player, Coordinate(x, frontRowY), pawnMovesFunc)

        assignToPieceAt(newBackrow)
        assignToPieceAt(newPawn)
        x += deltaX

def pieceAt(x, y):
    return board[y][x]

def assignToPieceAt(x, y, piece):
    board[y][x] = piece

def assignToPieceAt(piece: Piece):
    assignToPieceAt(piece.position.x, piece.position.y, piece)

def removePieceAt(x, y):
    board[y][x] = blankPiece

def positionInGrid(x, y):
    return x >= 0 and y >= 0 and x < 8 and y < 8

def positionInGrid(pos :Coordinate):
    return positionInGrid(pos.x, pos.y)

def getBoard():
    return board

def getTopPlayer():
    return p2

def getBottomPlayer():
    return p1

'''The following is logic related to where pieces can move
Altho this sounds like it should go into pieceLogic,
it makes more sense here, as piece logic is dependent upon the boardstate
for example (and crucially), board boundaries'''

def pieceMoveTypes(pieceType):
    return {
        "R": calculateRookMoves,
        "Kn": calculateKnightMoves,
        "B": calculateBishopMoves,
        "Q": calculateQueenMoves,
        "K": calculateKingMoves,
        "P": calculatePrawnMoves
    }[pieceType]

def calculateRookMoves(fromPos :Coordinate, direction):
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

def calculateKnightMoves(fromPos :Coordinate, direction):
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

def calculateBishopMoves(fromPos :Coordinate, direction):
    legalMoves = []
    curX = fromPos.x
    curY = fromPos.y
    for i in range(1, 7):
        addInBoundsCoord(legalMoves, curX+i, curY+i)
        addInBoundsCoord(legalMoves, curX+i, curY-i)
        addInBoundsCoord(legalMoves, curX-i, curY+i)
        addInBoundsCoord(legalMoves, curX-i, curY-i)
    return legalMoves

def calculateQueenMoves(fromPos :Coordinate, direction):
    legalMoves = calculateRookMoves(fromPos, direction)
    legalMoves.extend(calculateBishopMoves(fromPos, direction))
    return legalMoves

def calculateKingMoves(fromPos :Coordinate, direction):
    legalMoves = calculateQueenMoves(fromPos, direction)
    kinglyMoves = [move for move in legalMoves if isOneAway(fromPos, move)]
    return kinglyMoves

def isOneAway(fro  :Coordinate, to :Coordinate):
    return to.x == fro.x and to.y == fro.y+1 \
        or to.x == fro.x and to.y == fro.y-1 \
        or to.y == fro.y and to.x == fro.x+1 \
        or to.y == fro.y and to.x == fro.x-1

def calculatePrawnMoves(fromPos :Coordinate, direction):
    """TODO: include en passant and special diagonal pawn capture, and exclude pawn frontways capture"""
    legalMoves = []
    addInBoundsCoord(legalMoves, fromPos.x, fromPos.y + direction)
    return legalMoves

def addInBoundsCoord(coordList, x, y):
    if positionInGridToRemove(x, y):
        coordList.append(Coordinate(x, y))

def positionInGridToRemove(x, y):
    return x >= 0 and y >= 0 and x < 8 and y < 8
