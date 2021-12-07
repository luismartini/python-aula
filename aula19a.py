frase = 'Eu te amo, Jô'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

#input_usuario = input('Qual letra você quer que seja maiúscula: ')


while contador < tamanho_frase:
    #letra = frase[contador]
    
    #if letra == input_usuario:
        #nova_string += input_usuario.upper()
    nova_string += frase[contador]
    print(nova_string)
    contador += 1
