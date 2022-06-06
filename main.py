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

    board = Board(SCREEN, 8, DARK, LIGHT, BLOCKSIZE)
    
    # Store the selected piece
    piece = None

    # Variable determines player's turn
    light_turn = True

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coordinates = [i // BLOCKSIZE for i in pygame.mouse.get_pos()]
                
                # No piece was selected so far
                if piece == None:

                    possible_piece = board.get_piece(coordinates[0], coordinates[1])

                    # Checks if a valid piece was clicked
                    if not type(possible_piece) == int:
                        if possible_piece.light == light_turn:
                            piece = possible_piece
                        else: 
                            piece = None
                    else: 
                        piece = None

                # Checks if a valid move was made
                else:
                    valid_move = board.move_piece(piece, coordinates)

                    if valid_move:
                        light_turn = not light_turn
                        print(light_turn)

                        # Clear up piece variable
                        piece = None
                    else:

                        # Change focus to another alliance piece if it was selected
                        possible_piece = board.get_piece(coordinates[0], coordinates[1])

                        if not type(possible_piece) == int:
                            if possible_piece.light == light_turn:
                                piece = possible_piece

                            

        pygame.display.update()


if __name__ == "__main__":
    main()
