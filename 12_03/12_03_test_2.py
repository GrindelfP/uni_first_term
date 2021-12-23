import random


def find_max_element_raw(matrix) -> int:
    max_element = 0
    max_raw_index = None
    for raw in matrix:
        for element in raw:
            if element > max_element:
                max_element = element
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == max_element:
                max_raw_index = i
                break
    return max_raw_index


def find_min_element_raw(matrix) -> int:
    min_element = 99
    min_raw_index = None
    for raw in matrix:
        for element in raw:
            if element < min_element:
                min_element = element
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == min_element:
                min_raw_index = i
                break
    return min_raw_index


matrix_a = [[random.randint(0, 99) for _ in range(10)] for _ in range(10)]
for i in range(len(matrix_a)):
    print(*matrix_a[i], " ")
print("\n")

max_raw = find_max_element_raw(matrix_a)
min_raw = find_min_element_raw(matrix_a)
print(min_raw, max_raw)
print("\n")

matrix_a[max_raw], matrix_a[min_raw] = matrix_a[min_raw], matrix_a[max_raw]
for i in range(len(matrix_a)):
    print(*matrix_a[i], " ")
