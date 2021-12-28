def q_sort(input_list: list, start: int, finish: int) -> list:
    middle: int or float = input_list[(start + finish)//2]
    left: int = start
    right: int = finish
    while left < right:
        while input_list[left] < middle:
            left += 1
        while input_list[right] > middle:
            right -= 1
        if left <= right:
            input_list[left], input_list[right] = input_list[right], input_list[left]
            left += 1
            right -= 1
    if start < right:
        q_sort(input_list, start, right)
    if left < finish:
        q_sort(input_list, left, finish)

    return input_list
