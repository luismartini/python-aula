import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Luís', 'Martini']}
v = copy.deepcopy(d1)

v[1] = 'Luís'
v['d'] = ('Martini', 'Luís')

print(d1)  #valor de um não afeta o outro
print(v)

'''
d1 = v  # usando uma referências apenas
'''