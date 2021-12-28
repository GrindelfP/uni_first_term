def SortInsert(arr):
    for i in range(0, len(arr)):
        tmp = arr[i]
        hole = i
        while hole > 0 and arr[hole - 1] > tmp:
            hole -= 1
            arr[hole + 1], arr[hole] = arr[hole], arr[hole + 1]
    return arr
