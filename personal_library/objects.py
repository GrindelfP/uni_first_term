def know_type_of_input(user_input) -> type:
    # receives user's input and returns its type except boolean
    if user_input.count(',') == 1:
        user_input = user_input.replace(',', '.', 1)

    if user_input.isdigit():
        user_input = int(user_input)
    else:
        try:
            float(user_input)
            user_input = float(user_input)
            if int(user_input) == user_input:
                user_input = int(user_input)
        except ValueError:
            user_input = 'not a number'

    return type(user_input)
