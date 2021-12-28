def SortBubble(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def SortEnhancedBubble2(arr):
    last = len(arr)-1
    for i in range(0, len(arr)):
        changes = 0
        for j in range(0, last):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                changes += 1
                last = j
        if changes == 0:
            break
    return arr
print(SortBubble([3, 5, 6, 2, 43, 2, 4, 1]))
