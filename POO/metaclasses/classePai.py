class Pai:
    nome = 'Teste'

A = type('A', (Pai,), {'attr': 'Olá, mundo!'})
                #isso é uma tupla, por isso uma vírgula no final
a = A()
print(a.nome)