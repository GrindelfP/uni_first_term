from quest.utility import rules


def intro() -> None:
    print("Добро пожаловать в игру '10 DAYS'!"
          "\nПосле долгих мучений по сдаче ЕГЭ, поступления и надежд пройти вы находите себя в списках зачисленных."
          "\nСамое время прийти в себя и вспомнить свое имя!")
    players_name = getting_name()
    print("\nОтлично,", players_name + ",", "давайте немного поговорим о правилах...\n")


def giving_rules() -> None:
    rules()
    global_flag = True
    while global_flag:
        flag = True
        answer = None
        while flag:
            answer = input("\nНу, что же, вам все понятно? ")
            if answer != "Да" and answer != "Нет" and answer != "да" and answer != "нет" \
                    and answer != "ДА" and answer != "НЕТ":
                print("Я вас немножко не понял!")
            else:
                flag = False
        if answer == "Да" or answer == "да" or answer == "ДА":
            print("Тогда мы начинаем!")
            global_flag = False
        else:
            print("\nПовторим правила!\n")
            rules()


def end_of_intro() -> None:
    print("\nТяжелая учеба заставила вас потерять счет времени... "
          "\nСейчас некий день некоей недели..."
          "\nВам только хочется спать. Ничто больше не движет вашим первобытным мозгом..."
          "\nВы входите в университет.")


def getting_name() -> str:
    return input("Введите свое имя: ")


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

