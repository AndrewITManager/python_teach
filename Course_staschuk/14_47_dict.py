#Slovari
my_motorbike = {
    'brand' : 'Ducati',
    'price' : 25000,
    'engine_vol' : 1.2,
}
other_motorbike = {
    'price' : 25000,
    'engine_vol' : 1.2,
    'brand' : 'Ducati',
}
print(my_motorbike)
print(other_motorbike)
print(my_motorbike == other_motorbike)

print(other_motorbike['price'])

print(dir(my_motorbike))

print(my_motorbike['brand'])
#изменение значения ключа
my_motorbike['price'] = 7000
print(my_motorbike)

#добавление ключ-значение
my_motorbike['is_new'] = True
print(my_motorbike)

# удаление элементов
del my_motorbike['engine_vol']
print(my_motorbike)

#доступ к значению элемента с помощью переменной

key_name = 'brand'
my_motorbike[key_name] = 'BMV'
print(my_motorbike)

#вложенный словарь
my_bike = {
    'brand': 'Ducati',
    'engine_vol': 1.2,
    'price_info': {
        'price': 2500,
        'is_available': True,
    }
}

print(my_bike['price_info']['price'])
print(my_bike['price_info']['is_available'])

#переменные для создания словарей, название словарей и ключей могут не совподать
brand = 'Ducati'
bike_price = 25000
engine_volume = 1.2

my_bike1 = {
    'brand': brand,
    'price': bike_price,
    'engine_vol': engine_volume,
}
print(my_bike1)

#длина словаря
print(len(my_bike1))
del my_bike1['price']
print(len(my_bike1))

#несуществующие ключи, метод get для получения значений ключей
#print(my_bike1['model']) возникнет ошибка
print(my_bike1.get('model'))
print(my_bike1.get('model',0)) #вместо None получаем 0
print(my_bike1.get('brand'))
print(my_bike1.get('price'))
print(my_bike1.get('qty', 0))

#метод
my_dict = {}
print(my_dict.__doc__)







