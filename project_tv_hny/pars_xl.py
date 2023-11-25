from openpyxl import load_workbook #импортируем модуль работы с excel
import datetime #импортируем модуль работы с датой


#перевод текущего дня и месяца в слова
def get_date(date):
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('.')
    return (date_list[0] + ' ' +
        month_list[int(date_list[1]) - 1])


day = datetime.datetime.today().strftime("%d.%m")#текущий день, месяц
# print(day)
d = get_date(day) #для параметра в XML
# day_1 = datetime.datetime.today().strftime("%d.%m.%Y").split('.')[0:2]#текущий день, месяц

########################################################################################################

book = load_workbook(filename="project_tv_hny\date_year.xlsx") #открываем книгу excel по указанному пути


sheet = book['TDSheet'] #выгружаем книгу TDSheet


# day_of_birth = sheet['K6'].value.split('.')[0:2]
# print(day)
# print(day_of_birth)


list_name = []


# выполняем поиск и сравнение по текущей дате и месяцу, если соответсвует то выводим строку с определенными полями
for i in range(1, 500):
    try:
        day_of_birth = sheet['K' + str(i)].value.split('.')[0:2]
        if  day_of_birth == day:
            # print(f"{sheet['I' + str(i)].value} -  {sheet['H' + str(i)].value} - {sheet['K' + str(i)].value.split('.')[0]}")
            list_name.append(f"{sheet['I' + str(i)].value}")

    except Exception as e:
        day_of_birth = ['0', '0']

#######################################################################################################
 
#проверка именниников в этот день       
if len(list_name) > 0:
    n = (" ".join(list_name))#объеденяем спискок в одну строку
    p = "Поздравляем именниников"
    s = "С днём рожденья!!!"
else:
    p = ""
    s = ""
    n = ""





#создаем XML файл для импорта в sdb_complex_manager

 # Загружаем библиотеку
from lxml import etree
    
# Создаем основной элемент, в который будем добавлять последующие
root = etree.Element('root') 

# Добавляем дату
date_f = etree.SubElement(root, 'date')
date_f.set("name", "d1")
date_f.set("value", f"{d}")

# Добавляем заголовок
heading = etree.SubElement(root, 'heading')
heading.set("name", "a1")
heading.set("value", f"{p}")

people = etree.SubElement(root, 'people')
people.set("name", "p1")
people.set("value", f"{n}")

basement = etree.SubElement(root, 'basement')
basement.set("name", "s1")
basement.set("value", f"{s}")

# Посмотрим получившийся xml
print(etree.dump(root))

#создание xml документа
tree = etree.ElementTree(root)

#запись XML в файл
with open("people.xml", "wb") as file:
    file.write(etree.tostring(tree, pretty_print=True))
