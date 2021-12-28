def Just_Search(arr, el):
    for i in range(len(arr)):
        if arr[i] == el:
            return i
    return "Here is no such element"

