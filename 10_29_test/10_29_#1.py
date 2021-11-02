n = int(input("Введите натуральное число: n = "))
a_i_1 = 2
b_i_1 = 1
a_answer = [a_i_1]
b_answer = [b_i_1]
i = 1
factorial = 1
sigma = factorial/(a_i_1**2 - b_i_1**2)
while n > 1:
    i = i + 1
    factorial = factorial * i
    a_i = 5 * b_i_1 + a_i_1
    b_i = 2 * a_i_1 + b_i_1
    sigma = sigma + factorial/(a_i**2 - b_i**2)
    a_answer.append(a_i)
    b_answer.append(b_i)
    a_i_1 = a_i
    b_i_1 = b_i
    n = n - 1

print("Последовательность A элементов:", a_answer)
print("Последовательность B элементов:", b_answer)
print("Сумма рядов:", sigma)
