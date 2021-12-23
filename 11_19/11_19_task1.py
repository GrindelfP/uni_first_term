def find_biggest_word(line) -> str:
    # returns the biggest word of given line
    word = ""
    biggest_word = ""
    line += " "
    for char in line:
        if char != " ":
            word += char
        else:
            if len(word) > len(biggest_word):
                biggest_word = word
            word = ""

    return biggest_word


users_line = input()
print(find_biggest_word(line=users_line))
