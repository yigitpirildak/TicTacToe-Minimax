from enum import Enum
from p5 import *

FONT = create_font("fonts/SigmarOne-Regular.ttf", 0)

class Mark(Enum):
    X = 2
    O = 4
    EMPTY = 8

class State(Enum):
    DRAW = 1
    ONGOING = 2
    OVER = 3

class TicTacBoard:
    def __init__(self, size):
        self.size = size;
        self.size_per_square = size / 3
        self.boardMatrix = [[Mark.EMPTY.value for x in range(3)] for y in range(3)]
        self.turnToPlay = Mark.X
        self.mark_size = int(self.size_per_square / 2)
        self.winningMarks = []

    def draw(self):
        self.__draw_background()
        self.__draw_board_state()

    def __draw_background(self):
        stroke_weight(5)
        stroke(0)
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
                    if (x, y) in self.winningMarks:
                        fill(127, 0, 0)
                    else :
                        fill(255)
                    text(state.name, (self.size_per_square * x + self.size_per_square / 2 - self.mark_size / 2, self.size_per_square * y + self.size_per_square / 2 - self.mark_size))

    def make_move(self, mouse_x, mouse_y):
        x = int(mouse_x / self.size_per_square)
        y = int(mouse_y / self.size_per_square)
        if (self.boardMatrix[x][y] == Mark.EMPTY.value):
            self.boardMatrix[x][y] = self.turnToPlay.value
            self.__switch_players()

            board_eval = self.evaluate_board_state()
            print(board_eval)
            if (board_eval[0] is State.OVER):
                self.winningMarks = board_eval[2:]

    def __switch_players(self):
        self.turnToPlay = Mark.X if self.turnToPlay is Mark.O else Mark.O

    def evaluate_board_state(self):
        draw = True
        for x in range(3):
            for y in range(3):
                mark = Mark(self.boardMatrix[x][y])
                if mark is Mark.EMPTY:
                    draw = False
                    continue
                else:
                    # Horizontal
                    try:
                        if (mark.value | self.boardMatrix[x+1][y] | self.boardMatrix[x+2][y]) == mark.value:
                            return (State.OVER, mark, (x, y), (x+1, y), (x+2, y))
                    except:
                        pass

                    # Vertical
                    try:
                        if (mark.value | self.boardMatrix[x][y+1] | self.boardMatrix[x][y+2]) == mark.value:
                            return (State.OVER, mark, (x, y), (x, y+1), (x, y+2))
                    except:
                        pass

                    # Diagonal
                    if x == 0 and y == 0 and (mark.value | self.boardMatrix[x+1][y+1] | self.boardMatrix[x+2][y+2] == mark.value):
                        return (State.OVER, mark, (x, y), (x+1, y+1), (x+2, y+2))
                    elif x == 0 and y == 2 and (mark.value | self.boardMatrix[x+1][y-1] | self.boardMatrix[x+2][y-2] == mark.value):
                        return (State.OVER, mark, (x, y), (x+1, y-1), (x+2, y-2))

        return [State.DRAW if draw else State.ONGOING]
