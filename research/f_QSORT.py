def q_sort(input_list, start, finish) -> tuple:
    comp = 0
    move = 0
    middle = input_list[(start + finish)//2]
    left = start
    right = finish
    while left < right:
        comp += 3
        while input_list[left] < middle:
            left += 1
            comp += 1
        while input_list[right] > middle:
            right -= 1
            comp += 1
        if left <= right:
            input_list[left], input_list[right] = input_list[right], input_list[left]
            left += 1
            right -= 1
            move += 1
    # comp += 1
    if start < right:
        stat = q_sort(input_list, start, right)
        move += stat[2]
        comp += stat[1]
    # comp += 1
    if left < finish:
        stat = q_sort(input_list, left, finish)
        move += stat[2]
        comp += stat[1]

    return input_list, comp, move
