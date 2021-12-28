def select_sorting(input_list: list) -> list:
    for i in range(len(input_list) - 1):
        for j in range(i+1, len(input_list)):
            if input_list[j] < input_list[i]:
                input_list[i], input_list[j] = input_list[j], input_list[i]

    return input_list
