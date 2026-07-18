from commons import Node, take_input_better, print_ll

head = take_input_better()
print("Linked List Before Insertion")
print_ll(head)

def insert_at_head(head, data):
    new_node = Node(value=data)

    new_node.next = head
    head = new_node

    return head

head_after_insertion = insert_at_head(head, data=12)
print("\nLinked List After Insertion")
print_ll(head_after_insertion)