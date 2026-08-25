class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_predecessor_successor(root, key):
    """
    Function to find the predecessor and successor of a node with the given key in a BST.
    
    :param root: TreeNode -> The root of the binary search tree
    :param key: int -> The value of the node for which to find the predecessor and successor
    :return: Tuple[Optional[int], Optional[int]] -> A tuple containing the predecessor and successor
    """
    # TODO: Implement the logic to find the predecessor and successor
    
    def inorder(root, lst):
        if root == None:
            return 
        inorder(root.left, lst)
        lst.append(root.val)
        inorder(root.right, lst)
        
    lst = []
    inorder(root, lst)
    
    if key in lst:
        key_inx = lst.index(key)
    predecessor = lst[key_inx - 1] if key_inx > 0 else None
    successor = lst[key_inx + 1] if key_inx < len(lst) - 1 else None

    return (predecessor, successor)        
            
    
