'''
For in em Python
Iterando strings com for
função range(start=0, stop, step=1)
enumerate
(0, 'P')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')
'''
#texto = 'Python'

# for letras in texto:
#     print(letras)
    
# for n in range(0, 10, 1):
#     print(n)

#Tabuada
# num = int(input('Digite um número: '))
# for c in range(0, 11):
#     print(f'{c:2} x {num} = {c * num}')
print('#'*20)
# for n in range(100):
#     if n % 8 == 0:
#         print(n)
texto = 'Python'
nova_string = ''

#continue - pula para o próximo laço
#break - encerra o laço

for letra in texto:
    if letra == 't':
        #continue #não terei a letra t
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        #break #Pyth
    else:
        nova_string += letra
print(nova_string)