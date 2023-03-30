# Tic-Tac-Toe Game
import Game1vsAI
import Game1vs1

print("You want to play tic-tac-toe with a human or a machine?")
print("1. Human")
print("2. Machine")
option = input()
print()
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append('□')
    board.append(row)

if option == "1":
    Game1vs1.start(board)
elif option == "2":
    Game1vsAI.start(board)
else:
    print("Invalid option!! ", end='')
