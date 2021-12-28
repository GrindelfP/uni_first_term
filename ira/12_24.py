import random


def from_decimal(number, base):
    transferred = []
    while number:
        digit = number % base
        number //= base
        transferred.append(digit)
    result = ""
    for i in range(len(transferred) - 1, -1, -1):
        result += str(transferred[i])
    return int(result)


def to_decimal(number, init_base):
    power = 0
    number_decimal = 0
    while number:
        digit = number % 10 * init_base ** power
        number //= 10
        power += 1
        number_decimal += digit
    return number_decimal


# caesar
def caesar(repl, line):  # repl - length of shift, line - initial text
    new_line = ""
    for char in line:
        if repl + ord(char) > ord("z"):
            repl_loc = repl + ord(char) - ord("z")
            new_line += chr(ord("`") + repl_loc)
        else:
            new_line += chr(ord(char) + repl)
    return new_line


def create_matrix(n, m, min_num, max_num) -> list:
    return [[random.randint(min_num, max_num) for _ in range(n)] for _ in range(m)]


def print_matrix(matrix) -> None:
    for i in range(len(matrix)):
        print(*matrix[i], sep=" ")

# # trans
# matrix = create_matrix(4, 3, 1, 5)
# print_matrix(matrix)
# transp = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transp[j][i]=matrix[i][j]
# print_matrix(transp)


# multiply
def multipl_matr(A, B):
    if len(A[0]) != len(B):
        return "undefined"

    C = [[]]
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            C[i].append(0)

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C


am = [
    [5, 4],
    [2, 7]
]


bm = [
    [2, 2],
    [4, 3]
]


print_matrix(multipl_matr(am, bm))
print((len(multipl_matr(am, bm)[0])))