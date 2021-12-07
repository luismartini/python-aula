'''
For / Else em Python
'''
variável = ['Luís Martini', 'Joãozinho', 'Maria']

comeca_com_j: False

for valor in variável:
    if valor.startswith('L'):
        print('Começam com L: ', valor)
#    print(valor) #as primeiras letras de cada valor
#    break
#    print(valor)
    else:
        print('Não começa com L: ', valor)