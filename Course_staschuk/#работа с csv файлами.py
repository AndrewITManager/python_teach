#работа с csv файлами
import csv
with open('test.csv', 'w') as csv_file: #создвник csv файла
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([5255, 'andrew', 1352])
    writer.writerow([4428, 'mike', 246])
    writer.writerow([1684, 'alice', 73])


with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for line in reader:
        print(line)

    print(reader.line_num)