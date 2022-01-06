
#lista que contém vários dicionários
alunos = [
    {'nome': 'Luís', 'nota': 'A'},
]
#  Como apresentar apenas os nomes?
# print(alunos[0]['nome'])
# print(alunos[0]['nota'])

notas = map(lambda a: a['nota'], alunos)

for nota in notas:
    print(nota)