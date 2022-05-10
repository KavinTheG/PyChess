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
    def __init__(self, surface, size, dark, light,  block_size):

        self.board = []
        self.surface = surface    
        self.dark = dark
        self.light = light
        self.block_size = block_size
    

        # Goes throug the y-axis downwards
        for i in range(size):
            # Initialize empty list for each row
            # Append it to variable board at end of for loop
            board_row = []

            # Goes through the x-axis rightwards
            for j in range(size):
                if i == 0:
                    if j == 0 or j == 7:
                        dark_castle = Castle(j, i, False, block_size)
                        board_row.append(dark_castle)
                    elif j == 1 or j == 6:
                        dark_knight = Knight(j, i, False, block_size)
                        board_row.append(dark_knight)
                    elif j == 2 or j == 5:
                        dark_bishop = Bishop(j, i, False, block_size)
                        board_row.append(dark_bishop)
                    elif j == 3:
                        dark_queen = Queen(j, i, False, block_size)
                        board_row.append(dark_queen)
                    else:
                        dark_king = King(j, i, False, block_size)
                        board_row.append(dark_king)

                elif i == 1: 
                    dark_pawn = Pawn(j, i, False, block_size)
                    board_row.append(dark_pawn)

                elif i == 6:
                    light_pawn = Pawn(j, i, True, block_size)
                    board_row.append(light_pawn)

                elif i == 7:
                    if j == 0 or j == 7:
                        light_castle = Castle(j, i, True, block_size)
                        board_row.append(light_castle)
                    elif j == 1 or j == 6:
                        light_knight = Knight(j, i, True, block_size)
                        board_row.append(light_knight)
                    elif j == 2 or j == 5:
                        light_bishop = Bishop(j, i, True, block_size)
                        board_row.append(light_bishop)
                    elif j == 3:
                        light_queen = Queen(j, i, True, block_size)
                        board_row.append(light_queen)
                    else:
                        light_king = King(j, i, True, block_size)
                        board_row.append(light_king)

                else:
                    board_row.append(0)
            self.board.append(board_row)

        self.size = size

        self.draw_board()
        self.draw_pieces()

        print(self.board[0][3])

    def draw_board(self):

        size = self.size

        for y in range(size):
            for x in range(size):
                rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)

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


    def get_piece(self, row, col):
        return self.board[col][row]

