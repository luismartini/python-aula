secreto = 'python'
secreto_temporário = ''

digitadas = ['t', 'p', 'y', 'n', 'o', 'h']


for letra_secreta in secreto:
    print(f'Iteração para letra {letra_secreta}')
    
    if letra_secreta in digitadas:
        print(f'Eba, a letra que eu queria {letra_secreta}')
        secreto_temporário += letra_secreta
    else:
        print(f'Essa letra eu não queria {letra_secreta}!')
        secreto_temporário += '*'
print()
print(secreto_temporário)

if secreto == secreto_temporário:
    print('Você ganhou!')