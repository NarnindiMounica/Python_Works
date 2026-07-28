class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3) 



def print_binary_tree(root):
    #base case

    if root is None:
        return None

    print(f'{root.data}', end = " ")
    print_binary_tree(root.left)
    print_binary_tree(root.right)    

print_binary_tree(root)