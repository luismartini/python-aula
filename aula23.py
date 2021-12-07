'''
Split, join, enumerate
* Split - dividir uma string
* join - juntar uma lista #str
* enumerate - enumerar elementos da lista - objetos iteráveis
'''
string = "O Brasil é o país do futebol, o Brasil é penta."
lista1 = string.split(' ') # => separa em lista
lista2 = string.split(',')
#print(lista1)
#print(lista2)

for valor in lista1:
    #print(valor)
    #print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase') #contar quantas palavras apareceu na frase

    palavra = ''
    contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)
    
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')