import random


def make_matrix(n, m) -> list:
    matrix = [[random.randint(1, n) for _ in range(0, n)] for _ in range(0, m)]
    return matrix


def print_matrix(matrix, m) -> None:
    for i in range(m):
        print(*matrix[i], " ")


def sum_of_raw(raw_index, matrix) -> int:
    sigma = 0
    for element in matrix[raw_index]:
        sigma += element
    return sigma


def product_of_raw(raw_index, matrix) -> int:
    product = 1
    for element in matrix[raw_index]:
        product *= element
    return product


def find_sum_of_triangle(matrix) -> int:
    sigma = 0
    start_index = 0
    for i in range(0, len(matrix)):
        for j in range(start_index, len(matrix[i])):
            sigma += matrix[i][j]
        start_index += 1
    return sigma


n_num = int(input("n = "))
m_num = int(input("m = "))
the_matrix = make_matrix(n_num, m_num)
print_matrix(the_matrix, m_num)
# print(sum_of_raw(n_num - 1, the_matrix))
# print(product_of_raw(n_num - 1, the_matrix))
print(find_sum_of_triangle(the_matrix))
