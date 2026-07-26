from generic_trees_input import predefined_generic_trees

def count_of_nodes(root):
    if root == None:
        return 0

    node_count = 1
    for eachchild in root.children:
       node_count += count_of_nodes(eachchild)

    return node_count
root1, root2, root3 = predefined_generic_trees()
print(count_of_nodes(root1))
print(count_of_nodes(root2))
print(count_of_nodes(root3))