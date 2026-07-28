from generic_trees_input import predefined_generic_trees


def get_tree_height(root):
    if root == None:
        return 0
    height = 1
    max_child_height = 0
    for each_child in root.children:
        max_child_height = max(max_child_height, get_tree_height(each_child)) 
    height = height + max_child_height    
    return height

root1, root2, root3 = predefined_generic_trees()
print(get_tree_height(root1))
print(get_tree_height(root2))
print(get_tree_height(root3)