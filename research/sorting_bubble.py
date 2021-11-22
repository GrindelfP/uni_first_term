from random import sample
from time import time


def bubble_sort(input_list) -> list:
    for first in range(len(input_list)):
        for index in range(0, len(input_list) - 1):
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]

    return input_list


def bubble_sort_2(input_list) -> list:
    for first in range(len(input_list)):
        for index in range(0, len(input_list) - first - 1):
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]

    return input_list


def bubble_sort_3(input_list) -> list:
    flag = 1
    while flag > 0:
        flag = 0
        for index in range(0, len(input_list) - 1):
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
                flag = 1

    return input_list


def bubble_sort_4(input_list) -> list:
    start_index = 0
    for first in range(len(input_list)):
        for index in range(start_index, len(input_list) - first - 1):
            start_index = -1
            if input_list[index] > input_list[index + 1]:
                start_index = 0
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
            else:
                start_index = start_index + 1
    return input_list


archtime = time()
times = 1000000
time_0_l = []
time_1_l = []
time_2_l = []
time_3_l = []
while times > 0:
    the_list = sample(range(1001), 10)
    time_0 = time()
    bubble_sort(the_list)
    time_0_l.append((time() - time_0) * 10000)
    time_1 = time()
    bubble_sort_2(the_list)
    time_1_l.append((time() - time_1) * 10000)
    time_2 = time()
    bubble_sort_3(the_list)
    time_2_l.append((time() - time_2) * 10000)
    time_3 = time()
    bubble_sort_4(the_list)
    time_3_l.append((time() - time_3) * 10000)

    times = times - 1

print(sum(time_0_l)/len(time_0_l))
print(sum(time_1_l)/len(time_1_l))
print(sum(time_2_l)/len(time_2_l))
print(sum(time_3_l)/len(time_3_l))
print(time() - archtime)
