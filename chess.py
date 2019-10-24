from pieceController import board, movePiece
from boardDisplay import printBoard

print("This is my game board :)")

printBoard(board)

print("Mock turn 1, Blue, G1 to F1")

didMove = movePiece(["G", 1], ["F", 1])

print(f"Moved?: {didMove}")
printBoard(board)