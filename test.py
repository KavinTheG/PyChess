import random

board = []

board.append([])

for i in range(5):
    board[0].append(random.randint(1, 40))

board.append([])

for i in range(5):
    board[1].append(random.randint(1, 40))

for new_x in range(5, 0, -1):
    print(new_x)
