n = int(input())


def r(x):
    z = 0
    c = x
    while x != 0:
        z += x % 10
        x = x // 10
    if c ** 2 == z ** 3:
        print('верно')
    else:
        print('неверно')


r(n)
