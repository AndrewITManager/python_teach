"""объединение словарей с помощью **
"""
button_info = {
    'text': 'Buy',
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height':300
}

button = {
    **button_info,
    **button_style,
}

print(button)
print(button['color'])

button_two = button_info | button_style #объединение с помощью |
button_two['form'] = 'cube'
print(button_two)