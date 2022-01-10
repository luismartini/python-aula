class A:
    def falar(self):
        print('Falando... Estou na A.')

class B(A):
    def falar(self):
        print('Falando... Estou na B.')

class C(A):
    def falar(self):
        print('Falando... Estou na C.')

        # ->
class D(B, C):
    pass

d = D()
d.falar()

#Classe Mixing --> não foi feita para ser instanciada.