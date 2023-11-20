#задача запись чтение файла
from pathlib import Path #экземпляр класса

files_dir_path = Path('files')
files_dir_path.mkdir(exist_ok=True)#если такая ошибка есть то папка не будет сгенерирована

first_file = files_dir_path / 'first.txt'
second_file = files_dir_path / 'second.txt'

with open(first_file, 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")

with open(second_file, 'w') as f:
    lines = [
        " First line in the second file",
        " Second line in the second file",
        "Last line in the second file "
    ]
   
    for line in lines:
        f.write(line + '\n')

with open(first_file) as f:
    print(f.read())

with open(second_file) as f:
    ### option one ####
    for line in f:
        print(line.strip())
    ### option two ####    
    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     print(line.strip())#метод strip убирает лишние пробелы и \n

first_file.unlink()#удаляем файл first.txt в директории
second_file.unlink()#удаляем файл second.txt в директории
files_dir_path.rmdir()#удаляет только пустую директорию











