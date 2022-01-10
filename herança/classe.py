class Pessoa:  #SuperClasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__  #
        #self.__class__.__name__
        
    def falar(self):
        print(f'{self.nomeclasse} está falando...')

class Cliente(Pessoa):  #subclasse #especializada
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

class Aluno(Pessoa):  #subclasse #herdam
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')