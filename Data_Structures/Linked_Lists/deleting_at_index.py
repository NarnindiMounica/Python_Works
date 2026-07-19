from commons import Node, print_ll, take_input_better


def delete_at_index(head, inx):

    if inx == 0:
        return head.next
    
    count = 0
    temp = head
    while temp != None and temp.next != None:
        if count == inx-1:
            temp.next = temp.next.next
            break
        count = count + 1
        temp = temp.next
        
    return head

head = take_input_better()
head_after_deletion = delete_at_index(head, inx=100)
print_ll(head_after_deletion)


