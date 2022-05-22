from hmac import new
import sys
import pygame
from chess.board import Board
from chess.game_logic import GameLogic
from chess.king import King

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

DARK = (101, 67, 33)
LIGHT = (181, 101, 29)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

# Chess board size (8 by 8)
SIZE = 8
BLOCKSIZE = (int)(WINDOW_WIDTH / SIZE)


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    b = Board(SCREEN, 8, DARK, LIGHT, BLOCKSIZE)
    #b.print_board_state()
    game = GameLogic()

    # List to store moves allowed by player (if player clicked on a piece)
    current_legal_moves = []
    # Determines if a piece was clicked
    selected_piece = False
    # Store the selected piece
    piece = None

    light_king = [4, 7]
    dark_king = [4, 0]

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coordinates = [i // BLOCKSIZE for i in pygame.mouse.get_pos()]
                if not selected_piece:
                    piece = b.get_piece(coordinates[0], coordinates[1])

                    # set variable to true if a chess piece was clicked
                    selected_piece = not type(piece) == int
                    current_legal_moves = game.get_legel_moves(
                        piece, b, coordinates[0], coordinates[1]
                    )
                    #print(current_legal_moves)

                else:

                    # At the previous click, a piece was selected
                    # Therefore this click determines the move of the piece

                    #if type(piece) == King:
                    #    piece_moved = b.move_piece(current_legal_moves, coordinates, piece)
                    #else:
                    piece_moved = b.move_piece(current_legal_moves, coordinates, piece)

                    selected_piece = not selected_piece

                    new_legal_moves = game.get_legel_moves (
                            piece, b, coordinates[0], coordinates[1]
                    )

                    if not type(piece) == King:
                        b.set_legal_moves(new_legal_moves, current_legal_moves)

                    print("New Coordinates: " + str(new_legal_moves))
                    
                    print("All Legal Moves: " + str(b.all_legal_moves))

                    # Only change the boolean value of light_turn, if an piece was moved
                    game.light_turn = (
                        not game.light_turn if piece_moved else game.light_turn
                    )

        pygame.display.update()


if __name__ == "__main__":
    main()
