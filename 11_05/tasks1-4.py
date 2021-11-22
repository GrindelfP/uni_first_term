def first_task(operated_list):
    sigma = 0
    for sigma_element in operated_list:
        sigma += sigma_element
    return sigma


def second_task(operated_list, determined_value):
    sigma = 0
    for sigma_element in operated_list:
        if sigma_element == determined_value:
            sigma += sigma_element
    return sigma


def third_task(operated_list, mode):
    if mode == "min":
        minim = operated_list[0]
        for element in operated_list:
            if minim > element:
                minim = element
        return minim
    else:
        maxim = operated_list[0]
        for element in operated_list:
            if maxim < element:
                maxim = element
        return maxim


def forth_task(operated_list, value, index_place):
    if index_place == "f":
        for index in range(0, len(operated_list)):
            if operated_list[index] == value:
                return index
    else:
        looked_index = 0
        for index in range(0, len(operated_list)):
            if operated_list[index] == value:
                looked_index = index
        return looked_index


input_list_length = int(input("Enter len of your list (using integers): "))
input_value = int(input("To what summed numbers should equal: "))
mode_of_max_min = input("We should look for minimum or maximum element? (min/max): ")
place_of_index = input("You are looking for first or last index of that value? (f/l): ")
main_list = []
for i in range(input_list_length):
    new_element = int(input("-> "))
    main_list.append(new_element)
looked_element = third_task(main_list, mode_of_max_min)

print(first_task(main_list), "\n",
      second_task(main_list, input_value), "\n",
      looked_element, "\n",
      forth_task(main_list, looked_element, place_of_index))
