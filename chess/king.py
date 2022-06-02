import pygame
from chess.general_piece import GeneralPiece


class King(GeneralPiece):
    def __init__(self, x, y, light, block_size):
        super().__init__(x, y, light, block_size)

        load_sprite = pygame.image
        if self.light:
            load_sprite = pygame.image.load("assets/w_king_png_shadow_128px.png")
        else:
            load_sprite = pygame.image.load("assets/b_king_png_shadow_128px.png")

        self.sprite = pygame.transform.scale(
            load_sprite, (self.block_size, self.block_size)
        )

        self.blockSize = block_size

        self.rect = self.sprite.get_rect()

        self.rect_x = x * block_size
        self.rect_y = y * block_size

    def get_board_pos(self):
        return self.rect_x // self.block_size, self.rect_y // self.block_size

    def get_legal_moves(self, board):
        possible_moves = []

        directions = [(-1, -1),(0, -1),(1, -1),
                     (-1,  0),        (1,  0),
                     (-1,  1),(0,  1),(1,  1),
        ]

        for dir in directions:
            new_x, new_y = self.x + dir[0], self.y + dir[1] 
            piece = board.get_piece(new_x, new_y)

            if 0 <= new_x < 8 and 0 <= new_y < 8:
                piece = board.get_piece(new_x, new_y)
                if type(piece) == int:
                    possible_moves.append([new_x, new_y])
                else:
                    if not piece.light == self.light:
                        possible_moves.append([new_x, new_y])
                        break
                    else:
                        break
        return possible_moves

    def __repr__(self) -> str:
        status = "dark" if not self.light else "light"
        return str(status) + " King"
