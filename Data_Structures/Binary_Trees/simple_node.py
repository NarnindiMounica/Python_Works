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

#print_binary_tree(root)

def print_binary_tree_detailed(root):

    if root == None:
        return None

    print(f"{root.data}:", end = " ")
    if root.left == None:
        print("L -> None", end = ", ")
    else:
        print(f"L -> {root.left.data}", end = ", ") 

    if root.right == None:
        print("R -> None")
    else:
        print(f"R -> {root.right.data}") 

    print_binary_tree_detailed(root.left)
    print_binary_tree_detailed(root.right)

print_binary_tree_detailed(root)    

