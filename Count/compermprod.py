'''
Combination, Permutation e Product - itertools
combinação - Ordem não importa
Permutação - Ordem importa
Ambos - não repetem valores únicos
Produtor - Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product
pessoas = ['Luís', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

'''
Combinação - ordem não importa
'''
# for grupo in combinations(pessoas, 2):
#     print(grupo)
'''
Permutação - Ordem importa
'''
# for grupo in permutations(pessoas, 2):
#     print(grupo)

'''
produtor
products(pessoas, repeat=2)
'''
for grupos in product(pessoas, repeat=2):
    print(grupos)