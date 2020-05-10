# TicTacToe-Minimax
Implementation of minimax algorithm to solve Tic-Tac-Toe. Board visualization is achieved using p5 library.

# About Minimax
Minimax is an adversarial search algorithm to explore game trees in order to find the most optimal move. This project implements the most straight-forward version of it, no depth-limit and no alpha-beta pruning. The idea is to generate generate a game tree and explore each state until you either reach a terminal state, or the depth-limit (in depth-limited minimax). All leaf nodes are assigned a value and at each level of the tree, either maximizer or minimizer attempts to pick the most optimal move.

# Installation
Processing library (p5) requires GLFW to be installed. Based on your platform, installation guidelines can be found in https://p5.readthedocs.io/en/latest/install.html.
Once pre-requisites of p5 are met, install the required packages:

```bash
sudo apt-get install python3-pip
pip3 install -r requirements.txt
```


