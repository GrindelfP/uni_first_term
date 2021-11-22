from random import randint

mixed_list = []
for i in range(0, 100):
    mixed_list.append(randint(-100, 100))
    # # or if you want firstly-ordered list:
    # mixed_list += [i]
print(mixed_list)
for j in range(0, len(mixed_list)):
    mixing_index = randint(0, len(mixed_list) - 1)
    mixed_list[j], mixed_list[mixing_index] = mixed_list[mixing_index], mixed_list[j]
print(mixed_list)
