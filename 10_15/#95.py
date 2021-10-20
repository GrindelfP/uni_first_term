from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Введите натуральное число большее 1!")
    number = 0
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float \
                or make_number(user_number) < 2:
            print("Вы должны ввести натуральное число большее 1!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def calculating(users_number):
    a_0 = a_1 = 1
    a_i = 0
    a_i_1 = a_1
    a_i_2 = a_0
    result = 1
    counter = users_number
    i = 2
    while counter > 1:
        a_i = a_i_2 + a_i_1 / (2 ** a_i_1)
        a_i_2 = a_i_1
        a_i_1 = a_i
        result = result * a_i
        counter = counter - 1
        i = i + 1

    return a_i


print(calculating(getting_number()))
