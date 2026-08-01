from simple_node import print_binary_tree_detailed, BinaryTreeNode
from collections import deque

def take_input_level_wise():
    data = int(input("Enter the data of the node: "))
    if data == -1:
        return None
    
    node = BinaryTreeNode(data)

    queue = deque([node])

    while len(queue) != 0:
        current_node = queue.popleft()

        left_child_data = int(input(f"Enter the data of the left node of {current_node.data}: "))
        if left_child_data != -1:
            left_node = BinaryTreeNode(left_child_data)
            current_node.left = left_node
            queue.append(left_node)

        right_child_data = int(input(f"Enter the data of the right node of {current_node.data}: "))
        if right_child_data != -1:
            right_node = BinaryTreeNode(right_child_data)
            current_node.right = right_node
            queue.append(right_node) 


    return node

# root = take_input_level_wise()
# print_binary_tree_detailed(root)           


