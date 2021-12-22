import sys
import time

# def gera():
#     variavel = 'valor 1'
#     yield variavel
#     variavel = 'valor 2'
#     yield variavel
#     variavel = 'valor 3'
#     yield variavel
    
# g = gera()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  #StopIteration
# for v in g:
#     print(v)

'''
Memória
'''
l1 = [x for x in range(100000)]
# print(type(l1))
l2 = (x for x in range(100000))
# print(type(l2))
# print(sys.getsizeof(l1))  #8856
# print(sys.getsizeof(l2))  #112

for v in l2:
    print(v)
