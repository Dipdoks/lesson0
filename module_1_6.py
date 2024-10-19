# 1. Практическое задание: "Словари и множества"
# 2. Работа со словарями:
my_dict = {'Aleksandr': 1989, 'Olga': 1991, 'Kot': 2019}
print(my_dict)
print(my_dict.get('Kot'))
print(my_dict.get('Anna','Нет такого ключа'))
my_dict.update({'Vasya': 1988, 'Anton': 1987})
Aleksandr = my_dict.pop('Aleksandr')
print(Aleksandr)
print(my_dict)
# 3. Работа с множествами:
my_set = {1, 1, 2, 'Street', 'Home', 'Home'}
print(my_set)
my_set.add(777)
my_set.add(999)
my_set.remove(1)
print(my_set)
