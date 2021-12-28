# Вообще все неправильно было. Вот два алгоритма для перевода из 10-чной в меньшую, например 3-ую, и второй - для
# перевода из не 10-чной в 10-ную.
def from_decimal(number, base):
    transferred = []
    while number:
        digit = number % base
        number //= base
        transferred.append(digit)
    result = ""
    for i in range(len(transferred) - 1, -1, -1):
        result += str(transferred[i])
    return result


def to_decimal(number_str, init_base):
    number = number_str
    power = 0
    number_decimal = 0
    while number:
        digit = number % 10 * init_base ** power
        number //= 10
        power += 1
        number_decimal += digit
    return str(number_decimal)
# TODO: for 16
