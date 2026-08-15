from simple_node import BinaryTreeNode, print_binary_tree_detailed
import take_input_binary_tree

def left_leaves_sum(root):

    leaves_sum = 0

    if root == None:
        return 0

    if root.left != None and root.left.left == None and root.left.right == None:
        leaves_sum = leaves_sum + root.left.data

    leaves_sum += left_leaves_sum(root.left)
    leaves_sum += left_leaves_sum(root.right)

    return leaves_sum     


root = take_input_binary_tree.take_input_for_binary_tree()
print(left_leaves_sum(root))

    

