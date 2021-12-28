def count_let(string, letter):
    count = 0
    for i in string:
        if i == letter:
            count += 1
    return count
