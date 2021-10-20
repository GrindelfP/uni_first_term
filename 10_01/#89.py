from personal_library.number_operating import make_number
from personal_library.objects import know_type_of_input


def getting_number() -> list:
    print("Please enter two natural numbers!")
    numbers_names = ["n = ", "m = "]
    numbers = []
    for name in numbers_names:
        flag = True
        while flag:
            user_number = input(name)
            if know_type_of_input(user_number) is str or know_type_of_input(user_number) is float:
                print("You must enter a natural number!")
            else:
                numbers.append(make_number(user_number))
                flag = False

    return numbers


def euclid_algorithm(n, m) -> int:
    if n != 0 and m != 0:
        while n != m:
            if n < m:
                n, m = m, n
            n = n - m
    else:
        if m == 0:
            return n
        else:
            return m

    return n


def find_least_common_multiple(greatest_common_divisor, n, m) -> int:
    return (abs(n * m))/(greatest_common_divisor)


user_numbers = getting_number()
greatest_common_divisor_of_numbers = euclid_algorithm(n=user_numbers[0],m=user_numbers[1])
least_common_multiple_of_numbers = find_least_common_multiple(greatest_common_divisor_of_numbers,
                                                              user_numbers[0],user_numbers[1])

print("The greatest common divider of", user_numbers[0], "and", user_numbers[1], "->",
      greatest_common_divisor_of_numbers)
print("The least common multiple of", user_numbers[0], "and", user_numbers[1], "->",
      least_common_multiple_of_numbers)
