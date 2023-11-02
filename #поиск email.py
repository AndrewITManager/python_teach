#поиск email
import re

def chek_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "valid" if email_check_pattern.fullmatch(email) else "not valid"
    return (email, validation_result)


print(chek_email('bs@gmail.com'))
#Invalid
print(chek_email('bsgmail.com'))
print(chek_email('@gmail.com'))
print(chek_email('bs@com'))

