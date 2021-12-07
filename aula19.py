'''
Iterando strings com While
iterar é passar por cada índice da string
'''
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_usuario = input('Qual letra você quer que seja maiúscula: ')


while contador < tamanho_frase:
    letra = frase[contador]
    
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)