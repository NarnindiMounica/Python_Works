#constructing a tree from inorder and postorder traversal

from simple_node import BinaryTreeNode, print_binary_tree_detailed

def construct_tree_from_inorder_postorder(inorder, postorder, inS, inE, postS, postE):
    if (inS > inE) or (postS > postE):
        return None

    root_data = postorder[postE]
    root = BinaryTreeNode(root_data)

    rootindex_in_inorder = -1
    for i in range(inS, inE+1):
        if root_data == inorder[i]:
            rootindex_in_inorder = i
            break

    if rootindex_in_inorder == -1:
        print("Root index not found in inorder, please check logic")

    linS = inS
    linE = rootindex_in_inorder - 1
    lpostS = postS
    lpostE = lpostS + linE - linS

    rinS = rootindex_in_inorder + 1
    rinE = inE
    rpostS = lpostE + 1
    rpostE =   postE - 1

    root.left = construct_tree_from_inorder_postorder(inorder, postorder, linS, linE, lpostS, lpostE)    
    root.right = construct_tree_from_inorder_postorder(inorder, postorder, rinS, rinE, rpostS, rpostE) 

    return root

inorder = [5, 4, 2, 1, 3, 6]
postorder = [5, 4, 2, 6, 3, 1]
n = len(inorder)
root = construct_tree_from_inorder_postorder(inorder, postorder, 0, n-1, 0, n-1)
print_binary_tree_detailed(root)