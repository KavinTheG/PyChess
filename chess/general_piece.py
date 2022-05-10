class GeneralPiece:
    def __init__(self, x, y, light, block_size):

        # boolean value to determine if peice is dark/light
        self.light = light

        # boolean value to determine if peice is alive
        self.alive = True

        self.x = x
        self.y = y

        self.block_size = block_size
        
    def isdigit(self):
        return False