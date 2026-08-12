from simple_node import BinaryTreeNode, print_binary_tree_detailed
import take_input_binary_tree


def inorder_traversal(root, in_order_list=[]):
    """
    Function to perform inorder traversal of a binary tree.
    :param root: TreeNode -> root of the binary tree
    :return: List[int] -> list of nodes in inorder
    """
    
    # TODO: Implement this function
    if root == None:
        return []
    
    
    if root.left is not None:
        inorder_traversal(root.left, in_order_list)
        
    
    in_order_list.append(root.data) 
      
    
    if root.right is not None:
        inorder_traversal(root.right, in_order_list)
    
    return in_order_list


root = take_input_binary_tree.take_input_for_binary_tree()
print_binary_tree_detailed(root)
print(inorder_traversal(root, []))
print(inorder_traversal(root, []))

###with helper function


# def inorder_traversal(root):
    
#     def inorder_traversal_helper(root, in_order_list=[]):

#         """
#         Function to perform inorder traversal of a binary tree.
#         :param root: TreeNode -> root of the binary tree
#         :return: List[int] -> list of nodes in inorder
#         """
        
#         # TODO: Implement this function
#         if root == None:
#             return []
        
        
#         if root.left is not None:
#             inorder_traversal_helper(root.left, in_order_list)
            
        
#         in_order_list.append(root.val) 
          
        
#         if root.right is not None:
#             inorder_traversal_helper(root.right,in_order_list)
        
#         return in_order_list
        
#     return inorder_traversal_helper(root, [])
    
        