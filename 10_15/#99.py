from personal_library.number_operating import make_number, my_factorial
from personal_library.objects import know_type_of_input


def getting_numbers() -> list:
    print("Введите 2 действительных числа!")
    names = ["u = ", "v = "]
    received_numbers = []
    for point in names:
        flag = True
        while flag:
            user_point = input(point)
            if know_type_of_input(user_point) is str:
                print("Вы должны ввести число!")
            else:
                received_numbers.append(make_number(user_point))
                flag = False

    print("Введите натуральное число больше 1!")
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float \
                or make_number(user_number) < 2:
            print("Вы должны ввести натуральное число, большее 1!")
        else:
            received_numbers.append(make_number(user_number))
            flag = False

    return received_numbers


def calculation(user_numbers):
    a_k_1 = user_numbers[0]
    b_k_1 = user_numbers[1]
    counter = user_numbers[2]
    k = 2
    sigma = (a_k_1*b_k_1)/(my_factorial(1 + 1))
    while counter > 1:
        a_k = 2*b_k_1+a_k_1
        b_k = 2*a_k_1**2 + b_k_1
        sigma = sigma + (a_k*b_k)/(my_factorial(k + 1))
        a_k_1 = a_k
        b_k_1 = b_k
        counter = counter - 1

    return sigma


user_input = getting_numbers()
print(calculation(user_input))
