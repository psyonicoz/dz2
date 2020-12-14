month = int(input('Введите номер месяца: '))
year = ['зима январь','зима февраль', 'весна март','весна апрель','весна май', 'лето июнь', 'лето июль', 'лето август', 'осень сентябрь', 'осень октябрь', 'осень ноябрь', 'зима декабрь',]

if 9 <= month <= 11:
    print(year[month-1])
elif 3 <= month <= 5:
    print(year[month-1])
elif 6 <= month <= 8:
    print(year[month-1])
else:
    print(year[month-1])
