class GeneralBehaviour:
    def __init__(self, light, board, blockSize):

        # boolean value to determine if peice is dark/light
        self.light = light

        # boolean value to determine if peice is alive
        self.alive = True

        # Allows peices to know where other peices are
        self.board = board

        self.blockSize = blockSize

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position
