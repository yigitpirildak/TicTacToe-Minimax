from enum import Enum


class TicTacBoard:
    WINNING_SCORE = 3
    HEIGHT = 3
    WIDTH = 3
    MAX_NUMBER_OF_MOVES = HEIGHT*WIDTH

    def __init__(self):
        self.boardMatrix = [[Mark.EMPTY for x in range(TicTacBoard.WIDTH)] for y in range(TicTacBoard.HEIGHT)]
        self.numberOfMovesLeft = TicTacBoard.MAX_NUMBER_OF_MOVES
        self.boardState = BoardState.ONGOING

    def get_board(self):
        return self.boardMatrix

    def print_board(self):
        print("===============================")
        for x in range(TicTacBoard.HEIGHT):
            for y in range(TicTacBoard.WIDTH):
                print("[{0}]".format(self.boardMatrix[x][y]), end="")
            if x != TicTacBoard.HEIGHT:
                print("")
        print("===============================")

    def make_move(self, coordinates, mark):
        if self.boardState != BoardState.ONGOING:
            return self.boardState

        try:
            self.boardMatrix[coordinates[0]][coordinates[1]] = mark.value
            self.numberOfMovesLeft = self.numberOfMovesLeft - 1
            self.boardState = self.get_board_state()
            return self.boardState
        except IndexError:
            return self.boardState

    def get_board_state(self):
        current_state = self.__dfs_board_evaluation()
        if current_state is not None:
            return current_state
        elif self.numberOfMovesLeft > 0:
            return BoardState.ONGOING
        else:
            return BoardState.DRAW

    def __dfs_board_evaluation(self, row=0, col=0, countX=0, countY=0):
        try:
            if self.boardMatrix[row][col] == Mark.X.value:
                countX = countX + 1
            elif self.boardMatrix[row][col] == Mark.Y.value:
                countY = countY + 1
        except IndexError:
            return None

        if countX == TicTacBoard.WINNING_SCORE:
            return BoardState.WINNER_X
        elif countY == TicTacBoard.WINNING_SCORE:
            return BoardState.WINNER_Y
        elif row == TicTacBoard.HEIGHT or col == TicTacBoard.WIDTH:
            return None

        verticalEvaluation = self.__dfs_board_evaluation(row + 1, col, countX, countY)
        horizontalEvalution = self.__dfs_board_evaluation(row, col + 1, countX, countY)
        diagonalEvaluation = self.__dfs_board_evaluation(row + 1, col + 1, countX, countY)

        if verticalEvaluation is not None:
            return verticalEvaluation
        elif horizontalEvalution is not None:
            return horizontalEvalution
        elif diagonalEvaluation is not None:
            return diagonalEvaluation
        else:
            return None


class Mark(Enum):
    X = 1,
    O = 2,
    EMPTY = 3


class BoardState(Enum):
    WINNER_Y = 1
    WINNER_X = 2
    ONGOING = 3
    DRAW = 4

