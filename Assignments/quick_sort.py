def partitionFunction(l1, s, e):
    pass

def quicksorting(l1, s, e):
    if (s >= e):
        return 

    pivotIndex = partitionFunction(l1,s, e)

    quicksorting(l1, s, pivotIndex-1)
    quicksorting(l1, pivotIndex+1, e)