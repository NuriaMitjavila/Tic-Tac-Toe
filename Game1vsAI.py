# Game 1 vs AI
import random

def Gameboard(board):
    symbols = {1: 'x', -1: 'o', 0: '□'}
    for row in board:
        for cell in row:
            print(symbols[cell], end=' ')
        print()
    print()

def win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True        

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def blanks(board):
    blank = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if board[x][y] == 0:
                blank.append([x, y])
    return blank

def minimax(board, length, a, b, player):
    row = -1
    col = -1
    if length == 0 or (win(board, 1) or win(board, -1)):
        if win(board, -1):
            return row, col, -10
        elif win(board, 1):
            return row, col, 10
        else:
            return row, col, 0
    else:
        for cell in blanks(board):
            board[cell[0]][cell[1]] = player
            score = minimax(board, length - 1, a, b, -player)
            if player == -1:
                if score[2] < b:
                    b, row, col = score[2], cell[0], cell[1]
            else:
                if score[2] > a:
                    a, row, col = score[2], cell[0], cell[1]            
            board[cell[0]][cell[1]] = 0
            if a >= b:
                break
        if player == 1:
            return row, col, a
        else:
            return row, col, b

def start(board):
    player = 'x'
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            board[x][y] = 0
    
    if player == 'o':
        print("It's the IA turn")

    while not (len(blanks(board)) == 0 or (win(board, 1) or win(board, -1))):
        if player == 'x':
            a = True
            while a:
                try:
                    position = int(input('Is your turn, enter a number between 1-9: '))
                    row, column = (position-1) // 3, (position-1) % 3
                    if position not in range(1, 10):
                        print("Invalid number! Please choose a number between 1-9")
                    elif not ([row, column] in blanks(board)):
                        print('Invalid Move! Try again!')
                    else:
                        board[row][column] = 1
                        Gameboard(board)
                        a = False
                except(KeyError, ValueError):
                    print('Invalid input! Please enter a number between 1-9')
            
        else:
            if len(blanks(board)) == 9:
                board[random.choice([0, 1, 2])][random.choice([0, 1, 2])] = -1
                Gameboard(board)
            else:
                result = minimax(board, len(blanks(board)), -10**9, 10**9, -1)
                board[result[0]][result[1]] = -1
                Gameboard(board)
    
        if player == 'x': player = 'o'
        else: player = 'x'

    if win(board, 1):
        print('Player x has win the game!!!')
    elif win(board, -1):
        print('Player o has win the game!!!')
    else:
        print('There is no winner!')
