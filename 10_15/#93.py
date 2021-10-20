from personal_library.number_operating import know_type_of_input, make_number


def getting_numbers() -> list:
    print("Введите 5 действительных чисел!")
    names = ["q = ", "r = ", "b = ", "c = ", "d = "]
    received_points = []
    for point in names:
        flag = True
        while flag:
            user_point = input(point)
            if know_type_of_input(user_point) is str:
                print("Вы должны ввести число!")
            else:
                received_points.append(make_number(user_point))
                flag = False

    print("Введите натуральное число больше 1!")
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float \
                or make_number(user_number) < 2:
            print("Вы должны ввести натуральное число, большее 1!")
        else:
            received_points.append(make_number(user_number))
            flag = False

    return received_points


def calculation(user_points):
    x_k_2 = user_points[3]
    x_k_1 = user_points[4]
    b = user_points[2]
    q = user_points[0]
    r = user_points[1]
    counter = user_points[5]
    k = 2
    x_k = 0
    while counter > 1:
        x_k = q*x_k_1 + r*x_k_2 + b
        x_k_2 = x_k_1
        x_k_1 = x_k
        k = k + 1
        counter = counter - 1

    return x_k


print(calculation(getting_numbers()))
