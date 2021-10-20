from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Введите натуральное число больше 3!")
    number = 0
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float or int(user_number) < 4:
            print("Вы должны ввести натуральное число, большее 3!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def calculating(users_number):
    i = 4
    counter = users_number
    v_i_1 = 1.5
    v_i_2 = v_i_3 = 0
    v_i = 0
    while counter > 3:
        v_i = ((i + 1)/(i**2 + 1))*v_i_1 - v_i_2*v_i_3
        v_i_3 = v_i_2
        v_i_2 = v_i_1
        v_i_1 = v_i
        i = i + 1
        counter = counter - 1

    return v_i


print(calculating(getting_number()))
