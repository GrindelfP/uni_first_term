def bubble_sort_2(input_list: list) -> list:
    for outer_times in range(len(input_list)):
        for index in range(0, len(input_list) - outer_times - 1):
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]

    return input_list
