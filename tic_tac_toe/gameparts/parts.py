class Board: 
    """Класс, который описывает игровое поле."""

    def __init__(self): 
        self.field_size = 3
        self.board = [[' ' for _ in range(self.field_size)] for _ in range(self.field_size)]


    def make_move(self, row, col, player):
        sel