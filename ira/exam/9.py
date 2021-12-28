def SortSelect(arr):
	for i in range(0, len(arr) - 1):	
		minelement = arr[i]
		minindex = i
		for j in range(i, len(arr)):
			if arr[j] < minelement:
				minelement = arr[j]
				minindex = j
		arr[i], arr[minindex] = arr[minindex], arr[i]
	return arr
