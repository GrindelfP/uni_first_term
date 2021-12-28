# p(i)-предикат, какое-то условие, возвращает bool
def p(i):
    return i > 0


def sum_el(arr):
    sum_res = 0
    for i in arr:
        if p(i):
            sum_res += i
    return sum_res
