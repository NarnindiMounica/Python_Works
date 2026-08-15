from simple_node import BinaryTreeNode, print_binary_tree_detailed
import take_input_binary_tree

root = take_input_binary_tree.take_input_for_binary_tree()

def left_leaves_sum(root):

    if root == None:
        return 0
    sum = 0
    print(root.left.data)

    

