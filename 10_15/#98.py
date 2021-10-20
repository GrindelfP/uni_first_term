from personal_library.number_operating import make_number, my_factorial
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
    a_i_1 = b_i_1 = 1
    counter = users_number
    k = 2
    sigma = (2*k/((1 + a_i_1**2 + b_i_1**2)*my_factorial(1)))
    while counter > 1:
        a_i = 3*b_i_1+2*a_i_1
        b_i = 2*a_i_1 + b_i_1
        sigma = sigma + (2*k/((1 + a_i**2 + b_i**2)*my_factorial(k)))
        a_i_1 = a_i
        b_i_1 = b_i
        counter = counter - 1
        k = k + 1

    return sigma


print(calculating(getting_number()))
