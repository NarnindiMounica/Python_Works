from bst_node_and_printing import BSTNode, print_bst


def sortedListToBST(lst:list):
    if len(lst) == 0:
        return None

    mid = len(lst)//2
    rootData = lst[mid]
    root = BSTNode(data=rootData)

    root.left = sortedListToBST(lst[:mid])
    root.right = sortedListToBST(lst[mid+1:])

    return root

root = sortedListToBST(lst=[1,2,3,4,5,6,7,8])
print_bst(root)

        