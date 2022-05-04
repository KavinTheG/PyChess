import pygame
import Pieces.pawn
import Pieces.king
import Pieces.castle
import Pieces.knight
import Pieces.bishop
import Pieces.queen

DARK = (101, 67, 33)
LIGHT = (181, 101, 29)


class Board:
    def __init__(self, size):

        # Initialize 2d array with all 0's
        self.board = [[0 for x in range(size)] for y in range(size)]

        # Pawns
        self.dark_pawns = []
        self.light_pawns = []

        # Castle
        self.dark_castles = []
        self.light_castles = []

        # Knight
        self.dark_knights = []
        self.light_knights = []

        # Bishop
        self.dark_bishops = []
        self.light_bishops = []

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

                # if (x == 0 and y == 0) or (x == 0 and y == 7):

                if y == 1:
                    dark_pawn = Pieces.pawn.Pawn(False, self, blockSize)
                    dark_pawn.setPosition((x, y))

                    self.dark_pawns.append(dark_pawn)

                    surface.blit(
                        self.dark_pawns[x].returnSprite(),
                        (x * blockSize, blockSize * y),
                    )

                    self.board[y][x] = -5
                
                elif y == 6: 
                    light_pawn = Pieces.pawn.Pawn(True, self, blockSize)
                    light_pawn.setPosition((x, y))

                    self.light_pawns.append(light_pawn)

                    surface.blit(
                        self.light_pawns[x].returnSprite(),
                        (x * blockSize, blockSize * y),
                    )

                elif y == 0:
                    if x == 0:
                        dark_castle = Pieces.castle.Castle(False, self, blockSize)
                        dark_castle.setPosition((x, y))

                        self.dark_castles.append(dark_castle)
                        surface.blit(
                            self.dark_castles[0].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 1:
                        dark_knight = Pieces.knight.Knight(False, self, blockSize)
                        dark_knight.setPosition((x, y))

                        self.dark_knights.append(dark_knight)
                        surface.blit(
                            self.dark_knights[0].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 2:
                        dark_bishop = Pieces.bishop.Bishop(False, self, blockSize)
                        dark_bishop.setPosition((x, y))

                        self.dark_bishops.append(dark_bishop)
                        surface.blit(
                            self.dark_bishops[0].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 3:
                        self.dark_queen = Pieces.queen.Queen(False, self, blockSize)
                        self.board[y][x] = -25

                        surface.blit(
                            self.dark_queen.returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 4:
                        self.dark_king = Pieces.king.King(False, self, blockSize)
                        self.board[y][x] = -30

                        surface.blit(
                            self.dark_king.returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 5:
                        dark_bishop = Pieces.bishop.Bishop(False, self, blockSize)
                        dark_bishop.setPosition((x, y))

                        self.dark_bishops.append(dark_bishop)
                        surface.blit(
                            self.dark_bishops[1].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 6:
                        dark_knight = Pieces.knight.Knight(False, self, blockSize)
                        dark_knight.setPosition((x, y))

                        self.dark_knights.append(dark_knight)
                        surface.blit(
                            self.dark_knights[1].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 7:
                        dark_castle = Pieces.castle.Castle(False, self, blockSize)
                        dark_castle.setPosition((x, y))

                        self.dark_castles.append(dark_castle)
                        surface.blit(
                            self.dark_castles[1].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                elif y == 7:
                    if x == 0:
                        light_castle = Pieces.castle.Castle(True, self, blockSize)
                        light_castle.setPosition((x, y))

                        self.light_castles.append(light_castle)
                        surface.blit(
                            self.light_castles[0].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 1:
                        light_knight = Pieces.knight.Knight(True, self, blockSize)
                        light_knight.setPosition((x, y))

                        self.light_knights.append(light_knight)
                        surface.blit(
                            self.light_knights[0].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 2:
                        light_bishop = Pieces.bishop.Bishop(True, self, blockSize)
                        light_bishop.setPosition((x, y))

                        self.light_bishops.append(light_bishop)
                        surface.blit(
                            self.light_bishops[0].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 3:
                        self.light_queen = Pieces.queen.Queen(True, self, blockSize)
                        self.board[y][x] = 25

                        surface.blit(
                            self.light_queen.returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 4:
                        self.light_king = Pieces.king.King(True, self, blockSize)
                        self.board[y][x] = 30

                        surface.blit(
                            self.light_king.returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 5:
                        light_bishop = Pieces.bishop.Bishop(True, self, blockSize)
                        light_bishop.setPosition((x, y))

                        self.light_bishops.append(light_bishop)
                        surface.blit(
                            self.light_bishops[1].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 6:
                        light_knight = Pieces.knight.Knight(True, self, blockSize)
                        light_knight.setPosition((x, y))

                        self.light_knights.append(light_knight)
                        surface.blit(
                            self.light_knights[1].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

                    if x == 7:
                        light_castle = Pieces.castle.Castle(True, self, blockSize)
                        light_castle.setPosition((x, y))

                        self.light_castles.append(light_castle)
                        surface.blit(
                            self.light_castles[1].returnSprite(),
                            (x * blockSize, blockSize * y),
                        )

    def printBoardArray(self):

        for row in self.board:
            print(row)
