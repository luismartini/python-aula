'''
1- Crie uma funçao1 que recebe uma função2 como parâmetro
e retorne o valor função2 executada.
'''

# def ola_mundo():
#     return 'Olá, mundo!'

# def mestre(funcao):
#     return funcao()  #() executando a função

# executando = mestre(ola_mundo)

# print(executando)
# #print(ola_mundo())

'''
2- Crie uma função1 que recebe uma função2 como
parâmetro e retorne o valor da função2 executada. Faça a função1
executar duas funções que recebam um número diferente de argumentos

'''
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'



executando = mestre(fala_oi, 'Luís') 
executando2 = mestre(saudacao, 'Luís', saudacao='Bom dia')
print(executando)
print(executando2)
