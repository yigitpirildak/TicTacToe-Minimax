from enum import Enum
from p5 import *

FONT = create_font("fonts/SigmarOne-Regular.ttf", 0)

class Mark(Enum):
    X = 1
    O = 2
    EMPTY = 3

class TicTacBoard:
    def __init__(self, size):
        self.size = size;
        self.size_per_square = size / 3
        self.boardMatrix = [[Mark.EMPTY.value for x in range(3)] for y in range(3)]
        self.turnToPlay = Mark.X
        self.mark_size = int(self.size_per_square / 2)

    def draw(self):
        self.__draw_background()
        self.__draw_board_state()

    def __draw_background(self):
        stroke_weight(5)
        line((self.size_per_square, 0), (self.size_per_square, self.size))
        line((self.size_per_square * 2, 0), (self.size_per_square * 2, self.size))
        line((0, self.size_per_square), (self.size, self.size_per_square))
        line((0, self.size_per_square * 2), (self.size, self.size_per_square * 2))

    def __draw_board_state(self):
        for x in range(3):
            for y in range(3):
                state = Mark(self.boardMatrix[x][y])
                if state is not Mark.EMPTY:
                    text_font(FONT)
                    text_size(self.mark_size)
                    text(state.name, (self.size_per_square * x + self.size_per_square / 2 - self.mark_size / 2, self.size_per_square * y + self.size_per_square / 2 - self.mark_size))

    def make_move(self, mouse_x, mouse_y):
        x = int(mouse_x / self.size_per_square)
        y = int(mouse_y / self.size_per_square)
        if (self.boardMatrix[x][y] == Mark.EMPTY.value):
            self.boardMatrix[x][y] = self.turnToPlay.value
            self.__switch_players()

    def __switch_players(self):
        self.turnToPlay = Mark.X if self.turnToPlay is Mark.O else Mark.O
