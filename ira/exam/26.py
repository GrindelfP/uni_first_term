def is_prime(n):  # написал свою
    if n == 0 or n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    elif n > 4:
        for i in range(2, n//2):
            if n % i == 0:
                return False
    return True
