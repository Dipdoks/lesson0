first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

fi = map(len, first)
se = map(len, second)
first_result = (a - b for a, b in zip(fi, se) if a != b)

second_result = (len(first[c]) == len(second[c]) for c in range(len(first)))

print(list(first_result))
print(list(second_result))