class A:
    vc = 123  #da classe
    
    def __init__(self): #inicializador
        #self.vc = 321
        pass

a1 = A()
a2 = A()

A.vc = 'Alterado'

print(a1.vc)
print(a2.vc)
print(A.vc)
