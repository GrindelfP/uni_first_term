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
    a_k_1 = b_k_1 = 1
    counter = users_number
    k = 2
    sigma = a_k_1*b_k_1
    while counter > 1:
        a_k = 0.5*(b_k_1**0.5 + 0.5*a_k_1**2)
        b_k = 2 * a_k_1**2 + b_k_1
        sigma = sigma + a_k*b_k
        a_k_1 = a_k
        b_k_1 = b_k
        counter = counter - 1
        k = k + 1

    return sigma


print(calculating(getting_number()))
