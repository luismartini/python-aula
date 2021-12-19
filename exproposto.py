string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
contadores = [i for i in range(0, len(string), n)]
lista = [string[i: i + n] for i in range(0, len(string), n)]
raw = [f'string[{i}: {i + n}]' for i in range(0, len(string), n)]
tuplas = [(i, i + n) for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(contadores)
print(lista)
print(raw)
print(tuplas)
print(retorno)


#print(comp)  #['0123456789', '0123456789', '0123456789', '0123456789']
#print(comp)  #[(0, 10), (10, 20), (20, 30), (30, 40)]
#print(comp)  #[0, 10, 20, 30]
# print(string[0:10]) # replicar
# print(string[10:20])
# comp = [string[i: i + n] for i in range(0, len(string), n)]