from dados import lista, pessoas, produtos

# List Comprehesion
#novaLista = [x for x in lista if x > 5]
'''
novaLista = filter(lambda x: x > 5, lista)
print(list(novaLista))
'''
'''
def filtra(produtos):
    if produtos['preço'] > 50:
        produtos['e_caro'] = True
    return True

novoProduto = filter(filtra, produtos)

for produto in novoProduto:
    print(produto)
'''

def filtra(pessoa):
    if pessoa['idade'] >= 18:
        pessoa['e_maior'] = True
        return True
    elif pessoa['idade'] < 18:
        pessoa['e_menor'] = True
        return True

#menoresIdade = filter(filtra, pessoas)

#list comprehesion
menoresIdade = filter(lambda p: p['idade'] if p['idade'] < 18 else False, pessoas)

for idade in menoresIdade:
    print(idade)