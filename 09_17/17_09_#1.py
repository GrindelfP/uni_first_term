def print_line(number_of_mushrooms) -> None:
    if number_of_mushrooms == 0:
        print("Я не нашел грибов!")
    elif number_of_mushrooms == 1 or ((number_of_mushrooms % 10 == 1) and (number_of_mushrooms % 100 != 11)):
        print("Я нашел", number_of_mushrooms, "гриб!")
    elif 0 < (number_of_mushrooms % 10) < 5 and \
            not (10 < (number_of_mushrooms % 100) < 15):
        print("Я нашел", number_of_mushrooms, "гриба!")
    else:
        print("Я нашел", number_of_mushrooms, "грибов!")


mushrooms = int(input("Сколько я нашел грибов: "))
print_line(mushrooms)
