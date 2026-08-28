class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes_in_range(root, queries):
    
    out_lst = []
    # Core logic for the learner to implement
    def count_nodes_in_range_helper(root, low, high, count):
        
        if root == None:
            return 0
        
        if low <= root.val <= high:
            count += 1   

        if  root.val > low:
            count += count_nodes_in_range_helper(root.left, low, high, count)
        
        elif root.val < high:
            count += count_nodes_in_range_helper(root.right, low, high, count)
        
        return count
             