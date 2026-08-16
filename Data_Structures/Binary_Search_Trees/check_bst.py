from bst_node_and_printing import BSTNode

def find_max(root):
    if root is None:
        return  float("-inf")

    left_max = find_max(root.left)
    right_max = find_max(root.right)

    ans = max(root.data, left_max, right_max)
    return ans

def find_min(root):
    if root is None:
        return float("inf")

    left_min  = find_min(root.left)
    right_min = find_min(root.right)

    ans = min(root.data, left_min, right_min)
    return ans


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

    