def bubble_sorting(arr):
    "this fucntion is used to perform bubble sorting"
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr        

arr = [89, 23, 45, 12, 3]
print(bubble_sorting(arr))            