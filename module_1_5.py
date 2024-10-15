immutable_var = 'text', 12, ['а', 'b', 'c']
print(immutable_var)
immutable_var[2][0] = 'l'
# immutable_var[0] = 'apple' --выдает ошибку ниже
print(immutable_var)
# изменять элемент в кортеже нельзя, код выдаст ошибку, это своего рода хранилище с защитой от перезаписи
# 'tuple' object does not support item assignment
# AttributeError: 'tuple' object has no attribute 'append'(также remove,extend)
# можно изменять в составе кортежа, значения, типа данных список по индексу хоть все
mutable_list = ['text', 12,'а', 'b', 'c']
print(mutable_list)
mutable_list[0] = 999
mutable_list[1] = 999
mutable_list[2] = 999
mutable_list[3] = 'Y'
mutable_list.append('apple')
mutable_list.remove('c')
print(mutable_list)
