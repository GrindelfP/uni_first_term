from personal_library.number_operating import know_type_of_input, make_number

flag = True
while flag:
    user_input_of_hours = input("Введите значение часов: ")
    user_input_of_minutes = input("Введите значение минут: ")
    if know_type_of_input(user_input_of_hours) is int and know_type_of_input(user_input_of_minutes) is int:
        if (0 < make_number(user_input_of_hours) <= 24) and (0 < make_number(user_input_of_minutes) <= 60):
            hours = make_number(user_input_of_hours)
            minutes = make_number(user_input_of_minutes)
            flag = False
    else:
        print("Извинте, такого времени не бывает! Попробуйте ещё раз!")


user_change_of_minutes = int(input("Введите значение прибавляемых минут: "))

print("Вермя до: ", hours, ':', minutes)

if (user_change_of_minutes + minutes) >= 60:
    user_input_of_hours = hours + (user_change_of_minutes + minutes) // 60
    user_input_of_minutes = hours + user_change_of_minutes - 60


print("Вермя после: ", hours, ':', minutes)
