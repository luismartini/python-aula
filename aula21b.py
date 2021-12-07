# l1 = ['String', True, 10, -20.5]

# for elem in l1:
#     print(f'O tipo de elememento é {type(elem)} e seu valor é {elem}')
    
secreto = 'perfume'
digitadas = [] #a ser preenchida
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break
    
    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print('Ahhhh! Isso não vale. Digite apenas uma letra!')
        continue
    
    digitadas.append(letra) #adicionar
    
    if letra in secreto:
        print(f'UHUULLLL, a letra {letra} existe na palavra secreta')
    else:
        print(f'Tente outra vez! A letra {letra} NÃO existe na palavra secreta')
        digitadas.pop()
    
    secreto_temporário = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporário += letra_secreta #concatenando
        else:
            secreto_temporário += '*'
        
    
    if secreto_temporário == secreto:
        print('Que legal! Você ganhou')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporário}')
        
    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances')
    print()