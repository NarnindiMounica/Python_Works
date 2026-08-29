class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes_in_range(root, queries):
    
    out_lst = []
    # Core logic for the learner to implement
    def count_nodes_in_range_helper(root, low, high):
        count = 0

        if root == None:
            return 0
        
        if low <= root.val <= high:
            count += 1   

        if  root.val > low:
            count += count_nodes_in_range_helper(root.left, low, high)
        
        elif root.val < high:
            count += count_nodes_in_range_helper(root.right, low, high)
        
        return count

    for query in queries:
        query_count = count_nodes_in_range_helper(root, query[0], query[1])
        out_lst.append(query_count)
    
    return out_lst  
             