#проверка присутствия директории или файла
from pathlib import Path
print(Path('main.py').exists())
print(Path('/Users/Xadmin/Desktop').exists())
print(Path('other.py').exists())


print('')

#директория или файл?
print(Path('main.py').is_file())
print(Path('../python').is_file())
print(Path('../python_teach-2').is_dir())

