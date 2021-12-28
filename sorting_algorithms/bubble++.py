def bubble_sort_3(input_list: list) -> list:
    flag: bool = True
    while flag:
        flag = False
        for index in range(0, len(input_list) - 1):
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
                flag = True

    return input_list
