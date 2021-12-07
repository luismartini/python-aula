secreto = 'LUIS'
digitadas = []
chances = 3


while True:
    if chances <= 0:
        print('Você perdeu!')
        break
    
    letra = input('Digite uma letra: ').upper()
    
    if len(letra) > 1:
        print('Não! É apenas uma letra!')
        continue
    
    digitadas.append(letra)
    
    if letra in secreto:
        print(f'Aeee! A letra {letra} existe na palavra')
    else:
        print('Poxa, tente mais uma vez!')
        digitadas.pop()
    
    sec_temp = ''
    for letra_sec in secreto:
        if letra_sec in digitadas:
            sec_temp += letra_sec
        else:
            sec_temp += '*'
    
    if sec_temp == secreto:
        print('Que legal! Você ganhou!')
        break
    else:
        print(f'A palavra secreta está assim: {sec_temp}')
        
    if letra not in secreto:
        chances -= 1
    print(f'Você tem mais {chances} chances')
    print('Acabou')
