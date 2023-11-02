#мод регулярные выражения

import re

my_string = "My name is Andrew. Andrew is instructor"

res = re.search(r'A....w', my_string)
print(res)
print(type(res))

print(r'A....w\n.$')
print(res.span())
print(res.start())


my_pattern = re.compile(r'A..*w')
print(my_pattern)
print(my_pattern.search(my_string))
print(my_pattern.match(my_string))
print(my_pattern.findall(my_string))
