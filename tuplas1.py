'''
Tuplas - você não edita os elementos da tuplas
'''
#t1 = (1,2,3, 'a', 'Luís Martini')

# for v in t1:
#     print(v)

#print(type(t1))
#print(t1[4])

'''
Sem parenteses
'''
# t1 = 1,2,'Luís',4,5
# t2 = 6,7,8,9,10  #precisa de vírgula
# t3 = t1 + t2

# n1, n2, n3, *_, n10 = t3

# print(n10)

'''
Repetir
'''
# t1 = (1,2,3,4,5) * 10
# print(t1)

'''
Converter tuplas em listas
'''
t2 = (1,2,3,4,5)
t2 = list(t2)
t2[1] = 3
t2 = tuple(t2)  #redundante  #objeto apenas para leitura
print(t2)
