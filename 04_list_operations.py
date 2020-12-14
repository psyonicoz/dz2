abc = list(map(str, input('Введите значение массива через пробел ').split()))

for i in range(len(abc)):
    print(f'{i} : {abc[i][0:10]}')
