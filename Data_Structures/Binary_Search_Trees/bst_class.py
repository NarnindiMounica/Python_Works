class BSTNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        pass
    
    def search_helper(self, data, root):
        if self.root == None:
            return False

        if self.root.data == data:
            return True

        if data < self.root.data:
           return self.search_helper(self, data, root.left)

        else:
           return  self.search_helper(self, data, root.right)

    def search(self,data):
        return self.search_helper(self, data, self.root)    

    def delete(self, data):
        pass