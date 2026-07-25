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


    def dequeue(self):
        if self.get_size()==0:
            return "Cannot dequeue element from empty queue"
        temp = self.head.data
        self.head = self.head.next
        self.size -= 1
        return f"{temp} dequeued from queue"


queue_from_list = QueueFromList()

print(queue_from_list.is_empty())
print(queue_from_list.enqueue(2))
print(queue_from_list.enqueue(3))
print(queue_from_list.get_size())
print(queue_from_list.dequeue())
print(queue_from_list.front()) 

         



