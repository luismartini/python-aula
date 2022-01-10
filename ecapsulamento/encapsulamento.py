'''
POO clássica
public, protected, private  --> ir contra a filosofia do python

_ privado/protected (publico), mais fraco e sutil / protected
__ privado (_NOMECLASSE__nomeatributo): ele vai proibir de acessar 
:: renomeia os atributos

Encapsulamento: serve para esconder partes do código;
atributo ou método.
'''
class BaseDeDados:
        #construtor
    def __init__(self):
        self.__dados = {}  
        #Atributo da minha classe é público
        #A classe para de funcionar
        #__ não quero que de maneira alguma esse atributo seja acessado
        
    @property
    def dados(self):
        return self.__dados
        
    def inserirCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    
    def listaClientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apagaCliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserirCliente(1, 'Luís')
bd.inserirCliente(2, 'Jonice')
bd.inserirCliente(3, 'Adele')
bd.__dados = 'Outra coisa'  #cfriei um atributo e acessei 
#renomeia
# Dar acesso aos valores
#bd.dados = 'Outro valor'
print(bd.dados)