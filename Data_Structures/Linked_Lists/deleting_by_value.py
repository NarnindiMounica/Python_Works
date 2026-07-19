from commons import print_ll, take_input_better

def deleting_node_by_value_all_occurrence(head, value):

    if head==None:  #empty linked list
        return None
    
    if head.data == value:
        return head.next
    
    temp = head
    while temp is not None and temp.next is not None:
        if temp.next.data == value:
            temp.next = temp.next.next
        temp = temp.next    

    return head

# head = take_input_better()
# head_after_deletion = deleting_node_by_value_all_occurrence(head, value=20)
# print_ll(head_after_deletion)
    

def deleting_node_by_value_first_occurrence(head, value):

    if head == None:
        return None
    
    if head.data == value:
        return head.next
    
    temp = head
    
    while temp.next != None and temp.next.data != value:
        temp = temp.next

    if temp.next == None: # to handle case if value is not in given linked list  
        return head  

    temp.next = temp.next.next

    return head  

head = take_input_better()
head_after_deletion = deleting_node_by_value_first_occurrence(head, value=20)
print_ll(head_after_deletion)  

