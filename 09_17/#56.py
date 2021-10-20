def communication() -> list:
    print("Please enter some information! \nLet's start with the brick:")
    a_side = int(input("Side A: "))
    b_side = int(input("Side B: "))
    c_side = int(input("Side C: "))
    print("Now for the hole: ")
    x_side = int(input("Side X: "))
    y_side = int(input("Side Y: "))

    return [a_side, b_side, c_side, x_side, y_side]


def check_entrance_ability(side_one, side_two, hole_side_one, hole_side_two) -> bool:
    if (side_one <= hole_side_one and side_two <= hole_side_two) or (
            side_two <= hole_side_one and side_one <= hole_side_two):
        return True
    else:
        return False


sides = communication()

if check_entrance_ability(side_one=sides[0], side_two=sides[1], hole_side_one=sides[3], hole_side_two=sides[4]) or (
        check_entrance_ability(side_one=sides[1], side_two=sides[2], hole_side_one=sides[3], hole_side_two=sides[4])) or (
        check_entrance_ability(side_one=sides[1], side_two=sides[2], hole_side_one=sides[3], hole_side_two=sides[4])):
    print("Congrats! It does fit!")
else:
    print("No! I don't think so...")
