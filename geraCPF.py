from random import randint
numero = str(randint(000000000, 999999999))

novo_cpf = numero
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    
#print(cpf[index], index, reverso)  #primeiro dígito
    total += int(novo_cpf[index]) * reverso
    
    #  gerando os dois últimos dígitos
    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        
        #gerando os dois últimos dígitos
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)