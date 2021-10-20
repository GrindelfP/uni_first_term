from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_numbers() -> list:
    print("Please enter two numbers!")
    numbers = []
    numbers_templates = ["a = ", "x = "]
    for template in numbers_templates:
        flag_1 = True
        while flag_1:
            user_number = input(template)
            if know_type_of_input(user_number) is str:
                print("You must enter a number!")
            else:
                numbers.append(make_number(user_number))
                flag_1 = False
    flag_2 = True
    while flag_2:
        user_number = input("Enter here a natural number -> ")
        if know_type_of_input(user_number) is str:
            print("You must enter a natural number!")
        else:
            numbers.append(make_number(user_number))
            flag_2 = False

    return numbers


def calculating(operated_numbers) -> int or float:
    a = operated_numbers[0]
    n = operated_numbers[2]
    result = operated_numbers[1] + a
    while n > 0:
        result = result**2 + a
        print(result)
        n = n - 1

    return result


user_numbers = getting_numbers()
print("Here is your result:", calculating(user_numbers))
