family = ['Alex', 'Vincent', 'Anastasia', 'Nikolas', 'Andrey', 'Andrey']
print(family)

family_1 = {'Alex', 'Vincent', 'Anastasia', 'Nikolas', 'Andrey', 'Andrey'}
print(family_1)

family_2 = {
    'Dad': 'Nikolas',
    'Mom': 'Anastasia',
    'Son': 'Vincent',
    'Daughter': 'Alex'
    }
print(family_2['Dad'])

for k, v in family_2.items():
    print(k + ' - ' + v)