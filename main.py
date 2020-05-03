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
