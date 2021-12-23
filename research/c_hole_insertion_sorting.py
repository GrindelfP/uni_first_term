def hole_insertion_sort(input_list) -> tuple:
    comp = 0
    move = 0
    for i in range(0, len(input_list)):
        tmp = input_list[i]
        hole = i
        while hole > 0 and input_list[hole - 1] > tmp:
            comp += 1
            if hole == i:
                comp += 1
            hole -= 1
            input_list[hole + 1], input_list[hole] = input_list[hole], input_list[hole + 1]
            move += 1
    return input_list, comp, move
