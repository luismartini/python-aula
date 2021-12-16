'''
Dicionários
índices e valores

Lista: python gera índice; 
no dicionário, você controla o índice.

Dicionário: chave/valor - chave- índice
{'chave': 'valor', 'chave2': 'valor2}
'''

# d1 = {'chave1': 'valor da chave'}
# d1['nova chave'] = 'Valor'

# print(d1)
# print(d1['chave1'])

'''
Outra forma de fazer dicionários
'''
# d1 = dict(chave1='Valor da chave', chave2='Valor2')  #menos usual
# d1['chave3'] = 'valor3'
# print(d1)

'''
Explicação importante
'''
# d2 = {'chave': 'valor', 'chave':'valor', 'chave': 'valor real da chave'}
# # Só verá o último valor se elas não forem únicas
# # Elas devem ser únicas

# print(d2)

# d3 = {1: 'valor', 2: 'valor', 3: 'valor'}
# print(d3[3])

'''
Criação de chaves - dados imutáveis
str : 'valor
123 : 'Outro valor
(1,2,3,4,5): 'valor 1'
'''

d1 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',
}
# d1['nãoexiste'] = 'Agora existe'

# if 'nãoexiste' in d1:
# #print(d1[(1,2,3,4)])  
#     print(d1['nãoexiste'])  #problemas que podem ocorrer
# print('Oi')

#d1['str'] = 'Agora ela existe'

# if d1.get('str') is not None:
#     print(d1.get('str'))  #None

# print(d1)

'''
Atualizar o valor da chave
update()
'''
# d1.update({'novachave':'novo_valor'})

# if d1.get('novachave') is not None:
#     print(d1.get('novachave'))

'''
Apagar
'''
# del d1['str']
# print(d1)

'''
Verificar
'''

# print('str' in d1)
# print('str' in d1.keys())
# print('valor' in d1.values())

'''
quantos pares valores
'''

# print(len(d1))

'''
Iterar
'''
# for k in d1:
#     print(k)
    
# for v in d1.values():
#     print(v)
    
# Para ver os dois

# for k in d1.items():
#     print(k[0], k[1])

'''
desempacotar
'''
for k, v in d1.items():
    print(k, v)