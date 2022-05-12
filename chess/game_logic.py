from operator import pos
from tkinter import N
from chess.bishop import Bishop
from chess.castle import Castle
from chess.knight import Knight
from chess.pawn import Pawn


class GameLogic:

    def __init__(self):
        self.light_turn = True

    def get_legel_moves(self, piece, board, x, y):
        if type(piece) == int:
            return []

        if (self.light_turn and not piece.light) or \
           (not self.light_turn and piece.light):
           return []

        direction = -1 if piece.light else 1
        possible_moves = []

        if type(board.get_piece(x, y)) == Pawn:
            if not y == 0 or not y == 7:
                if type(board.get_piece(x, y + direction)) == int:
                    possible_moves.append((x, y + direction))

                if y == 1 and type(board.get_piece(x, y + 2 * direction)) == int and not piece.light:
                    possible_moves.append((x, y + 2 * direction))

                if y == 6 and type(board.get_piece(x, y + 2 * direction)) == int and piece.light:
                    possible_moves.append((x, y + 2 * direction))
                if not x == 0:
                    if not type(board.get_piece(x - 1, y + direction)) == int:
                        piece_two = board.get_piece(x - 1, y + direction)

                        if not piece_two.light == piece.light:
                            possible_moves.append((x - 1, y + direction))
                if not x == 7:
                    if not type(board.get_piece(x + 1, y + direction)) == int:
                        piece_two = board.get_piece(x + 1, y + direction)

                        if not piece_two.light == piece.light:
                            possible_moves.append((x + 1, y + direction))

        elif type(board.get_piece(x, y)) == Castle:

            # We are appending the possible moves
            # castle can make upwards
            if not y == 0:
                for cols in range(y - 1, -1, -1):
                    if type(board.get_piece(x, cols)) == int:
                        possible_moves.append((x, cols))
                    elif not board.get_piece(x, cols).light == piece.light:
                        # if there is an opposing piece,
                        # append the location and break the loop
                        possible_moves.append((x, cols))
                        break
                    else:
                        # break the loop as there is a friendly piece
                        break

            # Append possible moves that castle can make downwards
            if not y == 7:
                for cols in range(y + 1, 8):
                    if type(board.get_piece(x, cols)) == int:
                        possible_moves.append((x, cols))
                    elif not board.get_piece(x, cols).light == piece.light:
                        # if there is an opposing piece,
                        # append the location and break the loop
                        possible_moves.append((x, cols))
                        break
                    else:
                        # break the loop as there is a friendly piece
                        break

            if not x == 0:
                for rows in range(x - 1, -1, -1):
                    if type(board.get_piece(rows, y)) == int:
                        possible_moves.append((rows, y))
                    elif not board.get_piece(rows, y).light == piece.light:
                        # if there is an opposing piece,
                        # append the location and break the loop
                        possible_moves.append((rows, y))
                        break
                    else:
                        # break the loop as there is a friendly piece
                        break

            if not x == 1:
                for rows in range(x + 1, 8):
                    if type(board.get_piece(rows, y)) == int:
                        possible_moves.append((rows, y))
                    elif not board.get_piece(rows, y).light == piece.light:
                        # if there is an opposing piece,
                        # append the location and break the loop
                        possible_moves.append((rows, y))
                        break
                    else:
                        # break the loop as there is a friendly piece
                        break
        elif type(piece) == Knight:
                print("Knight was clicked")
                # for loop to iterate through values -2 to 2
                # these are the possible values we can add to the x-cord
                for i in range (-2, 3):
                    if i == 0:
                        continue # skip, as there is no possible movement where knight stays on the same axis
                    add_y = 1 if i % 2 == 0 else 2 
                    new_x = x + i

                    if 0 <= new_x < 8:
                        left_y = y - add_y
                        right_y = y + add_y

                        if left_y >= 0:
                            if type(board.get_piece(new_x, left_y)) == int or \
                                not board.get_piece(new_x, left_y).light == piece.light:
                                possible_moves.append((new_x, left_y))
                        if right_y < 8:
                            if type(board.get_piece(new_x, right_y)) == int or \
                                not board.get_piece(new_x, right_y).light == piece.light:
                                possible_moves.append((new_x, right_y))

        elif type(piece) == Bishop:

            # rightward
            if x < 7:
                # Two boolean variables to determine if another piece 
                # is blocking the bishops path
                # Break loop if both are false
                up, down = True, True                
                for new_x in range(x + 1, 8):
                    add_y = abs(x - new_x)
                    if up:
                        # y value decreases as we traverse up the board
                        new_y = y - add_y
                        if new_y >= 0:
                            if type(board.get_piece(new_x, new_y)) == int:
                                possible_moves.append((new_x, new_y))
                            elif not board.get_piece(new_x, new_y).light == piece.light:
                                possible_moves.append((new_x, new_y))
                                up = False
                            else:
                                up = False
                    if down:
                        # y value increase as we traverse down the board
                        new_y = y + add_y
                        if new_y <= 7:
                            if type(board.get_piece(new_x, new_y)) == int:
                                possible_moves.append((new_x, new_y))
                            elif not board.get_piece(new_x, new_y).light == piece.light:
                                possible_moves.append((new_x, new_y))
                                down = False
                            else:
                                down = False
            if x > 0:
                # Two boolean variables to determine if another piece 
                # is blocking the bishops path
                # Break loop if both are false
                up, down = True, True                
                for new_x in range(x, -1, -1):
                    add_y = abs(x - new_x)
                    if up:
                        # y value decreases as we traverse up the board
                        new_y = y - add_y
                        if new_y >= 0:
                            if type(board.get_piece(new_x, new_y)) == int:
                                possible_moves.append((new_x, new_y))
                            elif not board.get_piece(new_x, new_y).light == piece.light:
                                possible_moves.append((new_x, new_y))
                                up = False
                            else:
                                up = False
                    if down:
                        # y value increase as we traverse down the board
                        new_y = y + add_y
                        if new_y <= 7:
                            if type(board.get_piece(new_x, new_y)) == int:
                                possible_moves.append((new_x, new_y))
                            elif not board.get_piece(new_x, new_y).light == piece.light:
                                possible_moves.append((new_x, new_y))
                                down = False
                            else:
                                down = False
                
            
        return possible_moves
