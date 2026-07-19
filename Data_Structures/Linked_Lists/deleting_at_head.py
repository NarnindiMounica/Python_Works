from commons import Node, print_ll, take_input_better

def delete_at_head(head):

    if head == None:
        return None
    else:
        new_head = head.next
        return new_head
head = take_input_better() 
new_head = delete_at_head(head)
print("Linked list after deletion at head")
print_ll(new_head)    