from random import randint

class Pessoa:
    anoAtual = 2022
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    #método de instância
    def getAnoNascimento(self):
        print(self.anoAtual - self.idade)
    
    @classmethod  #decorador #factory Method referente a classe
    def porAnoNascimento(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)
    
    @staticmethod
    def geraID():
        rand = randint(10000, 19999)
        return rand

# p1 = Pessoa.porAnoNascimento('Adele', 1948)
p1 = Pessoa('Luís', 44)
print(p1)
print(p1.nome, p1.idade)
p1.getAnoNascimento()
print(Pessoa.geraID())
print(p1.geraID())


#método factory que gera outro objeto
#class method
#relacionado com  a classe em si
