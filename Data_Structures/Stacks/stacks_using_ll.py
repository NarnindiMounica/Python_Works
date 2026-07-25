class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class StackFromLL:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, value):
        new_node = Node(value)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.head.next = None
        else:
            self.head.next=new_node
            self.head = new_node
        return f"Data {value} pushed into stack"  

    def size(self):
        return self.size

    def is_empty(self):
        return  self.size==0
       




