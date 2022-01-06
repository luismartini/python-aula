from dados import produtos, pessoas, lista
from functools import reduce

'''
Reduce = acumulador
vai somar e retornar um valor]
'''
# somaLista = reduce(lambda ac, i: i + ac, lista, 0)
# print(somaLista)

# somaPreços = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
# print(somaPreços / len(produtos))

somaIdades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(somaIdades / len(pessoas))