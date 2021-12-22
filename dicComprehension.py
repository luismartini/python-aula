'''
Dictionary/set comprehension
'''

'''

d1 = {k: v for k, v in lista}
#d1 = dict(lista)
print(d1)

'''

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1, type(d1))