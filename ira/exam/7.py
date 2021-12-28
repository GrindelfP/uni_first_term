def SortBubble(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def SortEnhancedBubble2(arr):
    flag = True
    while flag:
        flag = False
        for index in range(0, len(arr) - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                flag = True

    return arr

print(SortBubble([3, 5, 6, 2, 43, 2, 4, 1]))
