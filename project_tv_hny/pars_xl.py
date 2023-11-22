from openpyxl import load_workbook #импортируем модуль работы с excel
import datetime #импортируем модуль работы с датой


day = datetime.datetime.today().strftime("%d")#текущий день


book = load_workbook(filename="project_tv_hny\date_year.xlsx") #открываем книгу excel по указанному пути


sheet = book['TDSheet'] #выгружаем книгу TDSheet

#выполняем поиск и сравнение с текущей датой месяца, если соответсвует то выводим строку с определенными полями
for i in range(1, 490):
    try:
        day_of_birth = sheet['K' + str(i)].value.split('.')[0]
        if  day_of_birth == day:
            print(f"{sheet['I' + str(i)].value} -  {sheet['H' + str(i)].value} - {sheet['K' + str(i)].value.split('.')[0]}")

    except Exception as e:
        day_of_birth = ['0']
        
    """осталось вывести результат в соответсвующий файл для обработки в sdb complex
    """
    
    

