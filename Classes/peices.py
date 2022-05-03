class Peices:
    def __init__(self, light, position, board, blockSize):

        # Variable to store current position of peice
        self.position = position

        # boolean value to determine if peice is dark/light
        self.light = light

        # boolean value to determine if peice is alive
        self.alive = True

        # Allows peices to know where other peices are
        self.board = board

        self.blockSize = blockSize

    def getPosition(self):
        return self.position
