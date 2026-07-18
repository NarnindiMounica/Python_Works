class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_ll(head):

        while head != None: 
            temp = head
            print(head.data)
            head = head.next

        return

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

head = first

print_ll(head=head)