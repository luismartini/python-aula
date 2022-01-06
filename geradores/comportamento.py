#Lista, tuples, str -> sequência -> iterável
nome = 'Luís Martini'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('Olha o FOR')

for letra in gerador:
    print(letra)
    
print('Olha o outro FOR')
for letra in gerador:
    print(letra)

# try:
#     print(next(iterador))  #L
#     print(next(iterador))  #u
#     # print(next(iterador))  #í 
#     # print(next(iterador))  #s

# except:
#     pass

# print('CADÊ OS VALORES')
# for valor in iterador:  #consumi os valores
#     print(valor)

# for letra in nome:
#     print(letra)

# print('#' * 30)

# for letra in nome:
#     print(letra)
    
# print(nome)

'''
GERADOR E ITERADORES SÕA FEITOS PARA CONSUMIR OS VALORES DELES
'''