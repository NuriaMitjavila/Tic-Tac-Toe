# Game 1 vs 1
import random
import Game1vsAI

def end(board):
    for row in board:
        for item in row:
            if item == '□':
                return False
    return True

def start(board):
    player = random.choice(['x', 'o'])
    while True:
        print("Player", player, "turn")
        for row in board:
            for place in row:
                print(place, end=" ")
            print()
        a = True
        while a:
            try:
                position = int(input("Enter the position (1-9) to put in an empty space: "))
                print()
                if position not in range(1, 10):
                    print("Invalid number! Please choose a number between 1-9")
                row, column = (position-1) // 3, (position-1) % 3
                if board[row][column] != '□':
                    print("Invalid move! Please choose an empty space.")
                else:
                    board[row][column] = player
                    a = False
            except(KeyError, ValueError):
                print("Invalid input! Please enter a number between 1-9")

        if Game1vsAI.win(board, player):
            print("Player", player, "has win the game!!!")
            break
        if end(board):
            print("There is no winner!")
            break
        if player == 'x': player = 'o'
        else: player = 'x'
    for row in board:
        for place in row:
            print(place, end=" ")
        print()
