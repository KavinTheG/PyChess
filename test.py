import random

board = []

board.append([])

for i in range(5):
    board[0].append(random.randint(1, 40))

board.append([])

l = [1, 2]

print(tuple(l) == l)
