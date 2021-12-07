'''
Condição IF, ELIF e ELSE
'''
from time import sleep

nome = input('Qual seu nome: ')
senha = int(input('Qual sua senha: '))

if senha == 14071977 and nome == 'Luís':
    print('Você será logado ao sistema!')
    sleep(2)
    print('Finalizando...')
    sleep(2)
    print(f'Acesso concedido! {nome}')
else:
    print('Você não tem permissão para logar no sistema')

# if False:
#     print('Verdadeiro')
# elif False:
#     print('Agora é verdadeiro')
# elif False:
#     print('Mais uma verdadeira')
# else:
#     print('Agora é verdadeira')