from commons import TreeNode, print_tree_detailed

def take_input():

    data = input("Enter data of the node: ")
    node = TreeNode(data)

    num_of_children = int(input(f"Enter number of children of the node {data}: "))
    for _ in range(num_of_children):
        child = take_input()
        print(child)
        node.children.append(child)

    return node

root_node = take_input()
print_tree_detailed(root_node)




