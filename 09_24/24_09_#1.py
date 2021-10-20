from personal_library.number_operating import make_number, know_type_of_input

triangle_1 = [0, 0, -1, 1, -1.5, 0]
triangle_2 = [-1.5, 0, -2, -1, 1, 0]
z = 0


def communication() -> list:
    print("Please enter information about inspected point!")
    names = ["x = ", "y = "]
    received_points = []
    for point in names:
        flag = True
        while flag:
            user_point = input(point)
            if know_type_of_input(user_point) is str:
                print("You must enter a number!")
            else:
                received_points.append(make_number(user_point))
                flag = False

    return received_points


def include_checking(x_1, y_1, x_2, y_2, x_3, y_3, x_user, y_user) -> bool:
    area_1 = 0.5 * (abs(((x_2 - x_1) * (y_user - y_1)) - ((x_user - x_1) * (y_2 - y_1))))
    area_2 = 0.5 * (abs(((x_3 - x_2) * (y_user - y_2)) - ((x_user - x_2) * (y_3 - y_2))))
    area_3 = 0.5 * (abs(((x_1 - x_3) * (y_user - y_3)) - ((x_user - x_3) * (y_1 - y_3))))
    area_triangle = 0.5 * (abs(((x_2 - x_1) * (y_3 - y_1)) - ((x_3 - x_1) * (y_2 - y_1))))

    if (area_1 + area_3 + area_2) == area_triangle:
        return True
    else:
        return False


x_and_y = communication()

if include_checking(triangle_1[0], triangle_1[1], triangle_1[2], triangle_1[3], triangle_1[4], triangle_1[5],
                    x_and_y[0], x_and_y[1]) or \
        include_checking(triangle_2[0], triangle_2[1], triangle_2[2], triangle_2[3], triangle_2[4], triangle_2[5],
                         x_and_y[0], x_and_y[1]):
    z = x_and_y[0]
    print("It fits in!", z)
else:
    print("It doesn't fit in!", z)
