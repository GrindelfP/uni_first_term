from quest.back_end import check_choice
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
            answer = input("\nНу, что же, вам все понятно? (да/нет) ")
            if answer.upper() != "ДА" and answer.upper() != "НЕТ":
                print("Я вас немножко не понял!")
            else:
                flag = False
        if answer.upper() == "ДА":
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


def get_choice(type_of_choice) -> str:
    flag = True
    while flag:
        choice = input("\nВаш выбор: ")
        if check_choice(type_of_choice, choice):
            return choice
        else:
            print("Вы выбрали несуществующий вариант! попробуйте снова!")
