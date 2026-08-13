from simple_node import BinaryTreeNode, print_binary_tree_detailed
import take_input_binary_tree


def max_depth_of_bt(root):

    if root == None:
        return 0

    height = 1
    max_height = 0

    left_height = max_depth_of_bt(root.left)
    right_height = max_depth_of_bt(root.right)

    max_height = max(left_height, right_height)
    height = height + max_height

    return height

root = take_input_binary_tree.take_input_for_binary_tree()
print(max_depth_of_bt(root)