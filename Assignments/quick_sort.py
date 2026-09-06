def partitionFunction(l1, s, e):
    pivot = l1[e]
    i = s

    rightPosition = s

    while(i <= e-1):
        if (l1[i]<pivot):
            rightPosition += 1

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