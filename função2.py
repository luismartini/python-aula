'''
Função - Parte (2)
return

Geralmente não se utiliza print() em função
'''

# def funcao(var):
#     return var
#     print('Isso não será executado!')
    
# variável = funcao('Valor que eu quero')

# if variável:
#     print(variável)
# else:
#     print('Nenhum valor')

#retorna None é um tipo de dado. None = Não-valor.

# def divisao(n1, n2):
#     if n2 > 0:
#         return n1 / n2

# divide = divisao(8, 0)

# if divide:
#     print(divide)  #None
# else:
#     print('Conta inválida')

# def divisao(n1, n2):
#     if n2 == 0:
#         return
#     return n1 / n2

# divide = divisao(8,0)

# if divide:
#     print(divide)
# else:
#     print('Conta inválida')

# def f(var):
#     print(var)

# def dumb():
#     return f  #só é executada com os parenteses 

# var = dumb()  #('E colocar meu valor aqui!')

# # print(id(var), id(f))

# # if var == f:
# #     print('Var é igual a F')
# # else:
# #     print('Blaaaa')
# var('Pode imprimir algo na tela')

def dumb():
    return 'Luís', 'Martini'

var = dumb()
print(var, type(var))
