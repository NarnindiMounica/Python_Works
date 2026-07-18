from commons import Node, take_input_better




def length_of_ll(head):
    ll_len = 0
    if head==None:
        return 0
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
            ll_len = ll_len + 1

    return ll_len        
head_of_ll = take_input_better()
len_of_ll = length_of_ll(head=head_of_ll)
print(f"Length of Linked List: {len_of_ll}")