def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
    L[i] = arr[l + i]
    for j in range(0, n2):