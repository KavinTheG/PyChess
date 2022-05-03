from curses import window
import pygame


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

DARK = (101, 67, 33)
LIGHT = (181, 101, 29)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)


    while True:
    
        drawBoard(8)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        

        pygame.display.update()


            
def drawBoard(size):

    blockSize = (int) (WINDOW_HEIGHT / size)

    #light = pygame.image.load("128px/square brown light_png_shadow_128px.png")
    #dark = pygame.image.load("128px/square brown dark_png_shadow_128px.png")

 #   light = pygame.transform.scale(light, (blockSize, blockSize))
#    dark = pygame.transform.scale(dark, (blockSize, blockSize))

    for y in range(size):
        for x in range(size):
            rect = pygame.Rect(x * blockSize, y * blockSize,
                               blockSize, blockSize)

            if (x % 2 == y % 2):
                pygame.draw.rect(SCREEN, DARK, rect)
            else:
                pygame.draw.rect(SCREEN, LIGHT, rect)




if __name__ == "__main__":
    main()