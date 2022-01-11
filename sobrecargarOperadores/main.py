'''
No Python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.
'''

class Retângulo:
    def __init__(self, x, y):  #métodos mágicos
        self.x = x
        self.y = y
        
    def getArea(self):
        return self.x * self.y
    
    def __repr__(self): #método mágico
        return f"<class 'Retângulo({self.x, self.y})'>"
    
    def __add__(self, other): #factorymethod
        novoX = self.x + other.x
        novoY = self.y + other.y
        return Retângulo(novoX, novoY)
    
    def __lt__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()
        
        if a1 < a2:
            return True
        else:
            return False
    
    
    def __gt__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()
        
        if a1 > a2:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
        
r1 = Retângulo(10, 20)
r2 = Retângulo(10, 20)
r3 = r1 + r2
print(r3)