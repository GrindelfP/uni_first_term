from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Please enter a natural number!")
    number = 0
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float or int(user_number) == 0:
            print("You must enter a natural number!")
        else:
            number = make_number(user_number)
            flag = False

    return number


def calculating(users_number):
    counter = users_number
    a_0 = 1
    a_1 = 0
    k = 1
    while counter > 0:
        a_1 = k * a_0 + (1/k)
        a_0 = a_1
        k = k + 1
        counter = counter - 1

    return a_1


result = calculating(getting_number())
print(result, type(result))
