from random import sample
from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> int:
    print("Введите натуральное число!")
    number = 0
    flag = True
    while flag:
        user_number = input("n = ")
        if know_type_of_input(user_number) is str or make_number(user_number) < 0:
            print("Вы должны ввести натуральное число!")
        else:
            number = make_number(user_number)
            flag = False

    return number


users_number = getting_number()
the_list = sample(range(101), users_number * 2)

# a
print("\nЗадание [а]\n")
for index_a in range(0, users_number):
    print("Элемент", index_a + 1, "=", the_list[index_a])
    print("Элемент", index_a + users_number + 1, "=", the_list[index_a + users_number])

# b
print("\n\nЗадание [б]\n")
for index_b in range(0, users_number):
    print("Элемент", index_b + 1, "=", the_list[index_b])
    print("Элемент", users_number * 2 - index_b, "=", the_list[users_number * 2 - index_b - 1])

# c
print("\n\nЗадание [в]\n")
for index_c in range(0, users_number):
    print("Сумма", index_c + 1, "=", the_list[index_c] + the_list[users_number * 2 - index_c - 1])

