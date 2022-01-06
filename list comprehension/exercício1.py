string = '0123456789012345678901234567890123456789'

'''
separar em grupos de 0 a 9
'''

'''
print(lista)
Output
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
'''
n = 10
# Fazer o fatiamento da string
#contadores = [i for i in range(0, len(string), n)]
# tuplas = [(i, i + n) for in range(0, len(string), n)]
lista = [string[i: i + n] for i in range(0, len(string), n)]

'''
Output
[(0, 10), (10, 20), (20, 30), (30, 40)]
['0123456789', '0123456789', '0123456789', '0123456789']
'''
retorno = '.'.join(lista)
print(lista)
print(retorno)
'''
0123456789.0123456789.0123456789.0123456789
'''