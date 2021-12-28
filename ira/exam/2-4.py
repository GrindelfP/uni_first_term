#ряды будут типа как мы в задачнике решали, вот например какой-то номер из него 101-110 что-то отттуда

eps = float(input("Epsilon = "))
a = float(input("a = "))
x = float(input("x = "))
y_0 = a
y_i_2 = y_0
y_i = 1 / 2 * (y_i_2 + (x / y_i_2))

while abs((y_i) ** 2 - (y_i_2) ** 2) < eps:
    y_i_2 = y_i
    y_i = 1 / 2 * (y_i_2 + (x / y_i_2))
print(y_i)


