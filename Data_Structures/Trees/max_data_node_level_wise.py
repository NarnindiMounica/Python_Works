from collections import deque

from generic_trees_input import predefined_generic_trees
from commons import print_tree_detailed


def max_data_level_wise(root):
    if root == None:
        return []
    
    queue = deque([root])
    max_node_list = []
    
    while len(queue) != 0:
        level_size = len(queue)
        temp = float('-inf')
        for _ in range(level_size):
            current_node = queue.popleft()
            temp = max(temp, current_node.data)
            for eachchild in current_node.children:
                queue.append(eachchild)
    max_node_list.append(temp)
    return max_node_list


root1, root2, root3 = predefined_generic_trees()

print_tree_detailed(root1)
print(max_data_level_wise(root1))
print()
print_tree_detailed(root2)
print(max_data_level_wise(root2))
print()
print_tree_detailed(root3)
print(max_data_level_wise(root3))
