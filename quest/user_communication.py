from quest.back_end import change_the_stats_lections, change_the_stats_evening, giving_rules, intro, end_of_intro
from quest.utility import lessons_game_test, stats_keeping, evening_game_test, endgame_text


def greetings() -> None:
    intro()
    giving_rules()
    end_of_intro()


def processing_game():
    counter = 10
    stats = stats_keeping()
    while counter > 0:
        lessons_game_test(counter, stats)
        choice_1 = input("\nВаш выбор: ")
        stats = change_the_stats_lections(choice_1, stats[0], stats[1], stats[2], stats[3])

        evening_game_test(stats)
        choice_2 = input("\nВаш выбор: ")
        stats = change_the_stats_evening(choice_2, stats[0], stats[1], stats[2], stats[3])

        counter = counter - 1

    endgame_text(stats)
