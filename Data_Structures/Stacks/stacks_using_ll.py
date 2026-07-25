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
            new_node.next = self.head
            self.head = new_node
        return f"Data {value} pushed into stack"  

    def get_size(self):
        return self.size

    def is_empty(self):
        return  self.size==0

    def top(self):
        return self.head.data

    def pop(self):

        if self.head is None or self.size == 0:
            return "Stack is empty, cannot pop an element"

        data_at_top = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data_at_top



stack_from_ll = StackFromLL()

print(stack_from_ll.is_empty())
print(stack_from_ll.push(2))
print(stack_from_ll.push(3))
print(stack_from_ll.push(4))
print(stack_from_ll.pop())
print(stack_from_ll.get_size())
print(stack_from_ll.top())




