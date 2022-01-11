class A:
    # def __new__(cls, *args, **kwargs):
    #     #designer pattern
        
    #     if not hasattr(cls, '_jaexiste'):
    #         cls._jaexiste = object.__new__(cls)
        
    #     return cls._jaexiste
    
    def __init__(self):
        pass
        # print('Eu sou o INIT')
        
    # def __call__(self, *args, **kwargs):
    #     # faz minha classe funcionar como uma função
    #     # *args = argumentos
    #     #**kwargs = argumentos nomeados - key word arguments = {}
    #     # print(args)
    #     # print(kwargs)
    #     resultado = 1
    #     for i in args:
    #         resultado *= i
    #     return resultado

    # def __setattr__(self, name, value):
    #     if name == 'nome':
    #         self.__dict__[name] = 'Você não pode fazer isso'
    #     else:
    #         self.__dict__[name] = value
    
    # def __del__(self):
    #     print('Objeto coletado.')
    
    # def __str__(self):
    #     return "<class A>"
    
    def __len__(self):
        return 55

a = A()
print(len(a))