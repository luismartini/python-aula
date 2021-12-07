'''
Desempacotamento de lista em Python!
'''
lista = ['Luís', 'João', 'Maria', 1,2,3,4,5,6,7,8,9,100]

#*outra_lista
#n1, n2, n3, *outra_lista, ultimo_da_lista = lista
#*outra_lista, n1, n2, n3, ultimo_da_lista = lista
n1, n2, *_ = lista

print(n1)
print(n2)
# print(outra_lista)
# print(ultimo_da_lista)