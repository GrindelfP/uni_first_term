def bubble_sort_4(input_list) -> list:
    start_index = 0
    for first in range(len(input_list)):
        for index in range(start_index, len(input_list) - first - 1):
            start_index = -1
            if input_list[index] > input_list[index + 1]:
                start_index = 0
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
            else:
                start_index = start_index + 1
    return input_list
