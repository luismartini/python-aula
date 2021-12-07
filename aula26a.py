idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você deve colocar apenas números inteiros')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
# if idade >= 18:
#     print('Pode acessar.')
# else:
#     print('Não pode acessar.')

    msg = 'Pode acessar.' if (maior_idade) else 'Não pode acessar.'
    print(msg)