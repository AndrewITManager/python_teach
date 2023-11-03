#отправка по шаблону html
from email.message import EmailMessage #создание сообщения
import smtplib #настройка отправки сообщений
from string import Template#импорт шаблона из модуля
from pathlib import Path#чтобы создать путь к  шаблонуhtml

my_email = EmailMessage()

html_tempate = Template(Path("templates/index.html").read_text())#считываем шаблон html
html_content = html_tempate.substitute({'name': 'Andrew', 'date': 'tomorrow'})#замена переменных в шаблоне

#формирование контента
my_email['from'] = 'Andrew'
my_email['to'] = 'friend@email.com'
my_email['subject'] = "Let's go out"
my_email.set_content(html_content, 'html')#передача контента в формате html

with smtplib.SMTP(host='192.168.0.1', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls() # если нужна авторизация
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print('Email was sent!')