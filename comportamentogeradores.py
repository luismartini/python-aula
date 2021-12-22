'''
Exercício proposto
'''
nome = 'Luís Martini'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('Olha o FOR')
for valor in gerador:
    print(valor)

print('Olha o outro FOR')
for valor in gerador:
    print(valor)
# try:
#     print(next(iterador))  #L
#     print(next(iterador))  #u
#     print(next(iterador))  #í
#     print(next(iterador))  #s
#     print(next(iterador))  # 
#     print(next(iterador))  #M
#     print(next(iterador))  #a
#     print(next(iterador))  #r
#     print(next(iterador))  #t
#     print(next(iterador))  #i
#     print(next(iterador))  #n
#     print(next(iterador))  #i
#     print(next(iterador))
# except:
#     pass
#print(next(iterador))  #StopIteration




# for letra in nome:  #stopIteration
#     print(letra)
# print('#' * 30)
# print(nome)


