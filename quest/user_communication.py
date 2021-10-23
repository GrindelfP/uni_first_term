from quest.back_end import change_the_stats_lections, change_the_stats_evening, death_check
from quest.comunication_back_end import giving_rules, intro, end_of_intro, get_choice
from quest.utility import day_game_test, stats_keeping, evening_game_test, endgame_text, death_text


def greetings() -> None:
    intro()
    giving_rules()
    end_of_intro()


def processing_game():
    counter = 10
    stats = stats_keeping()
    death = "no"
    while counter > 0:
        # day
        if death_check(stats[0], stats[1]) != "alive":
            death_text(death_check(stats[0], stats[1]))
            death = "yes"
            break
        day_game_test(counter, stats)
        choice_1 = get_choice("day")
        stats = change_the_stats_lections(choice_1, stats[0], stats[1], stats[2], stats[3])

        # evening
        if death_check(stats[0], stats[1]) != "alive":
            death_text(death_check(stats[0], stats[1]))
            death = "yes"
            break
        evening_game_test(stats)
        choice_2 = get_choice("evening")
        stats = change_the_stats_evening(choice_2, stats[0], stats[1], stats[2], stats[3])

        counter = counter - 1

    if death == "yes":
        endgame_text(stats, death)
    else:
        endgame_text(stats, death)
