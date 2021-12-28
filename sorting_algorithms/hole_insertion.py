def hole_insertion_sort(input_list: list) -> list:
    for i in range(0, len(input_list)):
        tmp: int = input_list[i]
        hole: int = i
        while hole > 0 and input_list[hole - 1] > tmp:
            hole -= 1
            input_list[hole + 1], input_list[hole] = input_list[hole], input_list[hole + 1]

    return input_list
