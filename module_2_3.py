my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0 # для перебора индексов +1

while index < len(my_list):
    if my_list[index] > 1:
        print(my_list[index])
        index = index + 1
    else:
        index = index + 1
    continue
    print('Не выведется на экран')
















