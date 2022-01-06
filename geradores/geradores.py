'''
iterável - pode iterar, não vai dar um valor de cada vez
'''
#lista = [0,1,2,3,4,5]
#lista = iter(lista) #Lista se tornou um iterador
# para ser um iterador, a lista usa o método '__iter__'
#print(hasattr(lista, '__iter__'))
#hasattr -> Sua principal tarefa é verificar 
# se um objeto tem o atributo nomeado fornecido e 
# retornar verdadeiro se presente, caso contrário, falso.


'''
Geradores
usar muita memória
'''
import sys
import time

# lista = list(range(10000))  
# #recebe todos os valores de uma vez, e salvando na memória
# print(sys.getsizeof(lista))

# def gera():
#     for n in range(100):
#         yield n  #lazy evaluation
#         time.sleep(0.1)

# g = gera()
#print(g)  #<generator object gera at 0x0000020786045EE0>

# for v in g:
#     print(v)  #lazy evaluetion

# print(hasattr(g, '__iter__'))
# print(hasattr(g, '__next__'))

# pode ser usado o método next

# def gera():
#     variável = 'Valor 1'
#     yield variável
#     variável = 'Valor 2'
#     yield variável
#     variável = 'Valor 3'
#     yield variável

# g = gera()

# # print(next(g))
# # print(next(g))
# # print(next(g))

# for v in g:
#     print(v)

l1 = [x for x in range(10)]  #reter todos os valores
l2 = (x for x in range(10))  #não salva os valores na memória

# print(sys.getsizeof(l1))
# print(sys.getsizeof(l2))
for v in l2:
    print(v)