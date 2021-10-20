from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Введите натуральное число больше 2!")
    number = 0
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float \
                or make_number(user_number) < 3:
            print("Вы должны ввести натуральное число, большее 2!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def calculating(users_number):
    u_i_1 = u_i_2 = 0
    v_i_1 = v_i_2 = 1
    u_i = 0
    v_i = 0
    counter = users_number
    i = 3
    while counter > 2:
        u_i = (u_i_1 - u_i_2*v_i_1 - v_i_2)/(1 + u_i_1**2 + v_i_1**2)
        v_i = (u_i_1 - v_i_1)/(abs(u_i_2 + v_i_1) + 2)
        u_i_2 = u_i_1
        u_i_1 = u_i
        v_i_2 = v_i_1
        v_i_1 = v_i
        counter = counter - 1
        i = i + 1

    return u_i, v_i


results = calculating(getting_number())
print("v_i =", results[1], "\nu_i =", results[0])
