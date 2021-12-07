variável = ['Luís Martini', 'Joãozinho', 'Maria']

comecaj = False

for valor in variável:
    if valor.lower().startswith('j'):
#        print('Uma palavra começa com J.')
#        pass
        continue
    print(valor)
#        break
#else:
#    print('Não existe uma palavra que começa com J.')