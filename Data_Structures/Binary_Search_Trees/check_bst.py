from bst_node_and_printing import BSTNode

def find_max(root):
    pass

def find_min(root):
    pass

def check_bst(root):
    if root is None: #empty tree is a bst
        return True

    left_max = find_max(root.left)
    right_min = find_min(root.right)

    left_bst = check_bst(root.left)
    right_bst = check_bst(root.right)

    ans = left_bst and right_bst and (left_max < root.data and root.data < right_min)

    return ans

    