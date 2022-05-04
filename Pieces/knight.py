import pygame
import Pieces.general_behaviour


class Knight(Pieces.general_behaviour.GeneralBehaviour):
    def __init__(self, light, board, blockSize):
        super().__init__(light, board, blockSize)

        load_sprite = pygame.image
        if self.light:
            load_sprite = pygame.image.load("128px/w_knight_png_shadow_128px.png")
        else:
            load_sprite = pygame.image.load("128px/b_knight_png_shadow_128px.png")

        self.sprite = pygame.transform.scale(
            load_sprite, (self.blockSize, self.blockSize)
        )

    def legalMove(self):

        # It's dark peice
        currentPos = self.position
        if self.light:
            newPos = (currentPos[0], currentPos[1] + 1)

        return newPos

    def returnSprite(self):
        return self.sprite
