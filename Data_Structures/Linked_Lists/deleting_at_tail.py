from commons import print_ll, take_input_better


def deletion_at_tail(head):
    if head == None:
        return None
    if head.next == None:
        return None
    head.next = deletion_at_tail(head.next)

    return head

head = take_input_better()
head_after_deletion = deletion_at_tail(head)
print("Linked List after deletion at tail:")
print_ll(head_after_deletion)
