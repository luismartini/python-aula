'''
https://rszalski.github.io/magicmethods/

Em Python, toda classe deriva de 'objetct'
'''


class A:
    def __new__(cls, *args, **kwargs):  #construtor
        
        def haha(*args, **kwargs):
            print('Fala OI')
        # return super().__new__(cls)
        # print('Eu sou o new')
        cls.nome = 'Luís'
        cls.haha = haha
        
        return object.__new__(cls)
    def __init__(self):  #construtor
        print('Eu sou o INIT')

a = A()
print(a.nome)
a.haha()

'''
O __new__ não inicia antes do __init__?
'''


