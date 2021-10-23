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
y_n_1 = 0
y_n = (y_n_1 + 1) / (y_n_1 + 2)
flag = True
while flag:
    y_n = (y_n_1 + 1) / (y_n_1 + 2)
    print(y_n)
    if (y_n - y_n_1) < epsilon:
        print("Результат:", y_n)
        flag = False
    y_n_1 = y_n
