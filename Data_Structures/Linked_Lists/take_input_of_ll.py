class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_ll(head):
    temp = head

    while temp != None:
        print(temp.data)
        temp = temp.next  

    return       
        
def take_input():
    value = int(input("Enter a value of node: "))
    head = None
    
    while value != -1:
        new_node = Node(value=value)
        if head == None:
            head = new_node
            
        else:
            temp = head
            while temp.next != None:
                temp = temp.next
                
            temp.next = new_node         

        value = int(input("Enter a value of node: "))

    print_ll(head)
    return

take_input()