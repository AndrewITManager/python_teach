#filter list задача
print(isinstance(True, bool))
print(isinstance(True, int))
print(isinstance(True, object))
print(int.__subclasscheck__)

def filter_list(list_to_filter, value_type):
    def chek_element_type(elem):
        return isinstance(elem, value_type)
    return list(filter(chek_element_type, list_to_filter))

res = filter_list([1, 10, 'abc', 5.5], int)
print(res)

