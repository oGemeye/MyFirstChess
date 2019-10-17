blank = ["" for x in range(8)]
horizontal = blank
vertical = [blank for x in range(8)]

def initBoard(board):
    for y in range(8):
        for x in range(8):
            if y in [0, 7]:
                board[x][y] = " o "
            elif y in [1, 6]:
                board[x][y] = " p "
            elif y in [2, 3, 4, 5]:
                board[x][y] = " _ "
    return board

def printBoard(board):
    for y in range(8):
        for x in range(8):
            print(board[x][y], end="")
        print("")
    print("")

board = initBoard(vertical)
#printBoard(board)