 # Загружаем библиотеку
from lxml import etree

# Создаем основной элемент, в который будем добавлять последующие
root = etree.Element('root') 

# Добавляем дату
date_f = etree.SubElement(root, 'date')
date_f.set("name", "d1")
date_f.set("value", "24 ноября")

# Добавляем заголовок
heading = etree.SubElement(root, 'heading')
heading.set("name", "a1")
heading.set("value", "Поздравляем именниников")

people = etree.SubElement(root, 'people')
people.set("name", "p1")
people.set("value", "Акимов Андрей Петрович Адамсон Влада Марисовна Андросенко Надежда Валерьевна Антипина Ольга Васильевна Бабанин Сергей Юрьевич Балашов Кирилл Сергеевич")

# Посмотрим получившийся xml
print(etree.dump(root))

#создание xml документа
tree = etree.ElementTree(root)

#запись XML в файл
with open("people.xml", "wb") as file:
    file.write(etree.tostring(tree, pretty_print=True))