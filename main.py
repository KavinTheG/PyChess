import sys
import pygame
import board
import images


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

    b = board.Board(size=SIZE)
    b.printBoardArray()

    while True:

        # drawBoard(SCREEN, DARK, LIGHT, BLOCKSIZE)
        b.drawBoard(SCREEN, DARK, LIGHT, BLOCKSIZE)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


'''def drawBoard(surface, dark, light, blockSize):

    for y in range(SIZE):
        for x in range(SIZE):
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)

            if x % 2 == y % 2:
                pygame.draw.rect(surface, dark, rect)
            else:
                pygame.draw.rect(surface, light, rect)

            if y == 1:
                SCREEN.blit(images.b_p, (x * blockSize, blockSize * y))'''


if __name__ == "__main__":
    main()
