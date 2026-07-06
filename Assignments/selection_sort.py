def selection_sorting(arr):
    """this function using selection sorting technique"""
    
    
    for i in range(len(arr)):
        min_element = i
        for j in range(i+1, len(arr)):
            if arr[min_element] > arr[j]:
                min_element = j
            arr[min_element], arr[i] = arr[i], arr[min_element]    
    return arr

print(selection_sorting(arr=[10, 23, 45, 67, 12]))        