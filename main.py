from ticTacBoard import TicTacBoard, Mark, BoardState
from memory import Memory
from model import TicTacModel
import numpy as np


class TicTacGame:

    def __init__(self):
        self.board = TicTacBoard()

    def get_board(self):
        return self.board.get_board()

    def get_normalized_board(self):
        return np.arange(self.board.get_board()) / 3  # 3 is the maximum possible value

    def print_board(self):
        return self.board.print_board()

    def make_move(self, coordinates, mark):
        board_state = self.board.make_move(self, coordinates, mark)
        terminal = True
        if board_state == BoardState.ONGOING:
            terminal = False

        reward = self.calculate_reward(mark)
        return terminal, reward

    def calculate_reward(self, mark):
        reward = 0
        if self.board.get_board_state() == BoardState.DRAW:
            reward = 5
        elif self.board.get_board_state() == BoardState.WINNER_X:
            reward = 50
        elif self.board.get_board_state() == BoardState.Winner_Y:
            reward = -50
        else:
            current_board = self.board.get_board()
            x_close_to_win, o_close_to_win = self.__get_closeness_to_win()
            if mark == Mark.X.value:
                reward = x_close_to_win*10 - o_close_to_win * 25
            else:
                reward = o_close_to_win*10 - x_close_to_win * 25
        return reward

    def __get_closeness_to_win(self):
        x_close_to_win = 0
        o_close_to_win = 0
        current_board = self.board.get_board()

        for i in range(0, len(current_board)):
            x_close_to_win, o_close_to_win = max(self.__check_if_close_to_win(current_board[i][0],
                                                                              current_board[i][1],
                                                                              current_board[i][2]),
                                                 (x_close_to_win, o_close_to_win))

        for i in range(0, len(current_board[0])):
            x_close_to_win, o_close_to_win = max(self.__check_if_close_to_win(current_board[0][i],
                                                                              current_board[1][i],
                                                                              current_board[2][i]),
                                                 (x_close_to_win, o_close_to_win))

        # Diagonals
        x_close_to_win, o_close_to_win = max(self.__check_if_close_to_win(current_board[0][0],
                                                                          current_board[1][1],
                                                                          current_board[2][2]),
                                             (x_close_to_win, o_close_to_win))

        x_close_to_win, o_close_to_win = max(self.__check_if_close_to_win(current_board[0][2],
                                                                          current_board[1][1],
                                                                          current_board[2][0]),
                                             (x_close_to_win, o_close_to_win))

        return x_close_to_win, o_close_to_win

    def __check_if_close_to_win(self, first, second, third):
        xor = first ^ second ^ third ^ Mark.EMPTY.value  # Check if 2 Mark + Empty is found
        sum = first + second + third

        x_close_to_win = 0
        o_close_to_win = 0
        if sum != Mark.EMPTY.value and xor == Mark.EMPTY.value:
            if first | second | third == Mark.X.value:
                x_close_to_win = 1
            else:
                o_close_to_win = 1

        return x_close_to_win, o_close_to_win


if __name__ == "__main__":
    ticTacGame = TicTacGame()
    memory = Memory()
    model = TicTacModel()
    while True:
        terminal = False
        while not terminal:
            print(ticTacGame.get_normalized_board())
