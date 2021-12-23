import random


def create_matrix(n, m, min_num, max_num) -> list:
    return [[random.randint(min_num, max_num) for _ in range(n)] for _ in range(m)]


def print_matrix(matrix) -> None:
    for i in range(len(matrix)):
        print(*matrix[i], sep=" ")


def print_main_diagonal(matrix) -> None:
    diagonal_sequence = []
    bottom_edge = 0
    for i in matrix:
        for j in range(bottom_edge, len(i)):
            diagonal_sequence.append(i[j])
            bottom_edge += 1
            break
    print(diagonal_sequence)


n_val = int(input("Enter number of raws and columns, and also the maximum value of elements -> "))
min_val = 1

users_matrix = create_matrix(n_val, n_val, min_val, n_val)
print_matrix(users_matrix)
print_main_diagonal(users_matrix)
