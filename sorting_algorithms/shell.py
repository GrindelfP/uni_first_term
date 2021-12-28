def shell_sorting(input_list: list) -> list:
    step: int = len(input_list) // 2
    while step > 0:
        for i in range(step, len(input_list)):
            tmp: list = input_list[i]
            hole: int = i
            while hole > step - 1 and input_list[hole - step] > tmp:
                hole -= step
                input_list[hole + step], input_list[hole] = input_list[hole], input_list[hole + step]
        step //= 2
    return input_list
