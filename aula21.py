'''
Listas = [] - ok
fatiamento - ok
append, isert, pop, clear, extend, +
min, max
range
[começo, fim, passo]
'''
#lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
#lista[5] = 'Qualquer outra coisa' modificar
#print(lista[::-1])
#[::-1] estou mostrando de trás para frente

# lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lista1)

#l1 = [1,2,3]
l2 = [4,5,6]
#l3 = l1 + l2
#l1.extend(l2) #extende/adiciona
#l1.extend('a') #adiciona ao final
#l2.append('b') #append - insere no final/ pode ser acessado
#insert - adiciona onde quiser
#pop remove o último elemento
#del(lista[índice])
#list(range(1,10))
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop()

#print(l1)
print(l2)
#print(l3)

l3 = [1,2,3,4,5,6,7,8,9]
l3.insert(0, 'Banana')
print(l3)

del(l3[0])
print(l3)

print(max(l3))
print(min(l3))

l4 = list(range(1,10))
print(l4)
# print(max(l4))
# print(min(l4))

l4.extend('Luís')
print(l4)

for valor in l4:
    print(valor)
