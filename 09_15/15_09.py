user_input_of_hours = int(input("Введите значение часов: "))
user_input_of_minutes = int(input("Введите значение минут: "))

user_change_of_minutes = int(input("Введите значение прибавляемых минут: "))

print("Вермя до: ", user_input_of_hours, ':', user_input_of_minutes)

if (user_change_of_minutes + user_input_of_minutes) >= 60:
    user_input_of_hours = user_input_of_hours + (user_change_of_minutes + user_input_of_minutes) // 60
    user_input_of_minutes = user_input_of_minutes + user_change_of_minutes - 60


print("Вермя после: ", user_input_of_hours, ':', user_input_of_minutes)
