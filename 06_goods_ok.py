goods = int(input("Введите количество товара "))
dict1 = []
arr = []
analytics = {
    'название': [],
    'цена': [],
    'количество': [],
    'eд': [],
}

for i in range(goods):
    dict1 = dict({'название': input("Введите название "), 'цена': input("Введите цену "),
                  'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    arr.append((i+1, dict1))
    for j in analytics.keys():
        analytics[j] += [dict1[j]]
print(arr)
print(analytics)
