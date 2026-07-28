from generic_trees_input import predefined_generic_trees

def preorder_traversal(root):

    # edge case
    if root == None:
        return None
    
    print(f'{root.data}', end = ' ')

    for eachChild in root.children:
        preorder_traversal(eachChild)

        

root1, root2, root3 = predefined_generic_trees()
preorder_traversal(root1)
print()
preorder_traversal(root2)
print()
preorder_traversal(root3)


def postorder_traversal(root):
    if root == None:
        return None

    for eachChild in 