#docstrings


def mult_by_factor(value, mult=1):
    """_summary_

    Args:
        value (_type_): _description_
        mult (int, optional): _description_. Defaults to 1.
    """
    return value * mult

mult_by_factor(5)


def print_number_info(num):
    if (num % 2) == 0:
        print("Num is even")
    else:
        print("Num is odd")