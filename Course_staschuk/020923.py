users = [
    {
        'user_id' : 134,
        'user_name' : 'Alice'
    },
    {
        'user_id' : 831,
        'user_name' : 'Bob'
    }
    
]
print(len(users))
print(users[1]['user_id'])
print(users[0]['user_name'])
#42

happy_smiles = []
happy_smiles.append('one')
happy_smiles.append('two')
happy_smiles.append('free')
happy_smiles.append('six')

print(happy_smiles)
happy_smiles.pop()
print(happy_smiles)
happy_smiles.pop(0)
removed_element = happy_smiles.pop()
print(removed_element)
print(happy_smiles)


