from personal_library.number_operating import know_type_of_input, make_number


def getting_numbers() -> list:
    print("Введите 3 действительных положительных числа!")
    names = ["a = ", "x = ", "epsilon = "]
    received_points = []
    for point in names:
        flag_ = True
        while flag_:
            user_point = input(point)
            if know_type_of_input(user_point) is str or make_number(user_point) <= 0:
                print("Вы должны ввести действительное положительное число!")
            else:
                received_points.append(make_number(user_point))
                flag_ = False

    return received_points


user_numbers = getting_numbers()
x = user_numbers[1]
epsilon = user_numbers[2]
y_n_1 = user_numbers[0]
y_n = 0.5*(y_n_1 + x/y_n_1)
flag = True
while flag:
    y_n = 0.5*(y_n_1 + x/y_n_1)
    print(y_n)
    if abs(y_n**2 - y_n_1**2) < epsilon:
        print("Результат:", y_n)
        flag = False
    y_n_1 = y_n

