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
        
    
    def search_helper(self, data, node):
        if node == None:
            return False

        if node.data == data:
            return True

        if data < node.data:
           return self.search_helper(data, node.left)

        else:
           return  self.search_helper(data, node.right)

    def search(self,data):
        return self.search_helper(data, self.root)    

    def delete_helper(self, data, node):
        if node == None:
            return None

        if data < node.data:
            node.left = self.delete_helper(data, node.left)
        elif data > node.data:
            node.right = self.delete_helper(data, node.right)

        if data == node.data and node.left == None:
            return node.right
        elif data == node.data and node.right == None:
            return node.left        

    def delete(self, data):
        self.root = self.delete_helper(data, self.root)
        return self.root



bst_obj = BST()

bst_obj.insert(10)
bst_obj.insert(25)
bst_obj.insert(30)
print(bst_obj.search(35))
print(bst_obj.search(25))