# две функции, два способа, можно любым хз
def just_word_find(string, word):
    for i in range(len(string)):
        if string[i:i + len(word)] == word:
            return i  # походу тоже возвращает индекс первой буквы искомого слова
    return "Not found"


def search(string, word):
    M = len(word)
    N = len(string)

    for i in range(N - M + 1):
        status = 1
        for j in range(M):
            if string[i + j] != word[j]:
                status = 0
                break
        if status != 0:
            return str(i)
