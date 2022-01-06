'''
zip - retorna um iterador next
count - Intertools
gera um contador
'''
from itertools import count

contador = count()

'''
count(start=10, step=5)
'''

lista = ['Luis', 'Jonice', 'Adele', 'José', 'Silva']
lista = zip(contador, lista)
print(list(lista))

#Looping infinito
# for valor in contador:
#     print(round(valor, 2))
    
#     if valor >= 10 or valor <= -10:
#         break

