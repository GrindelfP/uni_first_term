def select_sorting(input_list) -> tuple:
    comp = 0
    move = 0
    for i in range(len(input_list) - 1):
        for j in range(i+1, len(input_list)):
            comp += 1
            if input_list[j] < input_list[i]:
                move += 1
                input_list[i], input_list[j] = input_list[j], input_list[i]

    return input_list, comp, move


a = [33, 40, 3, 6, 35]
print(select_sorting(a))

