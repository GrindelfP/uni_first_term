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
    x_i_1 = y_i_1 = 1
    counter = users_number
    k = 2
    sigma = x_i_1/(1 + abs(x_i_1))
    print(sigma)
    while counter > 1:
        x_i = 0.3*x_i_1
        y_i = x_i_1 + y_i_1
        print(x_i)
        print(1 + abs(y_i))
        print(x_i/(1 + abs(y_i)))
        sigma = sigma + x_i/(1 + abs(y_i))
        x_i_1 = x_i
        y_i_1 = y_i
        counter = counter - 1
        k = k + 1

    return sigma


print(calculating(getting_number()))
