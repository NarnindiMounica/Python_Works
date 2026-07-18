class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_ll(head):
    temp = head

    while temp != None:
        print(temp.data, end= "->")
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

#big O time complexity of this function is O(n^2), to improve this we need to write better function

def take_input_better():

    value = int(input("Enter value of a node:"))
    head = None
    tail = None

    while value != -1:
        new_node = Node(value=value)
        if head == None and tail == None:
            
            head = tail = new_node
        else:
            tail.next = new_node
            tail = tail.next


        value = int(input("Enter value of a node:")) 
        return head
    
   
  