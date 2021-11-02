import random


def revert(number) -> int or float:
    if number < 0:
        return number ** 2
    else:
        return number


def order_check(input_list) -> bool:
    previous_element = -1
    testing_number = 0
    for element in input_list:
        if element >= previous_element:
            testing_number = testing_number + 1
            previous_element = element
    if testing_number == len(input_list):
        return True
    else:
        return False


def convert_input(users_input) -> int or float or str:
    if users_input.isdigit():
        return int(users_input)
    else:
        try:
            return float(users_input)
        except ValueError:
            return "You look weird!"


length = int(input("Введите длину последовательности -> "))
lower_limit = int(input("Введите нижнюю границу диапазона задания элементов последовательности -> "))
upper_limit = int(input("Введите верхнюю границу диапазона задания элементов последовательности -> "))
sequence = random.sample(range(lower_limit, upper_limit), length)

for index in range(0, len(sequence)):
    sequence[index] = revert(sequence[index])

if order_check(sequence):
    sigma = 0
    for element_sigma in sequence:
        sigma = sigma + element_sigma
    print("Результат:", sigma)
else:
    product = 1
    for element_product in sequence:
        product = product * element_product
    print("Результат:", product)
