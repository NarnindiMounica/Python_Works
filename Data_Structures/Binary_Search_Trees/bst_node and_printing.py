from predefined_bst import create_predefined_bst

class BTSNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_bst(root):
    if root is None:
        return None

    print_bst(root.left)
    print(root.data, end = " ") #inorder traversal of bts
    print_bst(root.right)

root1, root2, root3 = create_predefined_bst()
print_bst(root1)
print()
print_bst(root2)
print()
print_bst(root3)          