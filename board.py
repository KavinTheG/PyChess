import pygame
import Classes.pawn

DARK = (101, 67, 33)
LIGHT = (181, 101, 29)


class Board:
    def __init__(self, size):

        # Initialize 2d array with all 0's
        self.board = [[0 for x in range(size)] for y in range(size)]
        self.dark_pawns = []

        self.size = size

    def drawBoard(self, surface, dark, light, blockSize):

        size = self.size

        for y in range(size):
            for x in range(size):
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)

                if x % 2 == y % 2:
                    pygame.draw.rect(surface, dark, rect)
                else:
                    pygame.draw.rect(surface, light, rect)

                if y == 1:
                    self.dark_pawns.append(Classes.pawn.Pawn(False, (x, y), self, blockSize))
                    surface.blit(self.dark_pawns[x].returnSprite(), (x * blockSize, blockSize * y))

    def printBoardArray(self):

        for row in self.board:
            print(row)
