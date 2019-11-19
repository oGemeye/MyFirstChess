from grid import pieceAt

def printBoard(board):
    printHeader()
    for x in range(8):
        printSider(x)
        for y in range(8):
            printFromBoard(board, x, y)
        print('')
        printHorizontalSection()

def printHeader():
    letters = ["1", "2", "3", "4", "5", "6", "7", "8"]
    print("-", end='')
    for x in range(8):
        print(f'-[{letters[x]}]-', end='')
    print("-")

def printSider(row):
    letters = ["A}", "B}", "C}", "D}", "E}", "F}", "G}", "H}"]
    print(letters[row], end='')

def printHorizontalSection():
    print("-", end='')
    for h in range(8):
        printCellBorder()
    print("-")

def printCellBorder():
    print("-----", end="")

def printFromBoard(board, x, y):
    pieceName = pieceAt(x, y)[1]
    func = pickPieceFromBoard(pieceName)
    func()

def pickPieceFromBoard(pieceName):
    switch = {
        'R': printRook,
        'Kn': printKnight,
        'B': printBishop,
        'Q': printQueen,
        'K': printKing,
        'P': printPawn,
        '': printBlank
    }
    return switch[pieceName]

def printRook():
    print(" R  |", end="")

def printKnight():
    print(" Kn |", end="")

def printBishop():
    print(" B  |", end="")

def printQueen():
    print(" Q  |", end="")

def printKing():
    print(" K  |", end="")

def printPawn():
    print(" P  |", end="")

def printBlank():
    print("    |", end="")