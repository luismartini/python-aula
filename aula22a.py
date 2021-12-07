variável = ['Luís Martini', 'Joãozinho', 'Maria']

comecaj = False

for valor in variável:
    if valor.lower().startswith('j'):
        comecaj = True

if comecaj:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')