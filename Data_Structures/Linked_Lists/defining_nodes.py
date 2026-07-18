class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

first = Node(1)
second = Node(2) 

print(id(first), id(second))

first.next = second

print(id(first.next))
print(id(second))