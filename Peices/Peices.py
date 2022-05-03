class Peices:

    def __init__(self, light, position, board):

        # Variable to store current position of peice
        self.position = position

        # boolean value to determine if peice is dark/light
        self.light = light

        # Allows peices to know where other peices are
        self.board = board


    def getPosition(self):
        return self.position