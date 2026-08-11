from collections import deque

from generic_trees_input import predefined_generic_trees

class Tree:
    def __init__(self, val):
        self.val = val
        self.children = []

def max_data_level_wise(root):
    if root == None:
        return []
    
    queue = deque([root])
    max_node_list = []
    while queue != 0:
        current_node = queue.popleft()
        temp = -1
        for eachchild in current_node.children:
            temp = max(temp, eachchild.val)


