from commons import Node, create_ll_from_list, print_ll

head = create_ll_from_list([1,2,3,4,5,6,7,8])
print_ll(head)

def middle_of_linked_list(head):

    len_of_ll = 0
    temp = head

    while temp.next != None:
        temp = temp.next
        len_of_ll += 1

    middle = len_of_ll//2
    
    temp = head
    count = 0
    while count < middle:
        temp = temp.next
        count += 1
    return temp.data
print()
print(middle_of_linked_list(head))        