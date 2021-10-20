from personal_library.number_operating import know_type_of_input, make_number
from math import sin, pi

type_of_the_task = input("Введите букву задания (а, б, в, г): ")
flag_letter = True
acceptable_letters = ["а", "б", "в", "г"]
while flag_letter:
    if type_of_the_task not in acceptable_letters:
        type_of_the_task = input("Вы ввели несуществующее задание! Попробуйте снова: ")
    else:
        flag_letter = False


number_a = input("Введите число а: ")
flag_number = True
while flag_number:
    if know_type_of_input(number_a) is str:
        number_a = input("Вы ввели не число! Введите заново число а: ")
    else:
        number_a = make_number(number_a)
        flag_number = False


def function(a):
    if type_of_the_task == "а":
        if -2 <= a <= 2:
            return a ** 2
        else:
            return 4
    elif type_of_the_task == "b":
        if a <= 2:
            return a**2 + 4*a + 5
        else:
            if (a**2 + 4*a + 5) != 0:
                return 1/(a**2 + 4*a + 5)
            else:
                return "Ваше выражение нерешаемо!"

    elif type_of_the_task == "в":
        if a <= 0:
            return 0
        elif 0 <= a <= 1:
            return a
        else:
            return a ** 4

    elif type_of_the_task == "г":
        if a <= 0:
            return 0
        elif 0 <= a <= 1:
            return a ** 2 - a
        else:
            return a ** 2 - sin(pi)*(a**2)


print(function(number_a))
