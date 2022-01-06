'''
Escopo de variáveis
Global
Local
'''

variavel = 'valor'  #escopo global

def func():
    print(variavel)
    
    
def func2(arg=None):
    #variável global
    # global variavel  #Não é uma boa prática
    # variavel = 'outro valor'  #escopo local
    # print(variavel)
    arg = arg.replace('v', 'c')
    return arg

func()
outra_variavel = func2(arg=variavel)

#func2(arg=variavel)

print(outra_variavel)  #volta a ser global