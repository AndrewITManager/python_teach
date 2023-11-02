#задача запись чтение файла
from pathlib import Path #экземпляр класса

files_dir_path = Path('files')
files_dir_path.mkdir(exist_ok=True)#если такая ошибка есть то папка не будет сгенерирована

first_file = Path(files_dir_path / 'first.txt')
second_file = Path(files_dir_path / 'second.txt')

with open(first_file, 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")

with open(second_file, 'w') as f:
    lines = [
        "First line in the second file",
        "Second line in the second file",
        "Last line in the second file"
    ]
   
    for line in lines:
        f.write(line + '\n')

with open(first_file) as f:
    print(f.read())

with open(second_file) as f:
    for line in f.readlines():
        print(line)

first_file.unlink()
second_file.unlink()
files_dir_path.rmdir()#удаляет только пустую директорию











