from personal_library.number_operating import know_type_of_input, make_number


def getting_number() -> int:
    print("Введите уровень точности - действительное положительное число!!")
    number = 0
    flag_ = True
    while flag_:
        user_number = input("epsilon = ")
        if know_type_of_input(user_number) is str or make_number(user_number) <= 0:
            print("Это должно быть действительное положительное число!")
        else:
            number = make_number(user_number)
            flag_ = False

    return number


epsilon = getting_number()
x_n_1 = 1
x_n = (2 - x_n_1**3)/5
flag = True
while flag:
    x_n = (2 - x_n_1**3)/5
    print(x_n)
    if abs(x_n - x_n_1) < epsilon:
        print("Результат:", x_n)
        flag = False
    x_n_1 = x_n

