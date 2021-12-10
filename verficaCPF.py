cpf = '5028436098168'
novo_cpf = cpf[:-2]
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
    
if cpf == novo_cpf:
    print('Válido')
else:
    print('Inválido')
        

