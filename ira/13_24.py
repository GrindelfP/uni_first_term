# caesar
def caesar(repl, line): # repl - length of shift, line - initial text
    new_line = ""
    for char in line:
        if repl + ord(char) > ord("z"):
            repl_loc = repl + ord(char) - ord("z")
            new_line += chr(ord("`") + repl_loc)
        else:
            new_line += chr(ord(char) + repl)
    return new_line
