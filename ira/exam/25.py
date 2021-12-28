# p(i)-предикат, какое-то условие, возвращает bool
def p(i):
    return i > 0


def sum_el(arr):
    count = 0
    for i in arr:
        if p(i):  # если выполняется условие p(i), элемент массива нам подходит
            count += 1
    return count
