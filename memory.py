import math


class Memory:

    def __init__(self, limit=math.inf):
        self.memory = []
        self.limit = limit

    def add(self, state, action):
        self.memory.append(MemoryPiece(state, action))
        if self.limit > len(self.memory):
            self.memory.pop(0)


class MemoryPiece:

    def __init__(self, state, action):
        self.state = state
        self.action = action

    def get_state(self):
        return self.state

    def get_action(self):
        return self.action
