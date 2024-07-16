my_dict = {'Вася':1980, 'Петя':1946, 'Коля':1967}
print(my_dict)
print(my_dict['Коля'])
print(my_dict.get('Люся','Такого ключа нет'))
my_dict.update({'Зина':1978,
                'Нюра':1955})
print(my_dict)
z = my_dict.pop('Петя')
print(z)
print(my_dict)
#
my_set = {1,1,1,5.4,5.4,'Qwert',(56,98,25), True}
print(my_set)
my_set.update({5,8})
print(my_set)
my_set.remove(5.4)
print(my_set)
