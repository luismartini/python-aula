listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]
listaSoma = [x + y for x, y in zip(listaA, listaB)]
print(listaSoma)
#  [2, 4, 6, 8]
#print(list(zip(listaA, listaB)))
# [(1, 1), (2, 2), (3, 3), (4, 4)]

'''
listaSoma = []
for i in range(len(listaB)):
    listaSoma.append(listaA[i] + listaB[i])
print(listaSoma)

[2, 4, 6, 8]
'''

'''
listaSoma = []
for i in range(len(listaB)):
    listaSoma.append(listaA[i] + listaB[i])
    print(listaSoma)
Output
[2]
[2, 4]
[2, 4, 6]
[2, 4, 6, 8]
'''

'''
Maneira pythonica

listaSoma = []
for i, _ in enumerate(listaB):
    listaSoma.append(listaA[i] + listaB[i])
print(listaSoma)
[2, 4, 6, 8]
'''

