#аргументы функции
def sum_nums(*args): #объединение аргументов в tuple, любое количество
    print(args)
    print(type(args))
    print(args[0])
    return sum(args)

print(sum_nums(2, 3, 7))

#позиционные аргументы
def get_posts_info(name, posts_qty):#параметры
    info = f"{name} wrote {posts_qty} posts"#динамическая строка
    return info

info = get_posts_info('Sanya', 23)#важен порядок
print(info)

#аргументы с ключевыми словами
info2 = get_posts_info(posts_qty= 22, name='Sanyo')
print(info2)

#объединение аргументов в словарь
def get_posts(**person):
    print(person)
    print(type(person))
    info = (
        f"{person['name']} wrote"
        f"{person['posts_qty']} posts"
        
    )
    return info
info = get_posts_info(name='sanya', posts_qty=25)
print(info)


