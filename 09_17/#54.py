from personal_library.number_operating import know_type_of_input, make_number


# def triangle_check(list_of_points) -> bool:
#     point_1 = [list_of_points[0], list_of_points[1]]
#     point_2 = [list_of_points[2], list_of_points[3]]
#     point_3 = [list_of_points[4], list_of_points[5]]
#     if ((point_1[0] + point_1[1]) != (point_2[0] + point_2[1])) and ((point_1[0] + point_1[1]) != (point_3[0] + point_3[1])) and ((point_2[0] + point_2[1]) != (point_3[0] + point_3[1])):
#         if (point_1[0] != point_2[0]) or (point_1[0] != point_3[0]) and (point_1[1] != point_2[1]) or (point_1[1] != point_3[1]):
#             return True
#     else:
#         return False


def communication() -> list:
    print("Please enter information about the triangle!")
    requested_points = ["x1 = ", "y1 = ", "x2 = ", "y2 = ", "x3 = ", "y3 = "]
    received_points = []
    for point in requested_points:
        flag = True
        while flag:
            user_point = input(point)
            if know_type_of_input(user_point) is str:
                print("You must enter a number!")
            else:
                received_points.append(make_number(user_point))
                flag = False

    return received_points


def include_checking(x_1, y_1, x_2, y_2, x_3, y_3) -> bool:
    area_1 = 0.5 * (abs(((x_2 - x_1) * (0 - y_1)) - ((0 - x_1) * (y_2 - y_1))))
    area_2 = 0.5 * (abs(((x_3 - x_2) * (0 - y_2)) - ((0 - x_2) * (y_3 - y_2))))
    area_3 = 0.5 * (abs(((x_1 - x_3) * (0 - y_3)) - ((0 - x_3) * (y_1 - y_3))))
    area_triangle = 0.5 * (abs(((x_2 - x_1) * (y_3 - y_1)) - ((x_3 - x_1) * (y_2 - y_1))))

    if (area_1 + area_3 + area_2) == area_triangle:
        return True
    else:
        return False


points = communication()
print(points)

if include_checking(points[0], points[1], points[2], points[3], points[4], points[5]):
    print("Yes!")
else:
    print("No!")

