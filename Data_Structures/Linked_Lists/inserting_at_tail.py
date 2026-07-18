from commons import Node, print_ll, take_input_better

head = take_input_better()
print("Linked List Before Insertion")
print_ll(head)

def insert_at_tail(head, data):
    new_node = Node(value=data)

    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = new_node  

    return head

head_after_insertion = insert_at_tail(head, data=12)
print("\nLinked List After Insertion")
print_ll(head_after_insertion)
