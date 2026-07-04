def binary_sort(arr, target):
    "this function is used to perform binary sorting on elements given in array to find target value's index, if present in array"

    array_len  = len(arr)

    start = 0
    end = array_len - 1

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid+1

    return -1 


print(binary_sort(arr=[12, 23, 45, 67, 89], target=8))