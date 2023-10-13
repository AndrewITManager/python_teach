#операто распоковки славоря

button = {
    'width': 200,
    'text': 'Buy',
    'color': 'blue',
}

red_button = {
    **button,#распаковка словаря, если есть похожий ключ, то он перезапишется
    'color': 'red',
}

gray_button = {
    'color': 'gray',
    **button,
}

print(red_button)
print(gray_button)
print(button)
