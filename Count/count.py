'''
Count - Intertools
'''

from itertools import count

contador = count()
lista = ['Luís', 'João', 'Maria']
lista = zip(contador, lista)
lista = dict(lista)
print(lista)