'''
Sobreposição de métodos
'''
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
        
    def falar(self):
        print('Estou em CLIENTE.')

# class ClienteVIP(Cliente):  #Cliente e Pessoa
#     def falar(self):
#         # super().falar()
#         Pessoa.falar(self)
#         Cliente.falar(self)
#         print('Outra coisa qualquer...')

class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        # Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
    
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
        
'''
super().falar() superposição -- sempre na de cima
'''

