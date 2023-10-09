#объединение аргументов в dict
def get_postst_info(**person):#объединение аргументов
    print(person)#вывод словаря
    print(type(person))#вывод типа 
    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts"
    )
    return info

info = get_postst_info(name='Andrew', posts_qty=25)
print(info)