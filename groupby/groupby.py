'''
groupby:
agrupar elementos usando dicionários
'''
from itertools import groupby, tee
#lista que contém vários dicionários
alunos = [
    {'nome': 'Luís', 'nota': 'A'},
    {'nme': 'Jonice', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'E'},
    {'nome': 'Cácio', 'nota': 'B'},
    {'nome': 'Gilberto', 'nota': 'C'},
    {'nome': 'Luísa', 'nota': 'A'},
    {'nome': 'Lauro', 'nota': 'D'},
    {'nome': 'Letícia', 'nota': 'E'},
    {'nome': 'Líria', 'nota': 'A'},
    {'nome': 'Sofia', 'nota': 'B'},
]
# chave - nome do aluno
# valor - nota

#usar função lambda

ordenaNota = lambda item: item['nota']
alunos.sort(key=ordenaNota)

#Agrupar em dicionários por nota
alunosAgrupados = groupby(alunos, lambda item: item['nota'])
#
for agrupamento, valoresAgrupados in alunosAgrupados:
    va1, va2 = tee(valoresAgrupados)

#
    print(f'Agrupamento de alunos que tiraram a nota: {agrupamento}')
    
    aluno = ['nome']
    for aluno in va1:
        print(f'\t{aluno}')

    
    quantidade = len(list(va2))
    print(f'\t{quantidade} de alunos tiraram a nota {agrupamento}')
    print()
