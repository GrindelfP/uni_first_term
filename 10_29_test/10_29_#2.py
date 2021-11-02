def to_number(user_input) -> int or float:
    if user_input.isdigit():
        return int(user_input)
    else:
        return float(user_input)


epsilon = to_number(input("Введите действительное положительное число (уровень точности): е = "))
y_i_1 = to_number(input("Введите действительное положительное число (начальный элемент ряда): a = "))
y_i = y_i_1 + 1/y_i_1
while abs(y_i - y_i_1) >= epsilon:
    y_i_1 = y_i
    y_i = y_i_1 + 1/y_i_1

print("Результат:", y_i)
