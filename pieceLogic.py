'''PieceLogic.py: file to contain all logic pertaining to how pieces are initialised and used'''

class Piece:
    '''
    A Piece is a chess piece on a board.
    It can be initialised with any designation
    It has a player it belongs to
    It tracks the number of times it's moved
    It has a position coordinate
    It has a function that determines legal moves
    '''
    kind = ""
    player = ""
    movedCount = 0
    position = Coordinate()
    movesFunc = None

    def __init__(self, kind, player, position: Coordinate, movesFunc):
        self.kind = kind
        self.player = player
        self.position = position
    
    def __str__(self):
        return f'({self.kind}, owned by {self.player} at {self.position}, moved {self.movedCount} times)'
    
    def getMoves(self):
        return movesFunc(self.position, getPieceOrientation(self))

    def getPieceOrientation(self):
        '''determine's the direction this piece wants to move in'''
        if (self.player == "B"):
            return -1
        return 1

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
        return f'({self.x}, {self.y})'