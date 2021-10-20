from personal_library.objects import know_type_of_input


def make_number(number_input) -> int or float:
    # receives user's input and makes it a number
    if number_input.count(',') == 1:
        number_input = number_input.replace(',', '.', 1)

    if know_type_of_input(user_input=number_input) is int:
        if int(float(number_input)) == float(number_input):
            return int(float(number_input))
        return int(number_input)
    elif know_type_of_input(user_input=number_input) is float:
        return float(number_input)


def my_factorial(number) -> int:
    if number == 0:
        return 1
    elif number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        number_1 = number - 1
        factorial = number
        while number > 2:
            factorial = factorial * number_1
            number = number_1
            number_1 = number - 1
    return factorial
