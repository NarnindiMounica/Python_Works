from commons import Node, create_ll_from_list, print_ll

head1 = create_ll_from_list([1, 3, 4, 6])
head2 = create_ll_from_list([2, 5, 7, 8, 9, 10])

def merge_sorted_ll(head1, head2):

    if head1 == None:
        return head2 
    
    if head2 == None:
        return head1
    
    final_head = None
    final_tail = None

    while 