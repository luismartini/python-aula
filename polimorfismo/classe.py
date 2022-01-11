'''
Polimorfismo é o princípio que permite que classes derivadas de uma mesma
superclasse tenham métodos iguais (de mesma assinatura), mas comportamentos
diferentes.
Mesma assinatura = mesma quantidade e tipo de parâmetros
'''
from abc import ABC, abstractmethod

class A(ABC): #superclasse
    @abstractmethod
    def fala(self, msg): pass
    
class B(A):
    def fala(self, msg):
        print(f'B está falando: {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando: {msg}')

b = B()
c = C()
b.fala('Um assunto')
c.fala('Outro assunto')
'''
poliformismo de sobreposição
B está falando: Um assunto
C está falando: Outro assunto
'''