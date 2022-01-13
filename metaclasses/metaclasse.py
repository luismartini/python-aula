'''
Em python tudo é objeto: incluindo as classes.
Metaclasses são as classes que criam  classes.
type é uma metaclasse (!!!!?????)
'''
'''
class A:
    attr = 'Valor'
    #atributo de classe

#instância
a = A()
b = A()
c = A()
'''
# Para criar um framework
#Criei uma metaclasse
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        # print(name)
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        
        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['attr_classe']
        
        #print(namespace)  #{'__module__': '__main__', '__qualname__': 'B'}
        
        # if 'b_fala' not in namespace:
        #     print(f'Oi, você precisa criar o método b_fala em {name}')
        # else:
        #     if not callable(namespace['b_fala']):
        #         print(f'b_fala precisa ser um método, não um atributo em {name}')
        
        return type.__new__(mcs, name, bases, namespace)

# class A(metaclass=Meta):  #criar bibliotecas
#     def fala(self):
#         self.b_fala()


# class B(A):  #Criar Interfaces
#     teste = 'Valor'

#     def b_fala(self):
#         print('Oi')
        
#     def sei_la(self):
#         pass
# #classes abstratadas
class A(metaclass=Meta):
    #Não quero permitir que seja sobrescrito
    attr_classe = 'Valor A'

class B(A):
    attr_classe = 'Valor B'

class C(B):
    attr_classe = 'Valor C'
    
# b = B()
# print(b.attr_classe)
c = C()
print(c.attr_classe)