d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Luís', 'Martini']}
v = d1.copy()

v[1] = 'Luisinho'
v['d'][0] = 'Joãozinho'  #acessar o valor de chave, item mutável

print(d1)
print(v)