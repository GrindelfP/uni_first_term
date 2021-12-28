def sign(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    return -1


def F(x):
    return 2*x-4


def Solution(x_n, x_k, eps):
    y1 = F(x_n)
    y2 = F(x_k)
    if y1 * y2 >= 0:
        return "Корней нет"
    else:
        x = (x_n + x_k) / 2
        y3 = F(x)
        while abs(y3) > eps:
            x = (x_n + x_k) / 2
            y3 = F(x)
            if sign(y1) != sign(y3):
                x_k = x
            else:
                x_n = x
        return x


print(Solution(-10000, 10000, 0.0000005))
