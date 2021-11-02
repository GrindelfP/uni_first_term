from random import sample

sequence = sample(range(101), 99)
max_ = 0
for element in sequence:
    if element > max_:
        max_ = element
counter = len(sequence)
index = -1
while counter > 0:
    index = index + 1
    if sequence[index] == max_:
        sequence.remove(sequence[index])
        index = index - 1
    counter = counter - 1

print(sequence)
