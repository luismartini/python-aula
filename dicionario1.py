clientes = {
    'cliente1' : {
        'nome' : 'Luís',
        'sobrenome' : 'Martini',
    },
    'cliente2' : {
        'nome' : 'Paulo',
        'sobrenome' : 'Silva',
    },
    'cliente3' : {
        'nome' : 'Maria',
        'sobrenome' : 'Silva',
    },
}

# dicionários com filhos dicionários

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')