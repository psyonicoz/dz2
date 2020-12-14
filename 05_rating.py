arr = [8, 4, 4, 3,]

while True:
    try:
        number = int(input("Введите натуральное число: "))
        num_check = arr.count(number)
        if 0 > number or number >= 10:
            raise Exception
        for element in arr:
            if num_check > 0:
                i = arr.index(number) + num_check
                arr.insert(i, number)
                break
            else:
                if number > element:
                    j = arr.index(element)
                    arr.insert(j, number)
                    break
                elif number < arr[len(arr) - 1]:
                    arr.append(number)
        break
    except ValueError:
        print('Вводите цифры')
    except Exception:
        print('Введите число 0 до 9')
print(arr)
