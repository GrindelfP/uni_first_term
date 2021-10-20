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


def calculation(operated_number) -> int or float:
    augend_1 = 1
    augend_2 = 2
    result = 1
    while augend_1 < 64 and augend_2 < 65:
        if (operated_number - augend_1) == 0:
            return "Your problem is unsolvable!"
        result = (result*(operated_number - augend_2))/(operated_number - augend_1)
        augend_1 = augend_1 + 2
        augend_2 = augend_2 + 2
    return result


users_number = getting_number()
print("Here is your result:", calculation(users_number))
