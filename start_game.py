from kod import kod

def start_game():
    name_y = input('Хотите начать?')
    if name_y == "Да":
        kod()
    elif name_y == "Нет":
        exit()
    else:
        print('Непонятно,повтори ещё раз')
        start_game()