from personal_library.number_operating import know_type_of_input, make_number


def getting_number() -> int:
    print("Введите уровень точности - действительное положительное число!!")
    number = 0
    flag_ = True
    while flag_:
        user_number = input("epsilon = ")
        if know_type_of_input(user_number) is str or make_number(user_number) <= 0:
            print("Это должно быть действительное положительное число!")
        else:
            number = make_number(user_number)
            flag_ = False

    return number


epsilon = getting_number()

i = 1
sigma = 0
element = 1
while abs(element) >= epsilon:
    element = 1/(i*(i+1))
    i = i + 1
    sigma = sigma + element

print(sigma)
