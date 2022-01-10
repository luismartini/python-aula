'''
Associação - usa | Agregação - tem 
| Composição é dono | herança é outro objeto
'''
from classe import *

c1 = Cliente('Luís', 44)
print(c1.nome, c1.idade)
c1.comprar()

a1 = Aluno('Luís', 44)
print(a1.nome, a1.idade)
a1.estudar()


p1 = Pessoa('João', 43)
p1.falar()