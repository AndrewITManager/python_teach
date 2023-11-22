from openpyxl import load_workbook #импортируем модуль работы с excel
import datetime #импортируем модуль работы с датой


day = datetime.datetime.today().strftime("%d.%m.%Y").split('.')[0:2]#текущий день, месяц


book = load_workbook(filename="project_tv_hny\date_year.xlsx") #открываем книгу excel по указанному пути


sheet = book['TDSheet'] #выгружаем книгу TDSheet


# day_of_birth = sheet['K6'].value.split('.')[0:2]
# print(day)
# print(day_of_birth)


# выполняем поиск и сравнение по текущей дате и месяцу, если соответсвует то выводим строку с определенными полями
for i in range(1, 500):
    try:
        day_of_birth = sheet['K' + str(i)].value.split('.')[0:2]
        if  day_of_birth == day:
            print(f"{sheet['I' + str(i)].value} -  {sheet['H' + str(i)].value} - {sheet['K' + str(i)].value.split('.')[0]}")

    except Exception as e:
        day_of_birth = ['0', '0']
        
    """осталось вывести результат в соответсвующий файл для обработки в sdb complex
    """
    
    

