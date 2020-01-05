from grid import positionInGrid, Coordinate

validLetters = ["A", "B", "C", "D", "E", "F", "G", "H"]
validNumbers = [1, 2, 3, 4, 5, 6, 7, 8]

def validCoord(pos :Command):
    if (pos.Letter in validLetters
        and
        pos.Number in validNumbers):
        return True
    return False

def validInput(move):
    '''Validates input straight from stdin'''
    return move[0] in validLetters and int(move[1]) in validNumbers and len(move) == 2

def convertToCoord(move):
    '''converts a sanitised move-request string
    into a tuple in the form (CHAR, INT)'''
    return Command(move[0], int(move[1]))

def getNumCoord(pos):
    """converts (Letter, Number) pos into (num, num) coord
    A = 0, ..., H = 7"""
    x = pos[1] - 1
    y = ord(pos[0].upper()) - 65
    return Coordinate(x, y)

class Command:
    '''
    A Command is created by a player
    It is basically the same as a Coordinate, but in the form
    (Letter, Number)
    The Letter represents the horizontal axis
    The Number represents the vertical axis
    '''
    Letter = ""
    Number = -1

    def __init__(self, x, y):
        self.Letter = x.upper()
        self.Number = y
    
    def __str__(self):
        return f'({self.Letter}, {self.Number})'