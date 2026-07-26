class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

root = TreeNode(1) 
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)
child4 = TreeNode(5)
child5 = TreeNode(6) 

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

child1.children.append(child4)

child4.children.append(child5)
  
def print_tree(node):
    if root == None: #edge case, but not base case
        return
    print(node.data)
    for eachChild in node.children:
        print_tree(eachChild)

#print_tree(root)

def print_tree_detailed(node):
    if root == None:
        return

    print(f"{node.data}:", end = " ")
    for eachChild in node.children:
        print(eachChild.data, end=",")
    print()
    for eachChild in node.children:    
        print_tree_detailed(eachChild)

print_tree_detailed(root)        


