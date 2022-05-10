import pygame
from chess.general_piece import GeneralPiece

from chess.pawn import Pawn
from chess.castle import Castle
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King

DARK = (101, 67, 33)
LIGHT = (181, 101, 29)


class Board:
    def __init__(self, surface, size, dark, light, block_size):

        self.board = []
        self.surface = surface
        self.dark = dark
        self.light = light
        self.block_size = block_size

        # Goes throug the y-axis downwards
        for y in range(size):
            # Initialize empty list for each row
            # Append it to variable board at end of for loop
            board_row = []

            # Goes through the x-axis rightwards
            for x in range(size):
                if y == 0:
                    if x == 0 or x == 7:
                        dark_castle = Castle(x, y, False, block_size)
                        board_row.append(dark_castle)
                    elif x == 1 or x == 6:
                        dark_knight = Knight(x, y, False, block_size)
                        board_row.append(dark_knight)
                    elif x == 2 or x == 5:
                        dark_bishop = Bishop(x, y, False, block_size)
                        board_row.append(dark_bishop)
                    elif x == 3:
                        dark_queen = Queen(x, y, False, block_size)
                        board_row.append(dark_queen)
                    else:
                        dark_king = King(x, y, False, block_size)
                        board_row.append(dark_king)

                elif y == 1:
                    dark_pawn = Pawn(x, y, False, block_size)
                    board_row.append(dark_pawn)

                elif y == 6:
                    light_pawn = Pawn(x, y, True, block_size)
                    board_row.append(light_pawn)

                elif y == 7:
                    if x == 0 or x == 7:
                        light_castle = Castle(x, y, True, block_size)
                        board_row.append(light_castle)
                    elif x == 1 or x == 6:
                        light_knight = Knight(x, y, True, block_size)
                        board_row.append(light_knight)
                    elif x == 2 or x == 5:
                        light_bishop = Bishop(x, y, True, block_size)
                        board_row.append(light_bishop)
                    elif x == 3:
                        light_queen = Queen(x, y, True, block_size)
                        board_row.append(light_queen)
                    else:
                        light_king = King(x, y, True, block_size)
                        board_row.append(light_king)

                else:
                    board_row.append(0)
            self.board.append(board_row)

        self.size = size

        self.draw_board()
        self.draw_pieces()

        # print(self.board[0][3])

    def draw_board(self):

        size = self.size

        for y in range(size):
            for x in range(size):
                rect = pygame.Rect(
                    x * self.block_size,
                    y * self.block_size,
                    self.block_size,
                    self.block_size,
                )

                if x % 2 == y % 2:
                    pygame.draw.rect(self.surface, self.light, rect)
                else:
                    pygame.draw.rect(self.surface, self.dark, rect)

    def draw_pieces(self):
        for row in self.board:
            for item in row:
                if not type(item) == int:
                    self.surface.blit(item.sprite, (item.rect.x, item.rect.y))

    def print_board_state(self):
        for row in self.board:
            print(row)

    def get_piece(self, x, y):
        return self.board[y][x]
