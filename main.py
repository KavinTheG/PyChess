import sys
import pygame
from chess.board import Board
from chess.game_logic import GameLogic

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
    b.print_board_state()
    game = GameLogic()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coordinates = [i // BLOCKSIZE for i in pygame.mouse.get_pos()]
                print("Clicked Coordinates: " + str(coordinates))
                piece = b.get_piece(coordinates[0], coordinates[1])
                # print(piece)
                print(
                    "Possible moves: "
                    + str(
                        game.get_legel_moves(piece, b, coordinates[0], coordinates[1])
                    )
                )

        pygame.display.update()


if __name__ == "__main__":
    main()
