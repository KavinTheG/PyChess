from operator import pos
from chess.castle import Castle
from chess.pawn import Pawn


class GameLogic:
    def get_legel_moves(self, piece, board, x, y):
        if type(piece) == int:
            return 0

        direction = -1 if piece.light else 1
        possible_moves = []

        if type(board.get_piece(x, y)) == Pawn:
            if not y == 0 or not y == 7:
                if type(board.get_piece(x, y + direction)) == int:
                    possible_moves.append((x, y + direction))
                if not x == 0:
                    if not type(board.get_piece(x - 1, y + direction)) == int:
                        possible_moves.append((x - 1, y + direction))
                if not x == 7:
                    if not type(board.get_piece(x + 1, y + direction)) == int:
                        possible_moves.append((x + 1, y + direction))

        elif type(board.get_piece(x, y)) == Castle:

            # We are appending the possible moves
            # castle can make upwards
            if not y == 7:
                for cols in range(y + 1, 0, -1):
                    if type(board.get_piece(x, cols)) == int:
                        possible_moves.append(x, cols)
                    else:
                        # if there is a piece, break the loop
                        break

            # Append possible moves that castle can make downwards
            if not y == 0:
                for cols in range(y, 8):
                    if type(board.get_piece(x, cols)) == int:
                        possible_moves.append(x, cols)
                    else:
                        # if there is a piece, break the loop
                        break

            if not x == 0:
                for rows in range(x, 0, -1):
                    if type(board.get_piece(rows, y)) == int:
                        possible_moves.append(rows, y)
                    else:
                        # if there is a piece, break the loop
                        break

            if not x == 1:
                for rows in range(x, 8):
                    if type(board.get_piece(rows, y)) == int:
                        possible_moves.append(rows, y)
                    else:
                        # if there is a piece, break the loop
                        break

        return possible_moves
