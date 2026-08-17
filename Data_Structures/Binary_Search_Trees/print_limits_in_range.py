from predefined_bst import create_predefined_bst

def print_bst_in_range(root, low, high):
    if root is None:
        return None

    if low < root.data:
        print_bst_in_range(root.left, low, high)

    if root.data < high:
        print_bst_in_range(root.right, low, high)

    if low <= root.data <= high:
        print(root.data)

root1, root2, root3 = create_predefined_bst()

print_bst_in_range(root3, 30, 60)