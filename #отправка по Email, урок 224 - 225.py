#отправка по Email, урок 224 - 225
from email.message import EmailMessage #создание сообщения
import smtplib #настройка отправки сообщений

my_email = EmailMessage()
my_email['from'] = 'Andrew'
my_email['to'] = 'test@email.com'
my_email.set_content("Hey! Are you doing?")

with smtplib.SMTP(host='192.168.0.1', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls() # если нужна авторизация
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print('Email was sent!')

