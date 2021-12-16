d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1  #copiando objetos

# print(d1)
# print(v)  #você não cria um novo dicionário

# v[1] = 'Luís'

# print(d1)
# print(v)

# print(v == d1)

'''
shallow copy - Cópia rasa
'''
v = d1.copy()  #não foram copiados, são apenas referências
v[1] = 'Luís'

print(d1)
print(v)