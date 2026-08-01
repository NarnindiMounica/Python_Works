from simple_node import BinaryTreeNode, print_binary_tree_detailed
from take_input_level_wise import take_input_level_wise


def pre_order_traversal(root):
    if root == None:
        return None

    print(f"{root.data}", end = " ")

    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


root = take_input_level_wise()
print_binary_tree_detailed(root)
pre_order_traversal(root)

def post_order_traversal(root):
    if root == None:
        return None

    post_order_traversal(root.left)
    post_order_traversal(root.right)

    print(f"{root.data}", end = " ")

root = take_input_level_wise()
print_binary_tree_detailed(root)
post_order_traversal(root)    