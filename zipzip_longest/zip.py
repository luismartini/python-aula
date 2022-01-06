"""
Zip - unindo iteráveis
Zip_longest - itertools
"""
from itertools import zip_longest, count

índice = count()
cidades = ['São Paulo', 'Belo Horizonte' , 'Rio de Janeiro', 'Bauru']
estados = ['SP', 'MG', 'RJ']

#zip une a menor lista
#zip_longest = fillvalue='Estado'
cidades_estados = zip(
    índice,
    estados, 
    cidades, 
    #fillvalue='Estado'
    )

for índice, estado, cidade in cidades_estados:
    #print(valor)  #gera loop infinito
    print(índice, estado, cidade)

# for valor in cidades_estados:
#     print(f'{valor[0]}, {valor[1]}')

# print(list(cidades_estados))