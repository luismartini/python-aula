'''
operadores lógicos
and
not
in
not in
'''
a = 2
b = 2
c = 3

print('1', a == b and a < c)
print('2', a == b or a < c)
print('3', not a == b and not b < c)

'''
(verdadeiro E falso) = Falso
#comparação1 and comparação2

#Verdadeiro Ou Verdadeiro
#comp1 or comp2

#not inversor
'''
w = 2
y = 3

if w > y:
    print('W é maior que Y')
else:
    print('Y é maior que W')

if not w > y:
    print('W é maior que Y')
else:
    print('Y é maior que W')
    
z = '' # ' ' passa ser falso
m = 0 # 0 é um boolean falso

if not m:
    print('Por favor, preencha o valor de z')

# in
nome = 'Luís Martini'

if 'rano' not in nome:
    print('Executei')
else:
    print('Existe')