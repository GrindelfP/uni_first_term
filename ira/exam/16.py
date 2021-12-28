import random


def matrix_transpos(matrix):
    transp = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transp[j][i]=matrix[i][j]
    return transp


n = 15  # количество строк
m = 1  # количество столбцов
min_num = 1  # минимальное значение элемента
max_num = 7  # максимальное значение элемента
matr = [[random.randint(min_num, max_num) for _ in range(n)] for _ in range(m)]  # создание матрицы,
# можешь его выписать как отдельную функцию
for i in matr:
    print(*i)  # звездочка нужна чтобы он считал i одним целым и печатал строки матрицы в одну строчку

tr_matr = matrix_transpos(matr)
print("")  # просто разделитель
for i in tr_matr:
    print(*i)
