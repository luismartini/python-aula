'''
Combinations, Permutations, e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product

#ordem não importa
pessoas = ['Luís', 'Jonice', 'André', 'Letícia', 'Rose']
#                                    #quanto grupos eu quero
# for grupo in combinations(pessoas, 2): 
#     print(grupo)

# Ordem importa
# for grupo in permutations(pessoas, 2):
#     print(grupo)

# Product repete valores únicos
for grupo in product(pessoas, repeat=2):
    print(grupo)
