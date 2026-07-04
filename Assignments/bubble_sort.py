def bubble_sorting(arr):
    "this fucntion is used to perform bubble sorting"
    arr_len = len(arr)
    for j in range(arr_len):
        for i in range(arr_len-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr        

arr = [89, 23, 45, 12, 3]
print(bubble_sorting(arr))            