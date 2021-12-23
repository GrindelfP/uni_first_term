import random


def create_list(n, top_edge) -> list:
    sequence = []
    for time in range(0, n):
        sequence.append(random.randint(0, top_edge))
    return sequence


def find_max(sequence) -> int:
    max_element = 0
    for element in sequence:
        if element > max_element:
            max_element = element
    return max_element


n_num = int(input("n = "))
max_allowed_int = int(input("Enter your max integer: "))
the_sequence = create_list(n_num, max_allowed_int)
max_int_el = find_max(the_sequence)
print(the_sequence)
print("Max element:", max_int_el)
cleared_sequence = []
for element_2 in the_sequence:
    if element_2 != max_int_el:
        cleared_sequence.append(element_2)
print(cleared_sequence)
