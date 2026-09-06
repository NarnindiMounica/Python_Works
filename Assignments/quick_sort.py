def partitionFunction(l1, s, e):
    pivot = l1[e]
    i = s

    rightPosition = s

    while(i <= e-1):
        if (l1[i]<pivot):
            rightPosition += 1
        i += 1
    l1[rightPosition], l1[e] = l1[e], l1[rightPosition] 

    pivotIndex = rightPosition  

    #now make sure that everything smaller than pivot is on left and greater than pivot on the right
    start = s
    end = e

    while (start<pivotIndex and end>pivotIndex):
        if(l1[start]< pivot):
            start += 1
        elif(l1[end] >= pivot):
            end -= 1
        else:
            l1[start], l1[end] = l1[end], l1[start]                     

def quicksorting(l1, s, e):
    if (s >= e):
        return 

    pivotIndex = partitionFunction(l1,s, e)

    quicksorting(l1, s, pivotIndex-1)
    quicksorting(l1, pivotIndex+1, e)

    return

l1 = [3,6,7,2,1,4,5]
quicksorting(l1, s=0, e=len(l1)-1)
print(l1)