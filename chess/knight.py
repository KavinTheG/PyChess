import pygame
from chess.general_piece import GeneralPiece

class Knight(GeneralPiece):
    def __init__(self, x, y, light, block_size):
        super().__init__(x, y, light, block_size)

        load_sprite = pygame.image
        if self.light:
            load_sprite = pygame.image.load("assets/w_knight_png_shadow_128px.png")
        else:
            load_sprite = pygame.image.load("assets/b_knight_png_shadow_128px.png")

        self.sprite = pygame.transform.scale(
            load_sprite, (self.block_size, self.block_size)
        )

        self.rect = self.sprite.get_rect()

        self.rect_x = x * block_size
        self.rect_y = y * block_size

    def get_board_pos(self):
        return self.rect_x // self.block_size, self.rect_y // self.block_size

    def get_legal_moves(self, board):
        possible_moves = []

        # for loop to iterate through values -2 to 2
        # these are the possible values we can add to the x-cord
        for i in range(-2, 3):
            if i == 0:
                continue  # skip, as there is no possible movement where knight stays on the same axis
            add_y = 1 if i % 2 == 0 else 2
            new_x = self.x + i

            if 0 <= new_x < 8:
                left_y = self.y - add_y
                right_y = self.y + add_y

                if left_y >= 0:
                    if (
                        type(board.get_piece(new_x, left_y)) == int
                        or not board.get_piece(new_x, left_y).light == self.light
                    ):
                        possible_moves.append([new_x, left_y])
                if right_y < 8:
                    if (
                        type(board.get_piece(new_x, right_y)) == int
                        or not board.get_piece(new_x, right_y).light == self.light
                    ):
                        possible_moves.append([new_x, right_y])
        
        return possible_moves


    def __repr__(self) -> str:
        status = "dark" if not self.light else "light"
        return str(status) + " Knight"
