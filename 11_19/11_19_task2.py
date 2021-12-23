def alphabetic_order_english(line) -> str:
    line += " "
    alphabetic_order = [""] * 26
    ordered_line = ""
    word = ""
    for char in line:
        if char != " ":
            word += char
        else:
            if word != "":
                index = ord(word[0].upper()) - ord("A") + 1
                print(index)
                alphabetic_order.insert(index, word)
            word = ""
    print(alphabetic_order)
    for word in alphabetic_order:
        if word != "":
            ordered_line += word + " "
    return ordered_line


def alphabetic_order_russian():
    pass


user_line = input()
print(alphabetic_order_english(line=user_line))
