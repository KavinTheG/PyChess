from distutils.command.check import check
from matplotlib.pyplot import legend
import pygame

from .pawn import Pawn
from .castle import Castle
from .knight import Knight
from .bishop import Bishop
from .queen import Queen
from .king import King

DARK = (101, 67, 33)
LIGHT = (181, 101, 29)


class Board:
    def __init__(self, surface, size, dark, light, block_size):

        self.board = []
        self.surface = surface
        self.dark = dark
        self.light = light
        self.block_size = block_size

        self.check = False
        self.all_legal_moves = []

        # Save location of the kings to variable
        # Allows us to check if their location
        # coincides with the a legal movment of another piece
        self.light_king = [4, 7]
        self.dark_king = [4, 0]

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

                elif y == 2 or y == 5:
                    board_row.append(0)

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
        # print("draw_pieces called")
        for row in range(self.size):
            for col in range(self.size):
                if not type(self.board[row][col]) == int:
                    self.surface.blit(
                        self.board[row][col].sprite,
                        (self.board[row][col].rect_x, self.board[row][col].rect_y),
                    )

    def print_board_state(self):
        for row in range(self.size):
            print(self.board[row])

    def get_piece(self, x, y):
        return self.board[y][x]

    def move_piece(self, legal_moves, new_move, piece):
        new_move = tuple(new_move)

        for move in legal_moves:
            if move[0] == new_move[0] and move[1] == new_move[1]:
                print("New Move: " + str(new_move))

                old_coordinates = piece.get_board_pos()

                piece.set_new_pos(new_move[0], new_move[1])

                self.board[old_coordinates[1]][old_coordinates[0]] = 0
                self.board[new_move[1]][new_move[0]] = piece
                
                self.draw_board()
                self.draw_pieces()
                return True

        return False

    def move_king(self, king, legal_moves, new_move):

        illegal_moves = self.get_king_illegal_moves(king)

        # if the list below has any position in the illegal_movest list
        # remove it
        legal_moves = [i for i in legal_moves if list(i) not in illegal_moves]
        print("King Illegal Moves: " + str(illegal_moves))
        print("King Legal Moves: " + str(legal_moves))

        for move in legal_moves:
            if move[0] == new_move[0] and move[1] == new_move[1]:
                old_coordinates = self.light_king if king.light else self.dark_king

                king.set_new_pos(new_move[0], new_move[1])
                self.board[old_coordinates[1]][old_coordinates[0]] = 0
                self.board[new_move[1]][new_move[0]] = king

                if king.light:
                    self.light_king = new_move
                else:
                    self.dark_king = new_move

                self.draw_board()
                self.draw_pieces()
                return True
        return False

    def get_king_illegal_moves(self, king):
        king_pos = []
        illegal_moves = []
        # Determine if the piece is safe in each direction of the king
        directional_check = [None, None, None, 
                             None,       None, 
                             None, None, None]

        if king.light:
            king_pos = self.light_king
        else:
            king_pos = self.dark_king

        print("King Pos: " + str(king_pos))
        # Number of times we must circulate around the king
        # To check for possible checks (from Queen, Castle, Bishop)
        radius = (self.size - 1) - min(king_pos)     

        # Add 1 to inclue the last round in the for loop
        for r in range(1, radius + 1):
            index = 0
            for y_factor in range(-1, 2):
                # x +/- r. y +/- r -> diagonals
                # x, y +/- r -> up and down
                # x +/- r, y -> left and right

                for x_factor in range(-1, 2):
                    new_pos = [king_pos[0] + x_factor * r, king_pos[1] + y_factor * r]
                    
                    if new_pos[0] >= 0 and new_pos[0] < 8 and new_pos[1] >= 0 and new_pos[1] < 8:
                        print("Checking Pos: " + str(new_pos))
                        piece = self.get_piece(new_pos[0], new_pos[1])

                        if type(piece) == int or new_pos == king_pos \
                            or not directional_check[index] == None:
                            print(index)
                            index += 1 if not new_pos == king_pos else 0
                            continue
                        
                        print(piece)
                        # The line of code below checks if theres a piece with same colour, 
                        # The if statement above skips the loop if the direction 
                        # has no opposition/alliance piece
                        #directional_check[index] = not piece.light == king.light

                        if directional_check[index] == None:
                            if not piece.light == king.light:
                                print(str(piece) + "!")
                                if type(piece) == Queen or type(piece) == Castle or type(piece) == Bishop:
                                    print(str(piece) + "!!")
                                    directional_check[index] = True
                                    illegal_moves.append(
                                        [king_pos[0] + x_factor, king_pos[1] + y_factor]
                                    )
                                    illegal_moves.append(
                                        [king_pos[0] + x_factor * -1, king_pos[1] + y_factor * -1]
                                    )
                                else:
                                    if type(piece) == Pawn and not piece.light == king.light \
                                        and abs(x_factor) == abs(y_factor) and r == 1:
                                        # There is an opposite colour pawn within attack distance
                                        directional_check = True

                                    if not r == 1:
                                        directional_check[index] = False

                            else:
                                directional_check[index] = False

                    print("directional index: " + str(index)) 
                    index += 1
                    # for the directions the king cant move, I must gather 
                    # the root position, 1 square next to the king 
        print(directional_check)
        return illegal_moves



