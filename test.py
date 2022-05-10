import random

board = []

board.append([])

for i in range(5):
    board[0].append(random.randint(1, 40))

board.append([])

for i in range(5):
    board[1].append(random.randint(1, 40))

for i in range(len(board)):
    print(board[i])
print(board[0][2])
