from predefined_bst import create_predefined_bst

root1, root2, root3 = create_predefined_bst()


def search_in_bst(root, value):
    if root is None: 
        return False

    if root.data == value:
        return True

    if root.data < value:
        return search_in_bst(root.right, value)
    else:

       return search_in_bst(root.left, value)    

print(search_in_bst(root1, 25))
