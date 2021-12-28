# бинарный поиск работает только для отсортированных массивов
def Bin_Search(arr, el):
    left = -1
    right = len(arr)
    while right > left + 1:
        middle = (left + right) // 2
        if arr[middle] == el:
            return middle
        if arr[middle] > el:
            right = middle
        else:
            left = middle
    return -1


print(Bin_Search([1, 2 ,3 ,4 ,5 , 7, 8], 3))
