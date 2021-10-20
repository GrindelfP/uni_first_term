from math import factorial, sin, sqrt, cos

from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Please enter a natural number!")
    number = 0
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float or int(user_number) == 0:
            print("You must enter a natural number (also it must be different from 0)!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def print_results(r1, r2, r3, r4, r5, r6, r7) -> None:
    print("a)", r1)
    print("б)", r2)
    print("в)", r3)
    print("г)", r4)
    print("д)", r5)
    print("е)", r6)
    print("ж)", r7)


NUMBER = getting_number()

# а
result_1 = 2 ** NUMBER

# б
result_2 = factorial(NUMBER)

# в
number_3 = NUMBER
result_3 = 1
while number_3 > 0:
    result_3 = result_3 * (1 + (1 / (number_3 ** 2)))
    number_3 = number_3 - 1

# г
number_4 = NUMBER
result_4 = 0
while number_4 > 0:
    number_4_sin = number_4
    sum_of_sin = 0
    while number_4_sin > 0:
        sum_of_sin = sum_of_sin + sin(number_4_sin)
        number_4_sin = number_4_sin - 1
    result_4 = result_4 + (1/sum_of_sin)
    number_4 = number_4 - 1

# д
number_5 = NUMBER
result_5 = 0
while number_5 > 0:
    result_5 = sqrt(2 + result_5)
    number_5 = number_5 - 1

# е
number_6 = NUMBER
result_6 = 1
while number_6 > 0:
    number_6_sin = number_6
    sum_of_sin = 0
    while number_6_sin > 0:
        sum_of_sin = sum_of_sin + sin(number_6_sin)
        number_6_sin = number_6_sin - 1
    number_6_cos = number_6
    sum_of_cos = 0
    while number_6_cos > 0:
        sum_of_cos = sum_of_cos + cos(number_6_cos)
        number_6_cos = number_6_cos - 1

    result_6 = result_6 * (sum_of_cos/sum_of_sin)
    number_6 = number_6 - 1

# ж
number_7 = NUMBER
result_7 = 0
while number_7 > 0:
    result_7 = sqrt(3*number_7 + result_7)
    number_7 = number_7 - 1

print_results(result_1, result_2, result_3, result_4, result_5, result_6, result_7)
