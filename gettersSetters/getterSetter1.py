'''
Getters e Setters 1
'''
# SETTER = Set - configurando o valor (=)
# GETTER = OBTER um valor (.)

class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        #_ sustenta o valor
    
    @property  #GETTER -> obtém o valor do atributo com _
    def nome(self):
        return self._nome
    
    @nome.setter  #SETTER
    def nome(self, nome):
        self._nome = nome
        
    @property
    def sobrenome(self):
        return 'DESCONHECIDO'

p1 = Pessoa('Luís')
print(p1.nome)  #chamando o getter
print(p1.sobrenome) #chamando o setter


