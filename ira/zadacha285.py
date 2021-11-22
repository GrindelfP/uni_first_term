# from random import uniform
# n = int(input())
# a = [uniform(-100, 100) for i in range(n)]
# print(a)
a = [2, 2, 1, 1, 1, 1, 1, 1, 1, 2]
n = 10

for i in range(0, n):
    if a[i] < 0:
        a[i] = a[i] ** 2
print(a)


def sequence():
    flag = False
    for j in range(0, n - 1):
        if a[j] <= a[j + 1]:
            flag = True
        else:
            flag = False
            break
    return flag


result = a[0]
for i in range(1, n):
    if sequence():
        result += a[i]
    else:
        result *= a[i]
print(result)
