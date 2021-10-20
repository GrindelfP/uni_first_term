number_of_floors = 5
number_of_entrances = 3
number_of_flats_of_floor = 4
number_of_flats = number_of_floors * number_of_entrances * number_of_flats_of_floor


def communication() -> int:
    global number
    flag = True
    print("Hello there! I'm Obi-Wan.")
    while flag:
        number = input("Type here your flat number (please use only integers): ")
        if number.count(".") > 0 or not number.isdigit():
            print("Such flats do not exist in our dimensions! I remind you - use only integer flat numbers!")
        else:
            if int(number) > 60 or int(number) < 1:
                print("Such flats do not exist in our house!")
            else:
                flag = False

    return int(number)


def find_flat_address(number_of_flat) -> list:
    if number_of_flat % 4 == 0:
        flat_code = 4
    else:
        flat_code = number_of_flat % 4

    flat_floor_code = int((number_of_flat - flat_code) / number_of_flats_of_floor + 1)
    if flat_floor_code % 5 == 0:
        flat_floor = 5
    else:
        flat_floor = flat_floor_code % 5

    if flat_floor_code <= 5:
        flat_entrance = 1
    else:
        flat_entrance = int(flat_floor_code // number_of_floors + 1)

    flat_address = [flat_entrance, flat_floor]

    return flat_address


flat_number = communication()

print('You can get to this flat through entrance number', find_flat_address(flat_number)[0],
      'and it is located on floor number', find_flat_address(flat_number)[1])
