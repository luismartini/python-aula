from itertools import groupby, tee

alunos = [
    {'nome': 'Luís', 'nota': 'A'},
    {'nome': 'Jonice', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'E'},
    {'nome': 'Cácio', 'nota': 'B'},
    {'nome': 'Gilberto', 'nota': 'C'},
    {'nome': 'Luísa', 'nota': 'A'},
    {'nome': 'Lauro', 'nota': 'D'},
    {'nome': 'Letícia', 'nota': 'E'},
    {'nome': 'Líria', 'nota': 'A'},
    {'nome': 'Sofia', 'nota': 'B'},
]

ordenaNotas = lambda item: item['nota']
alunos.sort(key=ordenaNotas)

alunosAgrupados = groupby(alunos, lambda item: item['nota'])

for agrupamentos, valorAgregado in alunosAgrupados:
    va1, va2 = tee(valorAgregado)
    print(f'Agrupamento de alunos que tiraram a nota {agrupamentos}')
    
    ordenaAlunos = lambda item: item['nome']

    notasAgrupadas = groupby(alunos, lambda item: item['nome'])
    
    # c = 1
    for aluno in va1:
        print(f"\t{aluno['nome']}")
        # c += 1


    # for aluno, valorAgrupado in notasAgrupadas:
    #     va1, va2 = tee(valorAgrupado)
    #     print(f'{aluno}')