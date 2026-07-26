from commons import TreeNode, print_tree_detailed
from collections import deque

def take_input_level_wise():
    data = int(input("Enter the data of node: "))
    node = TreeNode(data)

    queue = deque([node])

    while len(queue) != 0:
        current_node = queue.popleft()
        num_of_children = int(input(f"Enter number of children of node {current_node.data}: "))

        for i in range(num_of_children):
            child_data = int(input(f"Enter the data of {i+1} child of node {current_node.data}: "))
            child_node = TreeNode(child_data)

            current_node.children.append(child_node)
            queue.append(child_node)

    return node

root_node = take_input_level_wise()
print_tree_detailed(root_node)

