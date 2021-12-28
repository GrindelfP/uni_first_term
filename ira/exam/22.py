def count_words(temp, word_low):
    string = ""
    word = ""
    for i in temp:
        string += i.upper()
    for i in word_low:
        word += i.upper()
    counttt = 0
    for i in range(0, len(string)):
        temp_word = ""
        while string[i].isalpha() and i != len(string) - 1:
            temp_word += string[i]
            i += 1
        if temp_word == word:
            counttt += 1
    return counttt


# Какой-то сложный код. Предлагаю алгоритм подсчета количества слов Бьёрна Страуструпа
def number_of_words(line):
    flag = False
    num_of_words = 0
    for i in range(len(line)):
        if not flag and line[i] != " ":
            num_of_words += 1
            flag = True
        elif line[i] == " ":
            flag = False
    return num_of_words
