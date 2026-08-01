#construction of tree from inorder and preorder traversal
from simple_node import BinaryTreeNode, print_binary_tree_detailed

def construct_tree_from_inorder_preorder(inorder, preorder, inS, inE, preS, preE):
    #base condition
    if (inS > inE) or (preS > preE):
        return None

    root_data = preorder[preS]
    root = BinaryTreeNode(root_data)
    rootindex_in_inorder = -1
    for i in range(inS, inE+1):
        if preorder[preS] == inorder[i]:
            rootindex_in_inorder = i
            break

    if rootindex_in_inorder == -1 :
        print("Root not found in inorder, please check logic")

    linS = inS
    linE = rootindex_in_inorder -1
    lpreS = preS + 1
    lpreE = lpreS + (linE - linS)

    rinS = rootindex_in_inorder + 1
    rinE = inE
    rpreS = lpreE + 1
    rpreE = preE

    root.left = construct_tree_from_inorder_preorder(inorder, preorder, linS, linE, lpreS, lpreE)
    root.right = construct_tree_from_inorder_preorder(inorder, preorder, rinS, rinE, rpreS, rpreE)

    return root



