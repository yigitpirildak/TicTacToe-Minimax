from memory import Memory
from model import TicTacModel
from ticTacBoard import TicTacBoard, State, Mark
from p5 import *
import random
import numpy as np
import math

ticTacBoard = None
SIZE = 300
playAs = Mark.X
aiPlayer = Mark.X if playAs is Mark.O else Mark.O

def setup():
    global ticTacBoard
    size(SIZE, SIZE)
    ticTacBoard = TicTacBoard(SIZE)

def draw():
    background(24)
    size_per_square = SIZE/3
    ticTacBoard.draw()

    if ticTacBoard.get_state() is not State.ONGOING:
        return

    if (ticTacBoard.get_turn_to_play() is aiPlayer):
        bestScore = -math.inf
        bestMove = None
        for move in ticTacBoard.get_possible_moves():
            ticTacBoard.make_move(move)
            score = minimax(False, aiPlayer, ticTacBoard)
            ticTacBoard.undo()
            if (score > bestScore):
                bestScore = score
                bestMove = move
        ticTacBoard.make_move(bestMove)
    else:
        if mouse_is_pressed:
            ticTacBoard.make_ui_move(mouse_x, mouse_y)

def minimax(isMaxTurn, maximizerMark, board):
    state = board.get_state()
    if (state is State.DRAW):
        return 0
    elif (state is State.OVER):
        return 1 if board.get_winner() is maximizerMark else -1

    scores = []
    for move in board.get_possible_moves():
        board.make_move(move)
        scores.append(minimax(not isMaxTurn, maximizerMark, board))
        board.undo()
        if (isMaxTurn and max(scores) == 1) or (not isMaxTurn and min(scores) == -1):
            break

    return max(scores) if isMaxTurn else min(scores)

if __name__ == "__main__":
    run()
