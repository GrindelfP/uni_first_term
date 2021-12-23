def shell_sorting(input_list) -> tuple:
    comp = 0
    move = 0
    step = len(input_list) // 2
    while step > 0:
        for i in range(step, len(input_list)):
            tmp = input_list[i]
            hole = i
            comp += 1
            # print("begin", tmp, input_list[hole - step], i)
            while hole > step - 1 and input_list[hole - step] > tmp:
                # print("begin2", tmp, input_list[step-1])
                hole -= step
                # print("comp", input_list, hole, hole + step)
                input_list[hole + step], input_list[hole] = input_list[hole], input_list[hole + step]
                # print("move", input_list, hole, hole + step)
                move += 1
        step //= 2
    return input_list, comp, move


a = [33, 40, 3, 6, 35]
print(shell_sorting(a))
