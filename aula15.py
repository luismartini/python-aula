#formatar valores
#format e f-string
'''
:s - string
:d - inteiros (int)
:f - float
:. (número)f - quantidade de casas
:(caractere)(> ou < ou ^)
> Esquerda
< Direita
^ Centro
'''

# num_1 = 1
# num_2 = 1150
# # divisão = num_1 / num_2
# # #format
# print(f'{num_1:0>10}')
# print(f'{num_2:0^10}')
# # #print('{:.2f}'.format(divisão))
# # #print(f'{divisão:.2f}')

# # nome = 'Luís Martini'
# # print(f'{s}')

# num_3 = float(1500)
# print(f'{num_3:0>10.2f}')

#nome = 'Luís Martini'
# print(50 - len(nome) / 2)
# print(f'{nome:-^50}')
#print(len('-------------------'))

#.format
nome = 'Luís Martini'
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

#indices
nome = 'Luís Martini'
sobrenome = 'Martini'
nome_formatado = '{1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

#funções
nome = 'luís Martini'
print(nome.lower())
print(nome.upper())
print(nome.title())