def cocktail_sort(input_list) -> tuple:
    comp = 0
    move = 0
    movements_done = True
    start_point = 0
    end_point = len(input_list) - 1

    while movements_done and start_point < end_point:
        movements_done = False

        for i in range(start_point, end_point):
            comp += 1
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                movements_done = True
                move += 1

        if not movements_done:
            break
        end_point -= 1
        movements_done = False

        for i in range(end_point, start_point - 1, -1):
            comp += 1
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                movements_done = True
                move += 1

        start_point += 1

    return input_list, comp, move
