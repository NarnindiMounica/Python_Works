def insertion_sorting(arr):
    "this function is used for insertion sort"
    num = len(arr)

    for i in range(1, num):
        current_card = arr[i]
        current_pos = i-1 #this will go from i-1 to 0

        while current_pos >= 0:
            if arr[current_pos] < current_card:
                break
            else:
                arr[current_pos+1] = arr[current_pos]
                current_pos = current_pos -1
            arr[current_pos + 1] = current_card 
    return arr


print(insertion_sorting(arr=[23, 45, 67, 12, 34]))
 