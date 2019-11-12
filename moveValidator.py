validLetters = ["A", "B", "C", "D", "E", "F", "G", "H"]
validNumbers = [1, 2, 3, 4, 5, 6, 7, 8]

def validCoord(pos):
    if (pos[0].upper() in validLetters
        and
        pos[1] in validNumbers):
        return True
    return False

def validInput(move):
    return move[0] in validLetters and int(move[1]) in validNumbers and len(move) == 2

def convertToCoord(move):
    '''converts a sanitised move-request string
    into a tuple in the form (CHAR, INT)'''
    return (move[0], int(move[1]))

def getNumCoord(pos):
    """converts (Letter, Number) pos into (num, num) coord
    A = 0, ..., H = 7"""
    x = pos[1] - 1
    y = ord(pos[0].upper()) - 65
    return Coordinate(x, y)

def addCoord(coordList, x, y):
    coordList.append([y, x])

class Coordinate:
    '''
    A Coordinate is defined as an (x, y) pair.
    The x value represents the horizontal axis
    The y value represents the vertical axis
    '''
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({x}, {y})'