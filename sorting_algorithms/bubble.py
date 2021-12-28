def bubble_sort(input_list: list) -> list:
    for first in range(len(input_list)):
        for index in range(0, len(input_list) - 1):
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]

    return input_list
