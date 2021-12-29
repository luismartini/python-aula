'''
groupby - agrupar elementos em um dicionário
'''
from itertools import groupby, tee

# Lista que contém dicionários
alunos = [
    {'nome': 'Luís', 'nota': 'A'},
    {'nome': 'Jonice', 'nota': 'B'},
    {'nome': 'Letícia', 'nota': 'C'},
    {'nome': 'Rose', 'nota': 'D'},
    {'nome': 'Mary', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'João', 'nota': 'A'},
]
# alunos.sort(key=lambda item: item['nota'])
# for aluno in alunos:
#     print(aluno)
# Agrupar em dicionários por notas

ordena = lambda item: item['nota']
alunos.sort(key=ordena)  #precisa ordenar os dados
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')
    
    for aluno in va1:
        print(f'\t{aluno}')
        
    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
    # for aluno in valores_agrupados:
    #     print(aluno)