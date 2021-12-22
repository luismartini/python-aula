'''
List Comprehension
'''
l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
# Criando uma nova lista

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
#v itera sobre a lista
#v2 sobre cada elemento da lista

l2 = ['Luís', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@') for v in l2]
#para cada valor, substituo o a por @

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(y,x) for x,y in tupla]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex6)