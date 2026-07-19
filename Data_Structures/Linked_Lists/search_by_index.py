from commons import print_ll, create_ll_from_list


def search_by_index(head, index):

    if head == None: # empty linked list
        return None
    
    inx_count = 0
    temp = head
    
    while temp != None:
        if inx_count==index:
            return temp.data
        temp = temp.next
        inx_count = inx_count + 1

    return None    


head = create_ll_from_list([1,2,3,4,5])
print(search_by_index(head=head, index=-1))