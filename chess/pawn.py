import pygame
from chess.general_piece import GeneralPiece


class Pawn(GeneralPiece):
    def __init__(self, x, y, light, block_size):
        super().__init__(x, y, light, block_size)

        load_sprite = pygame.image
        if self.light:
            load_sprite = pygame.image.load("assets/w_pawn_png_shadow_128px.png")
        else:
            load_sprite = pygame.image.load("assets/b_pawn_png_shadow_128px.png")

        self.sprite = pygame.transform.scale(
            load_sprite, (self.block_size, self.block_size)
        )

        #self.rect = self.sprite.get_rect()

        self.rect_x = x * block_size
        self.rect_y = y * block_size


    def __repr__(self) -> str:
        status = "dark" if not self.light else "light"
        return str(status) + " Pawn"
