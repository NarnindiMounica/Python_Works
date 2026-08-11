from collections import deque

class Tree:
    def __init__(self, val):
        self.val = val
        self.children = []

    def max_data_level_wise(self):
