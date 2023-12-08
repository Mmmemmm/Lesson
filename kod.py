def kod():
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                     'Сергей Робертович Цой': '21.06.1962', 'Владимир Семёнович Высоцкий': '25.01.1938'}

    rounds = int(input('Сколько раз вы хотите сыграть?:'))
    for i in range(rounds):
        name, date = random.choice(list(FAMOUS_PEOPLE.items()))
        answer = input(f'Когда родился {name}')
        if answer == date:
            print('Верно')
        else:
            print('Неверно')
    print('Пока')