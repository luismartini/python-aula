'''
List Comprehension
Otimização
'''

l1 = [1, 2, 3, 4, 5, 6]
ex1 = [variável for variável in l1]

ex2 = [v * 2 for v in l1]

ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['Luís', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]


tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 =[(x, y) for x, y in tupla]

#inverter valores
ex6 = [(y, x) for x, y in tupla]
ex6 = dict(ex5)


#filtrar a lista
l3 = list(range(100))
ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]


#usar o else
ex8 = [v if v % 3 == 0 else 0 for v in l3]

# OR ou AND
ex9 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex9)