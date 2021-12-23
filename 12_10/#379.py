import random


def create_matrix(n, m, min_num, max_num) -> list:
    return [[random.randint(min_num, max_num) for _ in range(n)] for _ in range(m)]


def print_matrix(matrix) -> None:
    for i in range(len(matrix)):
        print(*matrix[i], sep=" ")


def task_a(matrix) -> list:
    sums = []
    for i in matrix:
        current_sum = 0
        for j in i:
            current_sum += j
        sums.append(current_sum)
    return sums


def task_b(matrix) -> list:
    products = []
    for i in matrix:
        current_product = 1
        for j in i:
            current_product *= j
        products.append(current_product)
    return products


def task_c(matrix) -> list:
    minimal_elements = []
    for i in matrix:
        min_elem = i[0]
        for j in i:
            if j < min_elem:
                min_elem = j
        minimal_elements.append(min_elem)
    return minimal_elements


def task_d(matrix) -> list:
    average_elements = []
    for i in matrix:
        sum_of_raw = 0
        for j in i:
            sum_of_raw += j
        average_element = sum_of_raw/len(i)
        average_elements.append(average_element)
    return average_elements


def task_e(matrix) -> list:
    diminutions = []
    for i in matrix:
        min_elem = i[0]
        max_elem = 0
        for j in i:
            if j < min_elem:
                min_elem = j
            if j > max_elem:
                max_elem = j
        diminutions.append(max_elem - min_elem)
    return diminutions


n_val = int(input("Enter number of columns -> "))
m_val = int(input("Enter number of raws -> "))
min_val = int(input("Enter minimum value of element -> "))
max_val = int(input("Enter maximum value of element -> "))

users_matrix = create_matrix(n_val, m_val, min_val, max_val)
print("The MATRIX has you")
print_matrix(users_matrix)
print("Task \"a\" answer:", task_a(users_matrix))
print("Task \"b\" answer:", task_b(users_matrix))
print("Task \"c\" answer:", task_c(users_matrix))
print("Task \"d\" answer:", task_d(users_matrix))
print("Task \"e\" answer:", task_e(users_matrix))
