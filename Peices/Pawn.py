import Peices

class Pawn(Peices):

    def __init__(self):
        super().__init()
        

    def legalMove(self):
        
        # It's dark peice
        currentPos = self.position
        if self.light:
            newPos = (currentPos[0], currentPos[1] + 1)        

        return newPos