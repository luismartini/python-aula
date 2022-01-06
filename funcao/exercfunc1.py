'''
1- Crie uma funçao1 que recebe uma função2 como parâmetro
e retorne o valor função2 executada.
'''

def ola_mundo():
    return 'Olá, mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)

print(executando)
print(ola_mundo())