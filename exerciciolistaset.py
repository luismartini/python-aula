'''
Se não encontrar nada, retorne -1
retorne a duplicação considerada
'''

lista_de_listas_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,8,1,2,3,4,6,5,7,8],
    [2,2,4,5,2,4,5,6,7,8],
    [1,2,3,4,5,6,7,8,9,9],
    [10,9,8,7,6,5,4,3,2,1],
    [9,8,7,6,5,4,9,7,6,5],
    [1,1,1,2,2,2,3,3,3,4],
    [9,8,7,6,5,4,3,2,1,1],
    [10,10,9,9,8,8,7,7,1,2],
    [1,2,3,4,5,6,7,8,9,9],
]
def encontraDuplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    
    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        
        numeros_checados.add(numero)
        print(numeros_checados)
    
    return primeiro_duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontraDuplicado(lista_de_inteiros))

