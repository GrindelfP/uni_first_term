def min_and_max(arr):
    min_value = arr[0]
    i_min = 0
    max_value = arr[0]
    i_max = 0
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            i_max = i
        if arr[i] < min_value:
            min_value = arr[i]
            i_min = i
    return max_value, min_value, i_max, i_min
