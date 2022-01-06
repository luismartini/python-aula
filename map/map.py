from dados import produtos, pessoas, lista

# novaLista = map(lambda x: x * 2, lista)
#novaLista = [x * 2 for x in lista]  --> list comprehesion
# print(list(novaLista))  #type casting

#acrescentar 5% a cada produto

'''
def aumentaPreço(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p


#novo dicionário que apresente apenas os preços
#preços = map(lambda p: p['preço'], produtos)
novosPreços = map(aumentaPreço, produtos)


for preço in novosPreços:
    print(f'{preço}')
'''

'''
def aumentaIdade(p):
    p['novaIdade'] = round(p['idade'] * 1.20)
    return p

idade = map(aumentaIdade, pessoas)

for pessoa in idade:
    print(pessoa)
'''
novasIdades = [p['idade'] * 2 for p in pessoas]

for idade in novasIdades:
    print(idade)