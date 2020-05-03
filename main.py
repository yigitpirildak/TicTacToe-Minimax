from memory import Memory
from model import TicTacModel
from ticTacBoard import TicTacBoard
from p5 import *
import random
import numpy as np

ticTacBoard = None
SIZE = 300

def setup():
    global ticTacBoard
    size(SIZE, SIZE)
    ticTacBoard = TicTacBoard(SIZE)

def draw():
    background(24)
    size_per_square = SIZE/3
    ticTacBoard.draw()


    if mouse_is_pressed:
        ticTacBoard.make_move(mouse_x, mouse_y)

if __name__ == "__main__":
    run()
    """memory = Memory()
    model = TicTacModel()
    for i in range(0, 20):
        ticTacGame = TicTacGame()
        terminal = False
        turnToPlay = Mark.X
        x_train = np.array([])
        y_train = np.array([])
        while not terminal:
            print("Turn To Play = " + turnToPlay.name)
            rewards = np.ndarray(9)
            current_state = ticTacGame.get_normalized_board_with_player(turnToPlay)
            prediction = int(np.argmax(model.predict(np.array([ticTacGame.get_normalized_board_with_player(turnToPlay)]))))
            actual_reward, terminal = ticTacGame.make_move((int(prediction / 3), int(prediction % 3)), turnToPlay)
            while actual_reward == -100:
                rewards[prediction] = actual_reward
                prediction = random.randrange(0, 9)
                actual_reward, terminal = ticTacGame.make_move((int(prediction / 3), int(prediction % 3)), turnToPlay)
            rewards[prediction] = actual_reward
            x_train = np.insert(x_train, x_train.size, current_state)
            y_train = np.insert(y_train, y_train.size, rewards / max(abs(np.max(rewards)), abs(np.min(rewards))))

            turnToPlay = Mark.X if turnToPlay == Mark.O else Mark.O
        ticTacGame.print_board()
        model.train(x_train.reshape(int(x_train.size / 10), 10), y_train.reshape(int(y_train.size / 9), 9))
"""
