#наследование из других классов
class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")

custom_lists = ExtendedList([3, 5, 2])
custom_lists.print_list_info()
