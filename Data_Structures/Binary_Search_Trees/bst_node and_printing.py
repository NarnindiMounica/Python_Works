class BTSNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_bst(root):
    if root is None:
        return None

    print_bst(root.left)
    print(root.data, end = " ")
    print_bst(root.right)

            