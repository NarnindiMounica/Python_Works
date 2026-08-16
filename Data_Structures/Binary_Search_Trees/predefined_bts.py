class BinarySearchTrees:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_traversal(root):
    if root is None:
        return None

    bst_traversal(root.left)
    print(root.data, end = " ") #inorder traversal of bts
    bst_traversal(root.right)
  

def create_predefined_bst():

    root1 = BinarySearchTrees(10)
    root1.left = BinarySearchTrees(5)
    root1.right = BinarySearchTrees(15)


    root2 = BinarySearchTrees(20)
    root2.left = BinarySearchTrees(10)
    root2.right = BinarySearchTrees(30)

    root2.left.left = BinarySearchTrees(5)
    root2.left.right = BinarySearchTrees(15)

    root2.right.left = BinarySearchTrees(25)
    root2.right.right = BinarySearchTrees(35)


    root3 = 
    return root1, root2, root3