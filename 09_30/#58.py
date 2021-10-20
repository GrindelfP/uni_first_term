# UNFINISHED!
from personal_library.number_operating import know_type_of_input, make_number


def getting_type() -> str:
    flag = True
    type_of_task = None
    while flag:
        user_input = input("Please enter the type of the task, choosing one of following {а, б, в, г}:")
        types = ["а", "б", "в", "г"]
        if user_input not in types:
            print("You must enter one of this letters: {а, б, в, г}. Try again!")
        else:
            type_of_task = user_input
            flag = False

    return type_of_task


def getting_number() -> int or float:
    print("Please enter a real number!")
    number = 0
    flag = True
    while flag:
        user_number = input("a = ")
        if know_type_of_input(user_number) is str:
            print("You must enter a real number! Try again!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def find_f_from_a(task_type, number_a) -> int or float:
    # а_type
    if task_type == "а":
        if number_a < 0:
            return -number_a
        elif number_a > 0:
            return -(number_a ** 2)
        else:
            return 0
    # б_type
    elif task_type == "б":
        if number_a < -1:
            return -(1 / (number_a ** 2))
        elif number_a > 2:
            return 4
        else:
            return number_a ** 2
    # в_type
    elif task_type == "в":
        if number_a < -1:
            return -(1 / (number_a ** 2))
        elif number_a > 2:
            return 4
        else:
            return number_a ** 2
