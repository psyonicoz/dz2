year = {
    'зима': [12, 1, 2, ],
    'весна': [3, 4, 5, ],
    'лето': [6, 7, 8, ],
    'осень': [9, 10, 11, ],
}

while True:
    try:
        month = int(input('Введите номер месяца: '))
        if 0 >= month or month > 12:
            raise Exception
        for key in year.keys():
            if month in year[key]:
                print(f'Время года: {key}')
        break
    except ValueError:
        print('Вводите цифры')
    except Exception:
        print('Введите номер месяца от 1 до 12')
