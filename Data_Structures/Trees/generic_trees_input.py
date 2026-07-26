from commons import TreeNode, print_tree_detailed

def predefined_generic_trees():

    #tree 1

    root1 = TreeNode(data=1)
    child1 = TreeNode(data=2)
    child2 = TreeNode(data=3)
    child3 = TreeNode(data=4)
    child4 = TreeNode(data=5)

    root1.children.append(child1)
    root1.children.append(child2)
    child1.children.append(child3)
    child1.children.append(child4)

    # tree 2

    root2 = TreeNode(data=10)
    child1 = TreeNode(data=20)
    child2 = TreeNode(data=30)
    child3 = TreeNode(data=40)

    root2.children.append(child1)
    root2.children.append(child2)
    root2.children.append(child3)

    child2.children.append(TreeNode(data=50))
    child2.children.append(TreeNode(data=60))

    #tree 3
    root3 = TreeNode(data=100)
    child1 = TreeNode(data=200)
    root3.children.append(child1)
    root3.children.append(TreeNode(data=300))

    child1.children.append(TreeNode(data=400))
    child1.children.append(TreeNode(data=500))

    return root1, root2, root3
