def SortShaker(arr):
    last = len(arr) - 1
    for i in range(0, len(arr) // 2):
        changes = 0
        j = 0
        static_last = last
        while j < static_last:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                last = j
                changes += 1
            j += 1
        if changes == 0:
            break
        changes = 0
        j = last - 1
        while j > 0:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changes += 1
            j -= 1
        if changes == 0:
            break
    return arr
