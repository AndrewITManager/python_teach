#for in задача
def dict_to_list(dict_num):
    for key, value in dict_num.items():
        print(value)
    
        


dict_number = {
    'x': 5,
    'c': 4.5,
    'd': 8

}

print(dict_to_list(dict_number))