#значение параметров функции по умолчанию
def mult_by_factor(value, multiplier=1):#у второго параметра значение по умолчанию 1
    return value * multiplier

print(mult_by_factor(10, 2))
print(mult_by_factor(5))

from datetime import date


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):#второй параметр по умолчанию get_weekday
    post_copy = post.copy()#чтобы не изменять внешний объект
    post_copy['created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 243,
    'author': 'Bogdan',
}

post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)

print(get_weekday())
print(initial_post)
