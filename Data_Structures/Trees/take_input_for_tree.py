from commons import TreeNode, print_tree_detailed

def take_input():

    data = input("Enter data of the node: ")
    node = TreeNode(data)

    num_of_children = int(input("Enter number of children of the node: "))
    for _ in range(num_of_children):
        child = take_input()
        node.children.append(child)

    return print_tree_detailed(node)

take_input()




