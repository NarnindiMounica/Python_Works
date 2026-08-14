def is_balanced(root):
    """
    Function to check if a binary tree is height-balanced.
    :param root: TreeNode -> root of the binary tree
    :return: bool -> True if the tree is balanced, False otherwise
    """
    # TODO: Implement this function
    if root == None:
        return True
    
    height = 1
    max_height = 0
    left_height =  is_balanced(root.left)
    right_height = is_balanced(root.right)
    if left_height - right_height > 1:
        return False
    
    return True 