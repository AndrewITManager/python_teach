#тернарный оператор
my_number = 21

print("is int") if type(my_number) is int else print("is not int")

if type(my_number) is int:
    print("is int")
else:
    print("is not int")

#
product_qty = 10
print("in stock" if product_qty > 0 else "out of stock")

#
temp = +24
weather = "hot" if temp > 18 else "cold"
print(weather)