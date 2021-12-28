# p(i)-предикат, какое-то условие, возвращает bool
def p(i):
    return i > 0


def sun_el(arr):
    sum_res = 0
    count = 0
    for i in arr:
        if p(i):
            sum_res += i
            count += 1
    return sum_res / count
