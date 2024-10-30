immutable_var = (1, 'a', 3.1, True)
print(immutable_var)

#immutable_var[0] = 3
#print(immutable_var)
#TypeError: 'tuple' object does not support item assignment
#Кортеж относится к неизменяемым типам данных

mutable_list= [1, 'a', 3.1, True]
mutable_list[0] = 3
mutable_list[1] = 'b'
print(mutable_list)