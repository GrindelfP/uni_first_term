from math import sqrt


def point_checking(side) -> int or float:
    if side.count('.') > 0:
        side = float(side)
    else:
        side = int(side)

    return side


def if_exists(side_a, side_b, side_c) -> bool:
    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        return True
    else:
        return False


def count_area(side_a, side_b, side_c) -> float or int:
    semi_perimeter = (side_a + side_b + side_c) * 0.5
    area = sqrt(semi_perimeter*(semi_perimeter - side_a)*(semi_perimeter - side_b)*(semi_perimeter - side_c))

    return area


flag = True
while flag:
    a = point_checking(input('Hello! Enter your 1st side of a triangle:'))
    b = point_checking(input('Enter your 2st side of a triangle:'))
    c = point_checking(input('Enter your 3st side of a triangle:'))
    if if_exists(a, b, c):
        flag = False
    else:
        print('Your triangle does not exist! Try again!')

print('Your result is:', count_area(a, b, c))
