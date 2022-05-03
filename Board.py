from select import select


class Board:

    def __init__(self, size):

        # Initialize 2d array with all 0's
        self.board = [[0 for x in range(size)] for y in range(size)]

    def printBoardState(self):
        print(self.board)