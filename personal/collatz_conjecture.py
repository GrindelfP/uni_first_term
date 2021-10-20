from personal_library.number_operating import know_type_of_input, make_number


def communication() -> int:
    print("Please enter a natural number different from 0!")
    number = 0
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float or int(user_number) == 0:
            print("You must enter a natural number different from 0!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def collatz(operated) -> int:
    counter = 0
    print("\nSteps:")
    while operated > 1:
        if operated % 2 == 0:
            operated = operated / 2
            counter = counter + 1
            print(operated)
        else:
            operated = 3 * operated + 1
            counter = counter + 1
            print(operated)

    return counter


operated_number = communication()
print("\nIt took", collatz(operated_number), "steps to reach 1.")
