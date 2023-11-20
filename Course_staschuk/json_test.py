#json_test
import json
import os
from pathlib import Path

print(os.getcwd())
print(os.listdir('json_test'))

json_t = Path('./json_test/template.json')
print(json_t)

# with open(json_t) as file:
#     templates = json.load(file)

# print(templates)

# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))