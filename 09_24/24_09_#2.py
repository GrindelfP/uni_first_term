from personal_library.number_operating import know_type_of_input, make_number


def communication() -> list:
    print("Please enter information about the triangle!")
    names = ["A = ", "B = ", "C = "]
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


def if_exists(side_a, side_b, side_c) -> bool:
    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        return True
    else:
        return False


points = communication()
if if_exists(points[0], points[1], points[2]):
    print("Yes, it exists!")
    points.sort()
    hypotenuse = points[2]
    leg_1 = points[1]
    leg_2 = points[0]
    if hypotenuse**2 == leg_1**2 + leg_2**2:
        print("Also this is an orthogonal triangle!")
else:
    print("No, it doesn't exist")

