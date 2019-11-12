from moveValidator import validInput, convertToCoord

def requestTurn(currentTurn, currentPlayerString):
    print(f'Turn {currentTurn}: {currentPlayerString}')

    confirmed = False
    while not confirmed:
        fromPos = getValidMove('Which piece would you like to move? ')
        toPos = getValidMove('Where would you like to move to? ')
        confirmed = confirmMoves(fromPos, toPos)

    return (fromPos, toPos)

def getValidMove(movePrompt):
    validMove = False
    while not validMove:
        move = input(movePrompt)
        parsedMove = parseMove(move)
        validMove = parsedMove[0]

        if (not validMove):
            print('That is not a valid command! Please move your pieces with a command like \'A3\'')
            print(f'Invalid command: {move[0]}, {move[1]}, {len(move)}')
    
    return parsedMove[1]

def parseMove(move):
    isValid = validInput(move)

    if (isValid):
        return (True, convertToCoord(move))
    else:
        return (False, None)

def confirmMoves(fromPos, toPos):
    confirmation = f'Are you sure you want to move the piece at {fromPos} to {toPos}? [Y/N] '
    response = input(confirmation)
    return response.upper() == 'Y' or response.upper() == 'YES'