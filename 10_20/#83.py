from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Please enter a real number!")
    number = 0
    flag = True
    while flag:
        user_number = input("a = ")
        if know_type_of_input(user_number) is str:
            print("You must enter a real number!")
        else:
            number = make_number(user_number)
            flag = False

    return number


user_number = getting_number()
x_n = x_i = 0
while x_n < user_number:
    x_i = x_i + 1
    x_n = x_n + 1/x_i
    print(x_n, x_i)

