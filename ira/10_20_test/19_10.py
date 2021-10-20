from random import randint

a = [randint(1, 100) for i in range(10)]
print(a)


def the_requirement(operated_number) -> bool:
    return operated_number < 50


def max_if(list_) -> int:
    max_ = 0
    for element in list_:
        if element > max_ and the_requirement(element):
            max_ = element

    return max_


lesser = a[0]
lesser_2 = a[1]
number = 0
number_2 = 1
if lesser > lesser_2:
    lesser, lesser_2 = lesser_2, lesser
    number, number_2 = number_2, number

for i in range(2, len(a)):
    if a[i] < lesser:
        lesser_2 = lesser
        number_2 = number
        lesser = a[i]
        number = i

    if lesser_2 > a[i] > lesser:
        lesser_2 = a[i]
        number_2 = i

print(lesser, number)
print(lesser_2, number_2)
print(max_if(a))
