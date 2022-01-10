'''
Relação mais forte
'''
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
#especializar a classe
        self.endereços = []
        
    def insereEndereço(self, cidade, estado):
        self.endereços.append(Endereço(cidade, estado))
        
    def listaEndereços(self):
        for endereço in self.endereços:
            print(endereço.cidade, endereço.estado)
    
    def __del__(self):
        print(f'{self.nome} foi apagado')

class Endereço:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    def __del__(self):
        print(f'{self.cidade}/{self.estado} foram apagados')