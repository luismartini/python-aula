'''
Função (def) em Python = *args **kwargs
'''
'''
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func(1,2,3,4,5, nome='Luís', a6=5)
print(var[0], var[1])
'''
'''
# Não sabe quantos argumentos
def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

lista = [1,2,3,4,5]
#n1, n2, *n = lista  #desempacotando/empacotando *n
#print(n1, n2, n)  #restante da lista
print(*lista, sep='*') #desempacotando 1 2 3 4 5


func(1,2,3,4,5)  #(1, 2, 3, 4, 5)
Tupla não pode ser alterada
lista []
'''
'''
def func(*args):
    args = list(args)
    args[0] = 20
    print(args)
func(1,2,3,4,5)
'''

'''
def func(*args):
#    for v in args:
    print(args)
lista = [1,2,3,4,5]
lista1 = [10,20,30,40,50]
func(*lista, *lista1)
'''

def func(*args, **kwargs):  #kwargs -> keywords arguments
    print(args)
    #print(kwargs['nome'], kwargs['sobrenome'])  #{'nome': 'Luís', 'sobrenome': 'Martini'}
    # Luís Martini
    idade = kwargs.get('idade')
    
    #idade = kwargs['idade]
    #print(idade)
    
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')
    
lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

func(*lista, *lista2, nome='Luís', sobrenome = 'Martini', idade = 44)