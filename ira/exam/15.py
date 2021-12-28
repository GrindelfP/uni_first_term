import random


def mix_arr(arr):
    for i in range(len(arr)):
        i_one = random.randint(0, len(arr) - 1)
        i_two = random.randint(0, len(arr) - 1)
        arr[i_one], arr[i_two] = arr[i_two], arr[i_one]
    return arr
