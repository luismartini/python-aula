'''
Dicionários e sets
'''

# lista = [
#     ('chave', 'valor'),
#     ('chave1', 'valor1'),
# ]

# lista = [
#     ('chave', 'valor'),
#     ('chave1', 'valor1'),
# ]
#d1 = {k for k in range(5)}
#Output {0, 1, 2, 3, 4} <class 'set'>

d1 = {f'Chave {k}': k**2 for k in range(5)}
print(d1)  #{'Chave 0': 0, 'Chave 1': 1, 'Chave 2': 4, 'Chave 3': 9, 'Chave 4': 16}