from classe import Cliente

cliente1 = Cliente('Luís', 44)
cliente1.insereEndereço('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.listaEndereços()
print()
del cliente1
print('XXXXXX')

cliente2 = Cliente('Maria', 52)
cliente2.insereEndereço('Salvador', 'BA')
cliente2.insereEndereço('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.listaEndereços()
del cliente2
print('XXXXXXXXXXX')

cliente3 = Cliente('Jonice', 54)
cliente3.insereEndereço('Bauru', 'SP')
print(cliente3.nome)
cliente3.listaEndereços()
del cliente3
print('XXXXXXXXXXX')


print('#############################################')