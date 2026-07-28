from simple_node import BinaryTreeNode, print_binary_tree_detailed

def take_input_for_binary_tree():

    data = int(input("Enter data for the node: "))
    if data == -1:
        return None
    root = BinaryTreeNode(data)

    print(f"For left node of {root.data}: ")
    root.left=take_input_for_binary_tree()

    print(f"For right node of {root.data}: ")
    root.right=take_input_for_binary_tree()

    return root

root = take_input_for_binary_tree()
print_binary_tree_detailed(root)

