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
    
    def search(self, data):
        if self.root == None:
            return False

        if self.root.data == data:
            return True
        

    def delete(self, data):
        pass