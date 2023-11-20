#колбэк функции
def other_fn():
    pass #игнорируется, делает код валидным


def fn_with_callback(callback_fn):#колбэк функция
    callback_fn()


fn_with_callback(other_fn)


#пример функции
def print_number_info(num):
    if (num % 2) == 0:
        print("Enter number is even")
    else:
        print("Entered number is odd")

def print_square_num(num):
    print("Square of the num is", num*num)
    
    
def process_number(num, callback_fn):#колбэк функция
    callback_fn(num)


entered_num = int(input('Enter any number: '))
process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)


#пример два
def send_data(data):#отправка данных на сервер к примеру
    pass# чтобы функция была валидная


def process_data(input_data, send_data_fn):#обработка данных перед отправкой
    updated_data = input_data.copy()
    # actions with update_date
    send_data_fn(updated_data)
    
    
process_data({'name': 'Andrew'}, send_data)  
