'''
pop
popitem
'''
d1 = {
    1:2,
    2:3,
    4:5,
}

# d1.popitem()
# print(d1)

'''
Concatenar
Sinal de + não funciona
'''
d2 = {
    'a':'b',
    'c':'d',
}
print(d1)
print(d2)
d1.update(d2)
print(d1)