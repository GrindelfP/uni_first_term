def bubble_sort(input_list) -> tuple:
    comp = 0
    move = 0
    for first in range(len(input_list)):
        for index in range(0, len(input_list) - 1):
            comp += 1
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
                move += 1
    return input_list, comp, move


def bubble_sort_2(input_list) -> tuple:
    comp = 0
    move = 0
    for first in range(len(input_list)):
        for index in range(0, len(input_list) - first - 1):
            comp += 1
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
                move += 1

    return input_list, comp, move


def bubble_sort_3(input_list) -> tuple:
    comp = 0
    move = 0
    flag = True
    while flag:
        flag = False
        for index in range(0, len(input_list) - 1):
            comp += 1
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
                move += 1
                flag = True

    return input_list, comp, move
