from distutils.command.check import check
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

        self.pinned_pieces = []

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

        if piece in self.pinned_pieces:
            return False

        for move in legal_moves:
            if move[0] == new_move[0] and move[1] == new_move[1]:
                print("New Move: " + str(new_move))

                old_coordinates = piece.get_board_pos()

                piece.set_new_pos(new_move[0], new_move[1])

                self.board[old_coordinates[1]][old_coordinates[0]] = 0
                self.board[new_move[1]][new_move[0]] = piece

                self.update_pins(not piece.light)

                print("New Pinned Pieces: " + str(self.pinned_pieces))

                self.draw_board()
                self.draw_pieces()
                return True

        return False

    def move_king(self, king, legal_moves, new_move):

        # legal_moves = self.get_king_legal_moves(king)

        print("King Legal Moves: " + str(legal_moves))

        for move in legal_moves:
            if move[0] == new_move[0] and move[1] == new_move[1]:
                if self.is_king_move_legal(king, new_move):

                    old_coordinates = self.light_king if king.light else self.dark_king

                    king.set_new_pos(new_move[0], new_move[1])
                    self.board[old_coordinates[1]][old_coordinates[0]] = 0
                    self.board[new_move[1]][new_move[0]] = king

                    if king.light:
                        self.light_king = new_move
                    else:
                        self.dark_king = new_move

                    self.update_pins(not king.light)
                    self.draw_board()
                    self.draw_pieces()
                    print("Pinned Pieces: " + str(self.pinned_pieces))
                    return True
        print("Move_King returns false")
        return False

    # TODO: makes pinned pieces
    # These pieces cant move because it'll cause a check
    def is_king_move_legal(self, king, king_pos):

        current_pos = self.light_king if king.light else self.dark_king
        # Travel outwards radially in each direction
        direction = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]

        # Variable to store minimum number of times to travel outwards
        min_radius = 7 - min(king_pos) if min(king_pos) <= 3 else min(king_pos)

        for dir_index in range(len(direction)):

            root_dir = direction[dir_index]

            # Variable to remember pinned piece radius
            pinPieceRadius = 0

            # Variable to check if an enemy was detected
            attacker = False

            diagonal_index = [0, 2, 5, 7]

            for r in range(1, min_radius + 1):
                new_dir = [king_pos[0] + r * root_dir[0], king_pos[1] + r * root_dir[1]]

                print(new_dir)

                # Skip the current position
                if current_pos == new_dir:
                    continue

                if 0 <= new_dir[0] < 8 and 0 <= new_dir[1] < 8:
                    piece = self.get_piece(new_dir[0], new_dir[1])

                    if not type(piece) == int:
                        print(piece)

                        # ALliance Piece
                        if piece.light == king.light:
                            print("Alliance")
                            print("Direction Index: " + str(dir_index))
                            # If statement to check if no alliance piece was detect so far
                            # Also checks if no enemy piece was already met so far
                            if pinPieceRadius == 0 and not attacker:
                                pinPieceRadius = r
                            elif not pinPieceRadius == 0 and not attacker:
                                pinPieceRadius = -1

                        # Enemy piece
                        else:
                            print("Enemy")
                            print("Direction Index: " + str(dir_index))
                            # Only Queen and Bishop can effect king in this direction
                            # print('dir_index == (0 or 2 or 5 or 7): ' + str(bool(dir_index == 0 or 2 or 5 or 7)))
                            if dir_index in diagonal_index:
                                if type(piece) == Bishop or type(piece) == Queen:

                                    print(
                                        "This piece ( "
                                        + str(piece)
                                        + ") is potentially harmful"
                                    )
                                else:
                                    print(
                                        "This piece is harmless -> Piece: "
                                        + str(piece)
                                        + ", dir-index: "
                                        + str(dir_index)
                                    )
                                    print(
                                        "Status of conditions:"
                                        + str(bool(dir_index == 0 or 2 or 5 or 7))
                                        + ", "
                                        + str(not (type(piece) == Bishop or Queen))
                                    )

                                    # Pin piece functionality
                                    pinPieceRadius = r
                                    continue
                            # Only Queen and Castle can effect king in this direction
                            else:
                                if type(piece) == Castle or type(piece) == Queen:
                                    print(
                                        "This piece ("
                                        + str(piece)
                                        + ") is potentially harmful"
                                    )
                                else:
                                    print(
                                        "This piece is harmless -> Piece: "
                                        + str(piece)
                                        + ", dir-index: "
                                        + str(dir_index)
                                    )
                                    print(
                                        "Status of conditions:"
                                        + str(bool(dir_index == 0 or 2 or 5 or 7))
                                        + ", "
                                        + str(not (type(piece) == Castle or Queen))
                                    )

                                    pinPieceRadius = r

                                    continue

                            print("pinned piece: " + str(pinPieceRadius))

                            # If statement to check if there is any alliance piece detected already
                            # No alliance piece so far, this is an 'immediate enemy'
                            if pinPieceRadius == 0:
                                print("Immediate enemy: " + str(new_dir))
                                return False

        return True

    # Call this method after moving any piece
    # These are pieces that can't be moved
    # Otherwise, it will cause a check
    def update_pins(self, light):

        king_pos = self.light_king if light else self.dark_king

        # Clear pins
        self.pinned_pieces = []

        direction = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]

        # Variable to store minimum number of times to travel outwards
        min_radius = 7 - min(king_pos) if min(king_pos) <= 3 else min(king_pos)

        for dir_index in range(len(direction)):

            root_dir = direction[dir_index]

            # Variable to remember pinned piece radius
            pinPieceRadius = 0

            # Variable to check if an enemy was detected
            attacker = False

            diagonal_index = [0, 2, 5, 7]

            for r in range(1, min_radius + 1):
                new_dir = [king_pos[0] + r * root_dir[0], king_pos[1] + r * root_dir[1]]

                # Skip the current position
                if king_pos == new_dir:
                    continue

                if 0 <= new_dir[0] < 8 and 0 <= new_dir[1] < 8:
                    piece = self.get_piece(new_dir[0], new_dir[1])

                    if not type(piece) == int:
                        if piece.light == light:

                            # No alliance piece met so far
                            if pinPieceRadius == 0:
                                pinPieceRadius = r
                            elif not pinPieceRadius == 0 and not attacker:
                                # Two or more consecutive alliance piece
                                # Thus, no pin pieces in this direction
                                continue

                        else:

                            # This is an immediate attacker
                            # Thus, there is no pinned pieces in this direction

                            if (
                                dir_index in diagonal_index
                                and type(piece) == Bishop
                                or type(piece) == Queen
                            ) or (
                                not dir_index in diagonal_index
                                and type(piece) == Castle
                                or type(piece) == Queen
                            ):
                                if pinPieceRadius == 0:
                                    continue
                                else:
                                    attacker = True
            if attacker:
                self.pinned_pieces.append(
                    self.get_piece(
                        king_pos[0] + pinPieceRadius * root_dir[0],
                        king_pos[1] + pinPieceRadius * root_dir[1],
                    )
                )
