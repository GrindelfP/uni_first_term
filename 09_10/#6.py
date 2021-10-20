from math import sqrt
from personal_library.number_operating import know_type_of_input, make_number


def input_check(operated_input) -> bool:
    if know_type_of_input(operated_input) is str:
        return False
    else:
        return True


def communication() -> list:
    print("Hello there! I'm Obi-Wan. Please, enter your a, b & c coefficients for your 'ax^2 + bx + c = 0' "
          "equalization:")
    coefficients = []

    flag_a = True
    while flag_a:
        a = input("a = ")
        if input_check(a):
            coefficients.append(make_number(a))
            flag_a = False
        else:
            print("Use only integers or float numbers! Try again!")

    flag_b = True
    while flag_b:
        b = input("b = ")
        if input_check(b):
            coefficients.append(make_number(b))
            flag_b = False
        else:
            print("Use only integers or float numbers! Try again!")

    flag_c = True
    while flag_c:
        c = input("c = ")
        if input_check(c):
            coefficients.append(make_number(c))
            flag_c = False
        else:
            print("Use only integers or float numbers! Try again!")

    return coefficients


def computing(a, b, c) -> list:
    result = []
    if a == 0 and b == 0 and c == 0:
        result = [".......... -> any number :)\n"
                  "The problem is that your equalization makes no sense! Try another coefficients!"]
    else:
        if a != 0 and b != 0 and c != 0:  # with all the coefficients not equal to 0
            if b ** 2 - 4 * a * c < 0:
                result = ["EMPTY SET"]
            else:
                x_1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
                x_2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
                result = [x_1, x_2]

        elif a == 0 and c != 0:  # with coefficient "a" equal to 0
            if b == 0:
                result = ["Your equalization is totally wrong! Try another coefficients!"]
            else:
                x = -c / b
                result = [x]

        elif b == 0 and a != 0:
            if c > 0:
                result = ["EMPTY SET"]
            elif c == 0:
                result = [0]
            else:
                x_1 = sqrt(-c / a)
                x_2 = -sqrt(-c / a)
                result = [x_1, x_2]

        elif c == 0 and a != 0:
            if b == 0:
                result = [0]
            else:
                x_1 = 0
                x_2 = -b / a
                result = [x_1, x_2]

    return result


coefficients_of_user = communication()

answers = computing(a=coefficients_of_user[0], b=coefficients_of_user[1], c=coefficients_of_user[2])

if len(answers) > 1:
    print("Your answer is: \n", "x_1 = ", answers[0], "\n", "x_2 = ", answers[1])
else:
    print("Your answer is:", answers[0])
