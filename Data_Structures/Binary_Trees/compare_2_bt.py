from simple_node import BinaryTreeNode, print_binary_tree_detailed
import take_input_binary_tree

def is_same_tree(p, q):
    """
    Function to check if two binary trees are the same.
    :param p: TreeNode -> root of the first tree
    :param q: TreeNode -> root of the second tree
    :return: bool -> True if both trees are the same, False otherwise
    """
    # TODO: Implement this function
    if p == None and q == None:
        return True
    
    if p == None or q == None:
        return False
    
    if p.data != q.data:
        return False
        
    left_tree = is_same_tree(p.left, q.left)
    if left_tree == False:
            return False
    right_tree = is_same_tree(p.right, q.right)
    if right_tree == False:
            return False
    return True        

print("Enter node details of 1st tree: \n")
p = take_input_binary_tree.take_input_for_binary_tree()
print("Enter node details of 2nd tree: \n")
q = take_input_binary_tree.take_input_for_binary_tree()

print("Are both trees same: ")
print(is_same_tree(p,q))