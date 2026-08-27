class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    # Core logic for the learner to implement
    
    
    def inorder(root, lst):
        if root == None:
            return None
        inorder(root.left, lst)
        lst.append(root.val)
        inorder(root.right, lst)
        
    lst = []
    inorder(root, lst
    
    return lst[k-1]
