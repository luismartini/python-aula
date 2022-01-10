'''
Uma classe se associa a outra, mas vivem independentemente
'''
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
    
    @property
    def nome(self):
        return self.__nome
    
    @property  #getter
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter  #setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca
        
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        # self.__marca = marca
        print('Máquina de Escrever está escrevendo...')
    
    # @property
    # def marca(self):
    #     return self.__marca    