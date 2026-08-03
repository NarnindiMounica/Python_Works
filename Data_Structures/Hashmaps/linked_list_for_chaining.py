class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value= value
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None

    def add(self, key, value):
        new_node = LLNode(key, value)
        if self.head == None:
            new_node.next = self.head
            self.head = new_node


