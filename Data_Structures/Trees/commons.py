class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

root = TreeNode(1)  
child1 = root.children.append(2)
child2 = root.children.append(3)     

print(root.children)