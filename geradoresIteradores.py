'''
Geradores
Iteradores


Iteráveis

Método hasattr e __iter__
'''

'''
lista1 = 1234
lista2 = 'String'

print(hasattr(lista2, '__iter__'))

'''

'''
lista = [0,1,2,3,4,5]
lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
'''

'''
next() - iterador
'''

# print(hasattr(lista, '__next__'))
'''
Gerador
sys
sys.getsizeof()
import sys
lista = list(range(1))

print(sys.getsizeof(lista))
'''
import sys
import time

def gera():
    for n in range(100):
        yield n  #yield
        time.sleep(0.1)
        
g = gera()

# print(g)
# for v in g:
#     print(v)
    
'''
iteradores método __next__
'''
# print(hasattr(g, '__iter__'))
# print(hasattr(g, '__next__'))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))