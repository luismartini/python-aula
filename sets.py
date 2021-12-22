'''
add(adciona), uptade(atualiza), clear
discard
union | (une)
intersection & (todos os elementos presentes
nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
sets suportam apenas elementos únicos
'''
# s1 = {1,2,3,4,5,6}  #muito semelhante ao dicionário/ não tem par chave/valor
# for v in s1:
#     print(v)
    
# s2 = {} Estou criando um dicionário

# s2 = set()
# s2.add(1)
# s2.add(2)
# s2.add(3)
# #s2.discard(2)
# s2.update(['Luís'], {4,5,6})  #recebe um iterável/ Não respeitam ordem

# print(s2)

# l1 = [1,2,1,1,3,4,5,6,6,6,6,6,7,8,9]
# l1 = set(l1)
# l1 = list(l1)  #continua sem os elementos não duplicados
# print(l1[-1])

# s1 = {1,2,3,4,5}
# s2 = {1,2,3,4,5,6}
# s3 = s1 | s2  #pipe
# print(s3)

# s1 = {1,2,3,4,5}
# s2 = {1,2,3,4,5,6}
# s3 = s1 & s2  #intersection
# print(s3)

# s1 = {1,2,3,4,5,7 }
# s2 = {1,2,3,4,5,6}
# s3 = s1 - s2  #diferença = elementos apenas da esquerda
# print(s3)

# s1 = {1,2,3,4,5,7}
# s2 = {1,2,3,4,5,6}
# s3 = s1 ^ s2  #symmetric_diference
# print(s3)

l1 = ['Luís', 'João', 'Maria']
l2 = ['João', 'Maria', 'Luís']

l1 = list(set(l1))
l2 = list(set(l2))

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')