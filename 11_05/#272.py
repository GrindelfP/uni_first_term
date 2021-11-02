from random import sample

the_list = sample(range(101), 50)  # gives a list of random integers of length 50
sum_of_elements = 0
for element in the_list:
    sum_of_elements = sum_of_elements + element
average_value = sum_of_elements / 50  # gives average value of the list
print("Среднее значение:", average_value)
for element_ in the_list:
    print("Разница по сравнению со средним значением:", abs(element_ - average_value))  # prints deference between
    # current and average value
