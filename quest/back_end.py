def check_choice(type_, choice_) -> bool:
    if type_ == "day":
        if choice_.upper() == "А" or choice_.upper() == "Б" or choice_.upper() == "В" or choice_.upper() == "Г":
            return True
        else:
            return False
    elif type_ == "evening":
        if choice_.upper() == "А" or choice_.upper() == "Б" or choice_.upper() == "В":
            return True
        else:
            return False
    else:
        return False



def change_the_stats_lections(the_choice, food, tiredness, points_to_autopass, knowledge) -> list:
    if the_choice == "А":
        food = food - 60
        if food <= 0:
            food = 0
        tiredness = tiredness + 40
        if tiredness >= 100:
            tiredness = 100
        points_to_autopass = points_to_autopass + 10
        if points_to_autopass >= 100:
            points_to_autopass = 100
        knowledge = knowledge + 10
    elif the_choice == "Б":
        food = food - 30
        if food <= 0:
            food = 0
        tiredness = tiredness + 25
        if tiredness >= 100:
            tiredness = 100
        points_to_autopass = points_to_autopass + 5
        if points_to_autopass >= 100:
            points_to_autopass = 100
        knowledge = knowledge + 5
    elif the_choice == "В":
        food = food - 10
        if food <= 0:
            food = 0
        tiredness = tiredness + 15
        if tiredness >= 100:
            tiredness = 100
    else:
        points_to_autopass = points_to_autopass - 30
        if points_to_autopass <= 0:
            points_to_autopass = 0

    return [food, tiredness, points_to_autopass, knowledge]


def change_the_stats_evening(the_choice, food, tiredness, points_to_autopass, knowledge) -> list:
    if the_choice == "А":
        food = food + 30
        if food >= 100:
            food = 100
        tiredness = tiredness + 25
        if tiredness >= 100:
            tiredness = 100
        knowledge = knowledge + 5
    elif the_choice == "Б":
        food = food + 60
        if food >= 100:
            food = 100
        tiredness = tiredness - 30
        if tiredness <= 0:
            tiredness = 0
        knowledge = knowledge - 3
    else:
        food = food - 20
        if food <= 0:
            food = 0
        tiredness = tiredness - 30
        if tiredness <= 0:
            tiredness = 0
        knowledge = knowledge - 3

    return [food, tiredness, points_to_autopass, knowledge]

