class BSTNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert_helper(self, data, node):
        if node == None:
            node = BSTNode(data)
            return node

        if data < node.data:
            node.left = self.insert_helper(data,node.left)
        else:
            node.right = self.insert_helper(data,node.right)
        return node        


    def insert(self, data):
        self.root = self.insert_helper(data,self.root)  
        return self.root
        
    
    def search_helper(self, data, root):
        if self.root == None:
            return False

        if self.root.data == data:
            return True

        if data < self.root.data:
           return self.search_helper(data, root.left)

        else:
           return  self.search_helper(data, root.right)

    def search(self,data):
        return self.search_helper(data, self.root)    

    def delete(self, data):
        pass



bst_obj = BST()

bst_obj.insert(10)
bst_obj.insert(25)
bst_obj.insert(30)
bst_obj.search(25)
