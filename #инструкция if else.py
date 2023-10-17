#инструкция if else
my_number = 21.5

if type(my_number) is int:
    print(my_number, "is integer")
else:
    print(my_number, "is not an integer")


my_phone = {
    'price': 200,
    #'brand': 'nokia',
}  

if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")

