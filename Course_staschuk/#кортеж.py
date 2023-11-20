#кортеж
my_fruits = ('apple', 'banana', 'lime')
post_ids = (151, 245, 762, 167)
print(len(my_fruits))
print(len(post_ids))

#получение значений
print(my_fruits[1])
print(my_fruits[0])
print(my_fruits[-1]) #получение последнего значения 
print(my_fruits[0] == my_fruits[1])
#my_fruits[1] = 'jug' изменять значения в кортеже нельзя
#del my_fruits[0] удалять значения в кортеже нельзя
print('')
#кортеж словарей
users =(
    {'user_id': 134,
    'user_name': 'Maria'
    },
    {'user_id': 831,
    'user_name': 'Andrew'
    }
)
print(users[1]['user_id'])
users[1]['user_id'] = 125
print(users[1]['user_id'])

#использование переменных
my_fr1 = 'banana'
my_fr2 = 'apple'
my_fr3 = 'orange'
all_fr = (my_fr1, my_fr2, my_fr3)
print(all_fr)
print('slozhenie tuple')
internal_ids = (151, 152)
external_ids = (243, 456, 345)
all_ids = internal_ids + external_ids
print(all_ids)
print('podschet kolichestva elemntov')
print(internal_ids.count(151))
print('podschet indexa elemente')
print(external_ids.index(456))
#конвертация в список кортежа
kor = (152, 156)
kor_list = list(kor)
kor_list.append(351)
print(kor)

kor_tuple = tuple(kor_list)

print(kor_tuple)




