# a)
consequent_a = 1
coefficient_a = -1
sigma_a = 0
while consequent_a < 10001:
    coefficient_a = -coefficient_a
    current_element = coefficient_a * 1 / consequent_a
    consequent_a = consequent_a + 1
    sigma_a = sigma_a + current_element

print("Результат а:", sigma_a)


# b)
consequent_b = 1
sigma_b_1 = 0
sigma_b_2 = 0
while consequent_b < 10001:
    if consequent_b % 2 != 0:
        current_element = 1 / consequent_b
        consequent_b = consequent_b + 1
        sigma_b_1 = sigma_b_1 + current_element
    else:
        current_element = 1 / consequent_b
        consequent_b = consequent_b + 1
        sigma_b_2 = sigma_b_2 + current_element
print(sigma_b_1)
print(sigma_b_2)
print("Результат б:", sigma_b_1 + sigma_b_2)


# c)
consequent_c = 10000
coefficient_c = 1
sigma_c = 0
while consequent_c > 0:
    coefficient_c = -coefficient_c
    current_element = coefficient_c * 1 / consequent_c
    consequent_c = consequent_c - 1
    sigma_c = sigma_c + current_element

print("Результат в:", sigma_c)


# d)
consequent_d = 10000
sigma_d_1 = 0
sigma_d_2 = 0
while consequent_d > 0:
    if consequent_d % 2 != 0:
        current_element = 1 / consequent_d
        consequent_d = consequent_d - 1
        sigma_d_1 = sigma_d_1 + current_element
    else:
        current_element = 1 / consequent_d
        consequent_d = consequent_d - 1
        sigma_d_2 = sigma_d_2 + current_element
print("Результат г:", sigma_d_1 - sigma_d_2)
