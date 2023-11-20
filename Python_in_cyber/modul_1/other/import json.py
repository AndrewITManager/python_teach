import json

# Функция для загрузки данных из JSON-файла
def load_data(filename):
    # Открытие файла для чтения
    with open(filename, 'r', encoding='utf-8') as file:
        # Загрузка данных из файла и возврат их
        return json.load(file)

# Функция для сохранения данных в JSON-файл
def save_data(data, filename):
    # Открытие файла для записи
    with open(filename, 'w', encoding='utf-8') as file:
        # Сохранение данных в формате JSON с отступами для лучшей читаемости
        json.dump(data, file, ensure_ascii=False, indent=4)

# Функция для сравнения и синхронизации данных
def synchronize_data(base_data, updated_data):
    # Преобразование списка словарей в словарь с ключами по id для удобства доступа
    base_data_indexed = {item['id']: item for item in base_data}
    updated_data_indexed = {item['id']: item for item in updated_data}

    # Определение добавленных элементов
    added = [item for item_id, item in updated_data_indexed.items() if item_id not in base_data_indexed]
    # Определение удаленных элементов
    removed = [item for item_id, item in base_data_indexed.items() if item_id not in updated_data_indexed]
    # Определение измененных элементов
    modified = [updated_data_indexed[item_id] for item_id, item in updated_data_indexed.items()\
                if item_id in base_data_indexed and item != base_data_indexed[item_id]]

    # Создание синхронизированного списка, включающего все элементы из обновленного набора данных
    synchronized = list(updated_data_indexed.values())

    # Сохранение синхронизированных данных в новый файл
    save_data(synchronized, 'synchronized_data.json')

    # Создание отчета о изменениях
    report = {
        'added': len(added),   # Количество добавленных элементов
        'removed': len(removed),   # Количество удаленных элементов
        'modified': len(modified)  # Количество измененных элементов
    }
    # Вывод отчета в консоль
    print(report)
    # Возврат синхронизированных данных и отчета
    return synchronized, report

# Основная функция
def main():
    # Загрузка базовых данных
    base_data = load_data('base_data.json')
    # Загрузка обновленных данных
    updated_data = load_data('updated_data.json')
    # Синхронизация данных и получение отчета
    synchronized, report = synchronize_data(base_data, updated_data)

# Проверка, что скрипт не импортирован, а запущен напрямую
if __name__ == "__main__":
    main()
