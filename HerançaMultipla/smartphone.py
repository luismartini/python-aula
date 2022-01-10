from eletronico import Eletrônico
from log import LogMixin

class Smartphone(Eletrônico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False
                #atributo de instância  
        
    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} nao está ligado'
            print(info)
            self.log_info(info)
            return
        
        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO'
            print(error)
            self.log_error(error)
            return
        
        info = f'{self._nome} ESTÁ CONECTADO'
        print(info)
        self.log_info(info)
        self._conectado = True
    
    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NÃO ESTÁ CONECTADO'
            print(error)
            self.log_error(error)
            return
        
        info = f'{self._nome} foi desligado com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False    