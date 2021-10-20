from math import factorial

from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Please enter a number!")
    number = 0
    flag = True
    while flag:
        user_number = input("x = ")
        if know_type_of_input(user_number) is str:
            print("You must enter a number!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def operation(operated_number) -> float:
    consequent = 1
    resulting_sum = 0
    coefficient = -1
    while consequent < 15:
        coefficient = -coefficient
        resulting_sum = resulting_sum + coefficient*(operated_number**consequent)/(factorial(consequent))
        consequent = consequent + 2

    return resulting_sum


users_number = getting_number()
print("Your result is ->", operation(users_number))
