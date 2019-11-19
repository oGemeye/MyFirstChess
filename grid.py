p1 = "B"
p2 = "R"
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

def pieceAt(x, y):
    return board[y][x]

def assignToPieceAt(x, y, piece):
    board[y][x] = piece

def removePieceAt(x, y):
    board[y][x] = blankPiece

def positionInGrid(x, y):
    return x <= 0 and y <= 0 and x < 8 and y < 8

def getBoard():
    return board