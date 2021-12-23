def shell_sorting(input_list) -> tuple:
    comp = 0
    move = 0
    step = len(input_list) // 2
    while step > 0:
        for i in range(step, len(input_list)):
            tmp = input_list[i]
            hole = i
            comp += 1
            while hole > step - 1 and input_list[hole - step] > tmp:
                hole -= step
                input_list[hole + step], input_list[hole] = input_list[hole], input_list[hole + step]
                move += 1
        step //= 2
    return input_list, comp, move
