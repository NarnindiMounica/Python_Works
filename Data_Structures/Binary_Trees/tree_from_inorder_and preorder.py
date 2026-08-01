#construction of tree from inorder and preorder traversal
from simple_node import BinaryTreeNode, print_binary_tree_detailed

def construct_tree_from_inorder_preorder(inorder, preorder, inS, inE, preS, preE):
    #base condition
    if (inS > inE) or (preS > preE):
        return None

    root_data = preorder[preS]
    root = BinaryTreeNode(root_data)

    linS = inS
    linE =
    lpreS =
    lpreE =

    rinS = 
    rinE =
    rpreS =
    rpreE = 
    
    root.left = construct_tree_from_inorder_preorder(inorder, preorder, linS, linE, lpreS, lpreE)
    root.right = construct_tree_from_inorder_preorder(inorder, preorder, rinS, rinE, rpreS, rpreE)

    return root



