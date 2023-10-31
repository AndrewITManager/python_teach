#наследование из других классов
class ExtendedList(list):#подкласс класса list
    def print_list_info(self):
        print(f"List has {len(self)} elements")

custom_lists = ExtendedList([3, 5, 2, 6])
custom_lists.print_list_info()

custom_lists.reverse()
custom_lists.append(8)
print(custom_lists)
print(custom_lists.__dict__)
print(ExtendedList.__dict__)
print(list.__dict__)
print(list.__subclasses__())
