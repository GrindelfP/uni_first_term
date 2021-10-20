from personal_library.number_operating import make_number, my_factorial
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Введите натуральное число большее 3!")
    number = 0
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float \
                or make_number(user_number) < 4:
            print("Вы должны ввести натуральное число большее 3!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def calculating(users_number):
    x_i_1 = x_i_2 = x_i_3 = 1
    counter = users_number - 2

    i = 4
    sigma = x_i_1/(2**1) + x_i_2/(2**2) + x_i_3/(2**3)
    while counter > 1:
        x_i = x_i_1 + x_i_3
        sigma = sigma + x_i/(2**i)
        i = i + 1
        counter = counter - 1
        if counter == 1:
            break

        x_i_plus = x_i + x_i_2
        sigma = sigma + x_i_plus/(2**i)
        i = i + 1

        x_i_3 = x_i_1
        x_i_1 = x_i_plus
        x_i_2 = x_i

        counter = counter - 1

    return sigma


print(calculating(getting_number()))
