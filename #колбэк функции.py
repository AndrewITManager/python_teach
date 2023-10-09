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


def process_number(num, callback_fn):
    callback_fn(num)

entered_num = int(input('Enter any number: '))
process_number(entered_num, print_number_info)
