import os

print(os.getcwd())#вывод текущей дириктории

# os.mkdir("folder") #создание каталога

if not os.path.isdir("temp"):
    os.mkdir("temp")

os.chdir("temp") #изменение текущего каталога
print(os.getcwd())
# os.chdir("..") #возврат к пред дириктории
# print(os.getcwd())

print(os.listdir())#имена папок и файлов
# text_file = open("test.txt", "r")
# text_file.close()
with open('test.txt') as text_file:
    print(text_file.read())

with open('test.txt', 'r+') as text_file:
    print(text_file.read(8))
    print(text_file.read(5))
    print(text_file.read(4))
    print(text_file.read())

with open('test.txt', 'r+') as text_file:
    # print(text_file.read())
     list_with_symbol = [i for i in text_file.read() if not i == ' ']
     print(f"kolichestvo symbolov = {len(list_with_symbol)}")

# with open('dict_1.py') as f:
#     print(f.readlines())


     

        
    
    

