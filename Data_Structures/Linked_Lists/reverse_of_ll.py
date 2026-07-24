from commons import print_ll, create_ll_from_list, Node

head = create_ll_from_list([2,1,4,5,6])

def reverse_of_ll(head):
    if head == None:
        return None
    
    if head.next == None:
        return head
    
    small_answer = reverse_of_ll(head.next)
    temp = small_answer
    while temp.next != None:
        temp = temp.next
    temp.next = head
    head.next = None    

    return small_answer


head_rev = reverse_of_ll(head)
print("reverse ll")
print_ll(head_rev)
