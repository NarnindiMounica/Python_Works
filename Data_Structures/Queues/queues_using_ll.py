class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class QueueFromLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = Node(value=value)
        self.size += 1

        if self.head==None:
            self.head = new_node
            self.tail = new_node
            self.head.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node

        return f"{value} is enqueued in queue"
         



