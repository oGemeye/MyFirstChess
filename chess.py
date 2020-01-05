from playerIO import requestTurn
from pieceController import movePiece, getCurrentTurn, getCurrentPlayerString, isGameOver
from grid import getBoard
from boardDisplay import printBoard

log = []

print("This is my game board :)")

def doATurnAndCheckGameOver():
    turnDone = False
    while not turnDone:
        nextMove = requestTurn(getCurrentTurn(), getCurrentPlayerString())
        turnDone = movePiece(nextMove[0], nextMove[1])
    
    logAndReportMove(nextMove[0], nextMove[1])
    printBoard(getBoard())
    return isGameOver()

def logAndReportMove(fromPos, toPos):
    turn = getCurrentTurn()
    player = getCurrentPlayerString()
    newLog = f'T{turn}, {player}: {fromPos} -> {toPos}'
    print(newLog)
    logMove(newLog)

    if (isGameOver()):
        reportGameOver()

def reportGameOver():
    newLog = f'Game Over! {getCurrentPlayerString()} won! :D'
    print(newLog)
    logMove(newLog)

def logMove(newLog):
    log.append(newLog)

printBoard(getBoard())
gameOver = False
while not gameOver:
    try:
        gameOver = doATurnAndCheckGameOver()
    except KeyboardInterrupt:
        break
    except:
        raise