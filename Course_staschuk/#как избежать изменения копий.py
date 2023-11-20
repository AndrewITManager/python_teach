#как избежать изменения копий
info = {
    'name': 'Bogdan',
    'is_instruktor': True,
    'reviews': [],
}

info_copy = info.copy()
info_copy['reviews'].append('Great course')
info_copy['reviews'].append('Super')

print(info)
print(info_copy)

#глубокая копия объекта
from copy import deepcopy
word = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': [],
}
word_deepcopy = deepcopy(word)
word_deepcopy['reviews'].append('Great course!')

print(word)
print(word_deepcopy)

