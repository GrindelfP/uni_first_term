def cocktail_sort(input_list: list) -> list:
    movements_done: bool = True
    start_point: int = 0
    end_point: int = len(input_list) - 1

    while movements_done and start_point < end_point:
        movements_done = False

        for i in range(start_point, end_point):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                movements_done = True

        if not movements_done:
            break
        end_point -= 1
        movements_done = False

        for i in range(end_point, start_point - 1, -1):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                movements_done = True

        start_point += 1

    return input_list
