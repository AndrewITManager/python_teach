#работа с файлами
from os import path#объект path - функциональный подход

print(path.abspath('.'))#абсолютный путь к текущей папке
print(type(path))

print('')

from pathlib import Path#импортируем класс Path - объектноориентированный подход
print(Path('.').absolute())#экземпляр класса Path
print(type(Path))

print('')

file_path = Path('test.txt')
print([m for m in dir(file_path)
if not m.startswith('_')])#атрибуты pathlib path

print('')

#путь к текущей директории
from pathlib import Path
print(Path.cwd())#cdw - current working directory

#формирование путей на Windows
print(Path('C:/').joinpath('Users').joinpath('andrew'))
print(Path('C:/') / 'Users' / 'andrew')


