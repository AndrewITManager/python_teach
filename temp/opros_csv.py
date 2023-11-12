# import csv
import os
import pandas as pd
import numpy as np



print(os.getcwd())
# os.chdir('temp')
# print(os.getcwd())
path_f = os.getcwd()

# with open('template.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=';')
#     for row in reader:
#         print(row)

df = pd.read_csv('c:/Users/Xadmin/Desktop/python/python_teach-2/template.csv', delimiter=';', names=[
    'firstname', 'lastname', 'displayname', 'username', 'telephoneNumber', 'password',
    'departament', 'title','company', 'ou', 'mobile', 'description'
])
print(df)
