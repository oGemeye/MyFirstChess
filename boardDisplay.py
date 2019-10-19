def printBoard():
    for x in range(8):
        printHorizontalSection()
        for y in range(8):
            printCellContent(x, y)
        print("|")
    
    printHorizontalSection()

def printHorizontalSection():
    for h in range(8):
        printCellBorder()
    print("-")

def piecePicker(y):
    """x is top to bottom, 0-7
    y is left to right, 0-7"""
    switch = {
        0: printRook,
        1: printKnight,
        2: printBishop,
        3: printQueen,
        4: printKing,
        5: printBishop,
        6: printKnight,
        7: printRook
    }

    return switch[y]()

#def pieceReader(y):

def printCellBorder():
    print("-----", end="")

def printCellContent(x, y):
    if x in [0, 7]:
        func = piecePicker(y)
        if func is not None:
            func()
    elif x in [1, 6]:
        printPawn()
    elif x in [2, 3, 4, 5]:
        print("|    ", end="")

def printRook():
    print("| R  ", end="")

def printKnight():
    print("| Kn ", end="")

def printBishop():
    print("| B  ", end="")

def printQueen():
    print("| Q  ", end="")

def printKing():
    print("| K  ", end="")

def printPawn():
    print("| P  ", end="")
