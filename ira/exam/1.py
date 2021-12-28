def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


# вариант только для целых чисел:
def swap2(a, b):
    c = a + b
    a = c - a
    b = c - b
    return a, b


# классика Python:
def swap_classic(a, b):
    a, b = b, a
    return a, b
