#функция zip
fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]

fruit_qtys_zip = zip(fruits, quantities)

print(fruit_qtys_zip)
print(type(fruit_qtys_zip))

#fruit_qtys_list = list(fruit_qtys_zip)
#(fruit_qtys_list)

fruit_qtys_dict = dict(fruit_qtys_zip)
print(fruit_qtys_dict)
