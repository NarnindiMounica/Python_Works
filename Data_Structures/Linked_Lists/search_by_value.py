from commons import print_ll, create_ll_from_list


def search_by_value(head, value):
    inx = 0
    temp = head

    if temp.data == value:
        return inx
    
    while temp is not None:
        if temp.data == value:
            return inx
        temp = temp.next
        inx = inx+1

    return -1    

head = create_ll_from_list(lst=[1,2,3,4,5])
print(search_by_value(head, value=3))


