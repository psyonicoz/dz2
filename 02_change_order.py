arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
el_count = 0

for i in range(int(len(arr) / 2)):
    arr[el_count], arr[el_count + 1] = arr[el_count + 1], arr[el_count]
    el_count += 2
print(arr)
