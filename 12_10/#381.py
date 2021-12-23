import random


def create_matrix(n, m, min_num, max_num) -> list:
    return [[random.randint(min_num, max_num) for _ in range(n)] for _ in range(m)]


def print_matrix(matrix) -> None:
    for i in range(len(matrix)):
        print(*matrix[i], sep=" ")


def change_max_to_ten(matrix) -> list:
    changer = 10
    max_elem = matrix[0][0]
    for i in matrix:
        for j in i:
            if j > max_elem:
                max_elem = j
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == max_elem:
                matrix[i][j] = changer
    return matrix


n_val = int(input("Enter number of raws and columns -> "))
min_val = int(input("Enter minimum value of element -> "))
max_val = int(input("Enter maximum value of element -> "))

users_matrix = create_matrix(n_val, n_val, min_val, max_val)
print_matrix(users_matrix)
new_matrix = change_max_to_ten(users_matrix)
print("\n")
print_matrix(new_matrix)
