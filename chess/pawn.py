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

        # self.rect = self.sprite.get_rect()

        self.rect_x, self.y = x, y 
        self.rect_x = x * block_size
        self.rect_y = y * block_size

    def get_legal_moves(self, board):
        direction = -1 if self.light else 1
        possible_moves = []
        if not self.y == 0 or not self.y == 7:
            if type(board.get_piece(self.x, self.y + direction)) == int:
                possible_moves.append([self.x, self.y + direction])

            if (
                self.y == 1
                and type(board.get_piece(self.x, self.y + 2 * direction)) == int
                and not self.light
            ):
                possible_moves.append([self.x, self.y + 2 * direction])

            if (
                self.y == 6
                and type(board.get_piece(self.x, self.y + 2 * direction)) == int
                and self.light
            ):
                possible_moves.append([self.x, self.y + 2 * direction])
            if not self.x == 0:
                if not type(board.get_piece(self.x - 1, self.y + direction)) == int:
                    piece_two = board.get_piece(self.x - 1, self.y + direction)

                    if not piece_two.light == self.light:
                        possible_moves.append([self.x - 1, self.y + direction])
            if not self.x == 7:
                if not type(board.get_piece(self.x + 1, self.y + direction)) == int:
                    piece_two = board.get_piece(self.x + 1, self.y + direction)

                    if not piece_two.light == self.light:
                        possible_moves.append([self.x + 1, self.y + direction])
        
        return possible_moves

    def __repr__(self) -> str:
        status = "dark" if not self.light else "light"
        return str(status) + " Pawn"
