'''
Manipulando strings - Aula 6
* Strings índices
* fatiamento de strings [início:fim:passo]
funções built-in len, abs, type, print, etc
'''

# positivos
#       [012345678]
texto = 'Python S2'
#        987654321      
print(texto[2])
print(texto[0:3])
print(texto[8])
print(texto[1:8:2])

url = 'www.google.com.br/'
print(url[:-1])

#fatiamento
nova_string = texto[::]
print(nova_string)

#built-in - len
print(len(texto))

for letra in enumerate(texto):
    print(letra)
