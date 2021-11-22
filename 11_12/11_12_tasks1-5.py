# 1)
the_line = input("Введите вашу строку: ")
reversed_line = the_line
final_position = len(reversed_line) - 1
for index in range(0, len(reversed_line)):
    reversed_line = "".join((reversed_line, reversed_line[final_position - index]))
reversed_line = reversed_line[len(reversed_line) // 2:]
print("Развернутая строка:", reversed_line)

# 2)
the_letter = input("Введите искомую букву: ")
counter_2 = 0
for letter_2 in the_line:
    if letter_2.upper() == the_letter.upper():
        counter_2 += 1
print("Количество букв", the_letter, "-", counter_2)

# 3)
flag = False
number_of_words = 0
for i in range(0, len(the_line)):
    if not flag and the_line[i] != " ":
        number_of_words += 1
        flag = True
    elif the_line[i] == " ":
        flag = False
print("Количество слов в строке -", number_of_words)

# 4)
old_line = the_line
transformed_line = ""
for index in range(1, len(old_line)):
    if index != len(old_line) - 1:
        if old_line[index] == " " and old_line[index - 1] != " ":
            transformed_line += old_line[index]
        elif old_line[index] != " ":
            transformed_line += old_line[index]
    else:
        if old_line[index] != " ":
            transformed_line += old_line[index]
if transformed_line[len(transformed_line) - 1] == " ":
    transformed_line = transformed_line[: len(transformed_line) - 1]
print(transformed_line)

# 5)
line = the_line
hello_word = "привет"
indexes = []
counter = 0
for letter in line:
    if letter in hello_word:
        indexes.append(line.index(letter))
        counter += 1
        if counter == 5:
            break
line = line[:indexes[1]] + "о" + "к" + "a" + line[indexes[len(indexes) - 1] + 2:]
print(line)
