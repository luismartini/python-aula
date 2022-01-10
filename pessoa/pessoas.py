'''
Programação Orientada a Objetos
'''
#criar um método-função
#self -> self refere-se a instância
#variáveis da instância
from datetime import datetime

class Pessoa:
    #variável da Classe/atributo da classe
    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))
    #Método - instância
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo!!!')
            return
        if self.falando:
            print(f'{self.nome} já está falando {assunto}.')
            return
        
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True
    
    def paraFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = False
        
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return  #não executa nada abaixo
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
        
        if self.falando:
            print(f'{self.nome} não pode comer falando!')
    
    def paraComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer!')
        self.comendo = False
    
    #variáveis da classe
    def getAnoNascimento(self):
        return self.anoAtual - self.idade