from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Please enter a natural number different from 0!")
    number = 0
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float or int(user_number) == 0:
            print("You must enter a natural number different from 0!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def find_number_properties(number_itself) -> list:
    number_of_digits = 0
    sum_of_digits = 0
    first_digit = 0
    number_operated_1 = number_itself
    while number_operated_1 > 0:
        if number_operated_1 // 10 == 0:
            first_digit = number_operated_1
        number_of_digits = number_of_digits + 1
        sum_of_digits = sum_of_digits + (number_operated_1 % 10)
        number_operated_1 = number_operated_1 // 10

    number_operated_2 = number_itself
    lawful_sum = 0
    if number_of_digits % 2 == 0:
        coefficient = 1
    else:
        coefficient = -1
    while number_operated_2 > 0:
        coefficient = -coefficient
        lawful_sum = lawful_sum + coefficient*(number_operated_2 % 10)
        number_operated_2 = number_operated_2 // 10

    return [number_of_digits, sum_of_digits, first_digit, lawful_sum]


def output(number_properties) -> None:
    print("The number of digits equals to ->", number_properties[0])
    print("The sum of digits equals to ->", number_properties[1])
    print("The first digit equals to ->", number_properties[2])
    print("The lawful sum of digits equals to ->", number_properties[3])


operated_number = getting_number()
user_number_properties = find_number_properties(operated_number)
output(user_number_properties)
