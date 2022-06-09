class GeneralPiece:
    def __init__(self, x, y, light, block_size):

        # boolean value to determine if peice is dark/light
        self.light = light

        # boolean value to determine if peice is alive
        self.alive = True

        self.x = x
        self.y = y

        self.rect_x = x * block_size
        self.rect_y = y * block_size

        self.block_size = block_size

    def isdigit(self):
        return False

    def get_board_pos(self):
        return self.rect_x // self.block_size, self.rect_y // self.block_size

    def set_new_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect_x = x * self.block_size
        self.rect_y = y * self.block_size

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, GeneralPiece):
            return __o.x == self.x and __o.y == self.y

    def __hash__(self):
        return hash(str(self))