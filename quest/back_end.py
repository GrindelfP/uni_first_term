def check_choice(type_, choice_) -> bool:
    if type_ == "day":
        if choice_ == "1" or choice_ == "2" or choice_ == "3" or choice_ == "4":
            return True
        else:
            return False
    elif type_ == "evening":
        if choice_ == "1" or choice_ == "2" or choice_ == "3":
            return True
        else:
            return False
    else:
        return False


def death_check(food, tiredness) -> str:
    if food <= 0:
        return "starved"
    if tiredness >= 100:
        return "tired"
    else:
        return "alive"


def change_the_stats_lections(the_choice, food, tiredness, points_to_autopass, knowledge) -> list:
    if the_choice == "1":
        food = food - 30
        if food <= 0:
            food = 0
        tiredness = tiredness + 20
        if tiredness >= 100:
            tiredness = 100
        points_to_autopass = points_to_autopass + 20
        if points_to_autopass >= 100:
            points_to_autopass = 100
        knowledge = knowledge + 15
    elif the_choice == "2":
        food = food - 15
        if food <= 0:
            food = 0
        tiredness = tiredness + 20
        if tiredness >= 100:
            tiredness = 100
        points_to_autopass = points_to_autopass + 10
        if points_to_autopass >= 100:
            points_to_autopass = 100
        knowledge = knowledge + 7
    elif the_choice == "3":
        food = food - 10
        if food <= 0:
            food = 0
        tiredness = tiredness + 10
        if tiredness >= 100:
            tiredness = 100
    else:
        points_to_autopass = points_to_autopass - 30
        if points_to_autopass <= 0:
            points_to_autopass = 0
        tiredness = tiredness - 70
        if tiredness <= 0:
            tiredness = 0

    return [food, tiredness, points_to_autopass, knowledge]


def change_the_stats_evening(the_choice, food, tiredness, points_to_autopass, knowledge) -> list:
    if the_choice == "1":
        food = food + 30
        if food >= 100:
            food = 100
        tiredness = tiredness + 20
        if tiredness >= 100:
            tiredness = 100
        knowledge = knowledge + 5
    elif the_choice == "2":
        food = food + 70
        if food >= 100:
            food = 100
        tiredness = tiredness - 40
        if tiredness <= 0:
            tiredness = 0
        knowledge = knowledge - 4
    else:
        food = food - 20
        if food <= 0:
            food = 0
        tiredness = tiredness - 50
        if tiredness <= 0:
            tiredness = 0
        knowledge = knowledge - 5

    return [food, tiredness, points_to_autopass, knowledge]

