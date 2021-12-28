def min_and_max(arr):
    min_value = arr[0]
    max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    return max_value, min_value
