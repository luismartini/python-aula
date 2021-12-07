string = 'O Brasil é penta'
lista = string.split(' ') #lista
string2 = ' '.join(lista) #juntar a lista

# print(string)
# print(lista)
# print(string2)

'''
Enumerate
'''
    #desempacotando
# for indice, valor, in enumerate(lista):
#     print(indice, valor)
    
lista = ['Luís', 'João', 'Maria']
for nome in (lista):
    print(nome)
    
lista1 = [1,2,3,4,5]
for i, v in enumerate(lista1):
    print(i, v)
print('XXXXXXXXXXXXXXXXXXX')
lista2 = [
    [0, 'Luís'],
    [1, 'João'],
    [2, 'Maria'],
]

for indice, nome in lista2:
    print(indice, nome)
    
print('XXXXXXXXXXXXXXXX')

lista3 =['Luís', 'João', 'Maria']
for indice, nome in enumerate(lista3):
    print(indice, nome)