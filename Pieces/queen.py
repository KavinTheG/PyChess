import pygame
import Pieces.general_behaviour


class Queen(Pieces.general_behaviour.GeneralBehaviour):
    def __init__(self, light, board, blockSize):
        super().__init__(light, board, blockSize)

        load_sprite = pygame.image
        if self.light:
            load_sprite = pygame.image.load("128px/w_queen_png_shadow_128px.png")
        else:
            load_sprite = pygame.image.load("128px/b_queen_png_shadow_128px.png")

        self.sprite = pygame.transform.scale(
            load_sprite, (self.blockSize, self.blockSize)
        )

    def returnSprite(self):
        return self.sprite
