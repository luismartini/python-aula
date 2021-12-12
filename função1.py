'''
Funções - def em Python (Parte 1)
    def -> definir função
    função ajuda a funcionalidade mais rápida
'''


'''
funcao(parâmetro)

função(valores)
'''

# def funcao():
#     print('Olá, mundo!')

# funcao()
# funcao()
# funcao()
# funcao()


# def escrever(msg):
#     print(msg)

# escrever('O que eu quiser!')

# def saudacao(msg, nome):
#     print(msg, nome)
    
# saudacao('Olá,', 'Luís Martini')

def saudacao(msg='Olá,', nome='usuário'):
    nome = nome.replace('i', '3')
    msg = msg.replace('i', '3')
    return f'{msg} {nome}'
#    print(msg, nome)

#saudacao(nome = 'Zezinho', msg = 'Hi')
variável = saudacao()

print(variável)