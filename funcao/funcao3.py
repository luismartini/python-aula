'''
Função - Parte 3 - *args **kwargs
'''

# def func(a1, a2, a3, a4, a5):
#     print(a1, a2, a3, a4, a5)

# func(1,2,3,4,5)

# def func(a1,a2,a3,a4,a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#     return nome, a6

# var = func(1,2,3,4,5, nome='Luís', a6='Martini')  #Sempre nomear o argumento 
# print(var[0], var[1])  #retorna tupla

'''
Args e Kwargs
'''
#def func(*args): #empacotamento em uma tupla
#    print(args)  #(1,2,3,4,5)
#    print(args[0])  #1
#    print(args[-1])  #5
#    print(len(args))  #5
    
#var = func()

#lista = [1,2,3,4,5]
#n1, n2, *n = lista  #*n restante da lista/desempacotando/empacotando

#print(n1, n2, n)
#print(*lista, sep='-')  #output 1 2 3 4 5 / 1-2-3-4-5

#func(1,2,3,4,5)  #(1, 2, 3, 4, 5)

#tupla não pode ser alterada

'''
Converter tupla em lista
'''

# def func1(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)
    
# func1(1,2,3,4,5)  #20

# def func2(*args):
#     # for v in args:
#     #     print(v)
#     print(args)


# lista = [1,2,3,4,5]
# lista2 = [10,20, 30, 40, 50]
# func2(*lista, *lista2)  #desempacotada  #(1,2,3,4,5)
# #entra como índice da tupla

def func3(*args, **kwargs): #convenção
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])
    
    idade = kwargs.get('idade')  #se não tem certeza
    #print(idade)  #None. Não enviei idade
    
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')
    
    
lista = [1, 2, 3, 4, 5]
lista1 = [10, 20, 30, 40, 50]

func3(*lista, *lista1, nome = 'Luís', sobrenome='Martini', idade = 30)