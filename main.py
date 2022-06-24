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

WINDOW_HEIGHT = 480
WINDOW_WIDTH = 480

# Chess board size (8 by 8)
SIZE = 8
BLOCKSIZE = (int)(WINDOW_WIDTH / SIZE)


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    board = Board(SCREEN, 8, DARK, LIGHT, BLOCKSIZE)
    
    # Store the selected piece
    piece = None

    # Variable determines player's turn
    light_turn = True

    check_mate = False

    while True:


        for event in pygame.event.get():
            if check_mate and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('reset')
                    # Store the selected piece
                    piece = None

                    board = Board(SCREEN, 8, DARK, LIGHT, BLOCKSIZE)
                    
                    # Variable determines player's turn
                    light_turn = True

                    check_mate = False    

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not check_mate:
                coordinates = [i // BLOCKSIZE for i in pygame.mouse.get_pos()]
                
                # No piece was selected so far
                if piece == None:

                    possible_piece = board.get_piece(coordinates[0], coordinates[1])

                    # Checks if a valid piece was clicked
                    if not type(possible_piece) == int:
                        if possible_piece.light == light_turn:
                            piece = possible_piece
                            board.indicate_move(piece)
                        else: 
                            piece = None
                    else: 
                        piece = None

                # Checks if a valid move was made
                else:
                    valid_move = board.move_piece(piece, coordinates)

                    if valid_move:
                        light_turn = not light_turn
                        print("Turn: " + str(light_turn))
                        
                        check_mate = board.is_check_mate(light_turn)
                        print("Checkmate: " + str(board.is_check_mate(light_turn)))

                        # Clear up piece variable
                        piece = None
                    else:

                        # Change focus to another alliance piece if it was selecte
                        possible_piece = board.get_piece(coordinates[0], coordinates[1])

                        if not type(possible_piece) == int:
                            if possible_piece.light == light_turn:
                                piece = possible_piece
                                board.draw_board()
                                board.draw_pieces()
                                board.indicate_move(piece)

                            

        pygame.display.update()


if __name__ == "__main__":
    main()
